import tkinter
from PIL import ImageTk, Image

mainGUI = tkinter.Tk()
mainGUI.title("JoTha")
mainGUI.geometry("360x350")
mainGUI.resizable(False, False)
fondo = Image.open("jotha.png")
fondo = ImageTk.PhotoImage(fondo)

label = tkinter.Label(mainGUI, image=fondo)
label.pack()


mainGUI.mainloop()