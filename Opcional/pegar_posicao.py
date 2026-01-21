import pyautogui
import keyboard
import time
#Caso queiram ver como pegar a pocição do mouse para clicar
print("Aperte 'z' para capturar a posição, ou ESC para sair.")

while True:
    if keyboard.is_pressed("z"):
        print("Posição:", pyautogui.position())
        time.sleep(0.3)  # evita múltiplos cliques
        
    if keyboard.is_pressed("esc"):
        print("Encerrado.")
        break
