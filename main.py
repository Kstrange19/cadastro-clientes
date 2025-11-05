from tkinter import *

window = Tk()

class Application:
    def __init__(self):
        self.window = window
        self.tela()
        self.frames_da_tela()
        self.botoes_frame1()
        self.window.mainloop()
    def tela(self):
        self.window.title("Cadastro de Clientes")
        self.window.configure(background='#234299')
        self.window.geometry("1920x1080")
        # Redimensionar - Horizontal, Vertical
        self.window.resizable(True, True)
        self.window.maxsize(width=1920, height=1080)
        self.window.minsize(800, 600)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.window, border=4, background='#ffffff',
                        # Cor e largura da borda do frame
                            highlightbackground="#FFB74D", highlightthickness=4)
        
        '''O valor mínimo e máximo aceitos pelos relativos são 0 e 1'''
        # relx = localização no eixo x da tela em porcentagem;
        # rely = localização no eixo y da tela em porcentagem;
        # relwidth e relheight = comprimento e altura relativos do frame (variam com o aumento da tela)
        self.frame_1.place(relx=0.005 ,rely=0.005, relwidth= 0.990, relheight=0.490)

        self.frame_2 = Frame(self.window, bd=2, background="#ffffff",
                            highlightbackground="#FFB74D", highlightthickness=4)
        self.frame_2.place(relx=0.005, rely=0.505, relwidth=0.990, relheight=0.490)
    def botoes_frame1(self):
        ### Criação do botão limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=4, bg="#234299", fg='white', font=('arial', 11,))
        self.bt_limpar.place(relx=0.2, rely=0.08, relwidth=0.1, relheight=0.15)
        
        ### Criação do botão buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=4, bg="#234299", fg='white', font=('arial', 11,))
        self.bt_buscar.place(relx=0.3, rely=0.08, relwidth=0.1, relheight=0.15)
        
        ### Criação do botão novo
        self.bt_buscar = Button(self.frame_1, text="Novo", bd=4, bg="#234299", fg='white', font=('arial', 11,))
        self.bt_buscar.place(relx=0.6, rely=0.08, relwidth=0.1, relheight=0.15)
        
        ### Criação do botão alterar
        self.bt_buscar = Button(self.frame_1, text="Alterar", bd=4, bg="#234299", fg='white', font=('arial', 11,))
        self.bt_buscar.place(relx=0.7, rely=0.08, relwidth=0.1, relheight=0.15)
        
        ### Criação do botão apagar
        self.bt_buscar = Button(self.frame_1, text="Apagar", bd=4, bg="#234299", fg='white', font=('arial', 11,))
        self.bt_buscar.place(relx=0.8, rely=0.08, relwidth=0.1, relheight=0.15)

Application()