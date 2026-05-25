import json
import os

catalog_path = "catalog.json"
api_catalogue_dir = "api-catalogue"
output_path = "catalog_enrichi.json"

with open(catalog_path, "r", encoding="utf-8") as f:
    catalog = json.load(f)

catalog_enrichi = []

for api in catalog:
    name = api["name"]
    swagger_path = os.path.join(api_catalogue_dir, f"{name}.json")
    
    try:
        with open(swagger_path, "r", encoding="utf-8") as f:
            swagger = json.load(f)
        
        info = swagger.get("info", {})
        
        # Endpoints enrichis
        endpoints = []
        for path, methods in swagger.get("paths", {}).items():
            # Paramètres de path partagés
            path_params = [p['name'] for p in methods.get("parameters", [])]
            
            for method, details in methods.items():
                if method not in ['get', 'post', 'put', 'delete', 'patch', 'options']:
                    continue
                if not isinstance(details, dict):
                    continue
                
                # Champs requis depuis requestBody
                required_fields = list(path_params)
                optional_fields = []
                
                rb = details.get("requestBody", {})
                schema = rb.get("content", {}).get("application/json", {}).get("schema", {})
                required_fields += schema.get("required", [])
                all_props = list(schema.get("properties", {}).keys())
                optional_fields = [p for p in all_props if p not in required_fields]
                
                # Paramètres de query/path
                for param in details.get("parameters", []):
                    if param.get("required") and param["name"] not in required_fields:
                        required_fields.append(param["name"])
                    elif not param.get("required") and param["name"] not in optional_fields:
                        optional_fields.append(param["name"])
                
                # Réponses
                responses = details.get("responses", {})
                response_summary = " | ".join([
                    f"{code} — {resp.get('description', '')}"
                    for code, resp in responses.items()
                ])
                
                endpoints.append({
                    "method": method.upper(),
                    "path": path,
                    "summary": details.get("summary", ""),
                    "operationId": details.get("operationId", ""),
                    "required_fields": required_fields,
                    "optional_fields": optional_fields,
                    "response": response_summary
                })
        
        # Schemas enrichis
        schemas = {}
        for schema_name, schema_def in swagger.get("components", {}).get("schemas", {}).items():
            props = list(schema_def.get("properties", {}).keys())
            required = schema_def.get("required", [])
            schemas[schema_name] = {
                "properties": props,
                "required": required
            }
        
        # Authentification
        security_schemes = swagger.get("components", {}).get("securitySchemes", {})
        auth = ""
        for scheme_name, scheme in security_schemes.items():
            auth = f"{scheme_name} — {scheme.get('description', scheme.get('type', ''))}"
        
        # Serveur
        servers = swagger.get("servers", [])
        server = f"{servers[0]['url']} — {servers[0].get('description', '')}" if servers else ""
        
        api_enrichi = {
            "name": name,
            "title": info.get("title", name),
            "version": info.get("x-api-version", "v1"),
            "status": info.get("x-status", api["status"]),
            "domain": info.get("x-domain", api["domain"]),
            "team": info.get("x-team", ""),
            "description": info.get("description", api["description"]),
            "endpoints": endpoints,
            "schemas": schemas,
            "authentication": auth,
            "server": server
        }
        
        catalog_enrichi.append(api_enrichi)
        print(f"✅ {name} — {len(endpoints)} endpoints, {len(schemas)} schemas")
        
    except FileNotFoundError:
        catalog_enrichi.append(api)
        print(f"⚠️ {name} — fichier swagger non trouvé")
    except Exception as e:
        catalog_enrichi.append(api)
        print(f"❌ {name} — erreur : {e}")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(catalog_enrichi, f, ensure_ascii=False, indent=2)

taille_enrichi = os.path.getsize(output_path) / 1024
taille_original = os.path.getsize(catalog_path) / 1024
print(f"\n✅ Total : {len(catalog_enrichi)} APIs enrichies")
print(f"📁 catalog_enrichi.json : {taille_enrichi:.0f} KB")
print(f"📁 catalog.json original : {taille_original:.0f} KB")
print(f"📈 Ratio enrichissement : {taille_enrichi/taille_original:.1f}x")