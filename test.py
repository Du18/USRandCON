import tkinter
from PIL import ImageTk, Image
from time import sleep

mainGUI = tkinter.Tk()
mainGUI.title("JoTha")
mainGUI.geometry("360x350")
#mainGUI.resizable(False, False)
fondo = Image.open("jotha.png")
fondo = ImageTk.PhotoImage(fondo)
label = tkinter.Label(mainGUI, image=fondo)
label.pack()
userGui = tkinter.Label(mainGUI, text="USUARIO", padx=5, pady=5, font=("Arial", 8, "bold"), fg="white")
userGui.configure(bg="#1E1E1E") 
userGui.place(x=145, y=140)

mainGUI.mainloop()