import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class FrmExercicio_02_25052024(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master

        frmBotoes = FrmBotoes(self)
        frmBotoes.grid(row=0, column=0, padx=30, pady=20, sticky='WSEW')


class FrmBotoes(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.btnWidth = 35
        self.btnPadx = 10
        self.btnPady = 5

        btnMensagem = tk.Button(self, width= self.btnWidth, background="gray", text="Mensagem",
                                command=self.enviarMensagem)
        btnMensagem.grid(row=4, column=0, padx=self.btnPadx, pady=self.btnPady, sticky='WSEW')
        btnMensagem.pack()


    def enviarMensagem(self):
        tk.messagebox.showinfo("Mensagem", "Mensagem enviada com sucesso!")


