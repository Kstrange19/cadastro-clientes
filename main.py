from tkinter import Tk

window = Tk()

class Application:
    def __init__(self):
        self.window = window
        self.tela()
        self.window.mainloop()
    def tela(self):
        self.window.title("Cadastro de Clientes")
        self.window.configure(background='#234299')
        self.window.geometry("1920x1080")
        # Redimensionar - Horizontal, Vertical
        self.window.resizable(True, True)
        self.window.maxsize(1920, 1080)
        self.window.minsize(800, 600)

Application()