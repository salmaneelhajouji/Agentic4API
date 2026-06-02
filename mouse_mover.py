import pyautogui
import time
import sys

# Définit le temps d'attente entre chaque mouvement (en secondes)
# 60 secondes = 1 minute
INTERVALLE_SECONDES = 60 

print("Le script 'Mouse Mover' est en cours d'exécution...")
print("Appuyez sur Ctrl+C dans ce terminal pour l'arrêter.")

try:
    while True:
        # Déplace la souris de 1 pixel vers la droite, puis de 1 pixel vers la gauche
        # Le mouvement est si petit qu'il est invisible, mais suffisant pour le système
        pyautogui.move(1, 0)
        pyautogui.move(-1, 0)
        
        # Le script fait une pause pendant l'intervalle défini
        time.sleep(INTERVALLE_SECONDES)

except KeyboardInterrupt:
    # Permet de quitter proprement quand vous appuyez sur Ctrl+C
    print("\nScript arrêté par l'utilisateur. Au revoir !")
    sys.exit()