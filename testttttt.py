import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image
from time import sleep
import requests

url = 'https://raw.githubusercontent.com/Du18/USRandCON/refs/heads/main/usrandcon.json'
def MainAccount():
    response = requests.get(url)
    if response.status_code == 200:
        usuarios = response.json()
        def UserBrowse(usuario_buscado, contrasena_buscada):
            for usuario in usuarios:
                if usuario["usuario"] == usuario_buscado and usuario["contraseña"] == contrasena_buscada:
                    return True  
            return False 
        usuario_buscado = Usertext.get()
        contrasena_buscada = ConText.get()

        if UserBrowse(usuario_buscado, contrasena_buscada):
            print("Acceso permitido")
        else:
            messagebox.showerror("002", "User or Password incorrect")

    else:
        messagebox.showerror("001", "Data Base Error")

mainGUI = tkinter.Tk()
mainGUI.title("JoTha")
mainGUI.geometry("360x350")
mainGUI.resizable(False, False)
fondo = Image.open("jotha.png")
fondo = ImageTk.PhotoImage(fondo)
label = tkinter.Label(mainGUI, image=fondo)
label.pack()
userGui = tkinter.Label(mainGUI, text="USUARIO", padx=5, pady=5, font=("Arial", 9, "bold"), fg="white")
userGui.configure(bg="#1E1E1E") 
userGui.place(x=144, y=140)
Usertext = tkinter.Entry(mainGUI)
Usertext.place(x=115, y=170)
conGui = tkinter.Label(mainGUI,text="CONTRASEÑA", padx=5, pady=5, font=("Arial", 9, "bold"), fg="white")
conGui.configure(bg="#1E1E1E") 
conGui.place(x=132, y=197)
ConText = tkinter.Entry(mainGUI, show="•")
ConText.place(x=115, y=230)
Bmain = tkinter.Button(mainGUI, text="CONTINUE", command=MainAccount)
Bmain.place(x=143, y=275)
mainGUI.mainloop()