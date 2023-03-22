import pyautogui as r

print("")
r.displayMousePosition()

print("\n Digite en el siguiente formato (x-y)...")

x, y = (input(" >>> Digite cordenadas (x, y): ")).split("-")

while True:
    opc = input("\n >>> Digite un Comando: ")
    
    if opc == "1":
        txt = "Hola Mundo!"
        r.moveTo(int(x.strip()), int(y.strip()), 0.3)
        r.click()
        r.write(txt, 0.05)

    if opc == "go":
        txt = ""
        with open("./text.txt", "r") as f: txt = f.read() 
        r.moveTo(int(x.strip()), int(y.strip()), 0.3)
        r.click()
        r.write(txt, 0.05)

    if opc == "slr" or opc == "exit": break

#* Author: Francisco Velez
