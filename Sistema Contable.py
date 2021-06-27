from tkinter import *
from tkinter import ttk
from Menu_Principal import menu_principal
from tkinter import messagebox
import os

class Sistema_contable:
    def __init__(self, ventana):
        self.ventana = ventana
        self.encabezado = Frame(self.ventana, height="50")
        self.encabezado.config(bg="DodgerBlue4")
        self.encabezado.pack(fill = X)
        Label(self.encabezado, text="SISTEMA CONTABLE", font=("Arial",20,"bold"),bg="DodgerBlue4",fg="snow").place(x=95, y=5)
        Label(self.ventana, text="Usuario", bg="AntiqueWhite1").place(x=75,y=75)
        Label(self.ventana, text="Contraseña", bg="AntiqueWhite1").place(x=70,y=100)
        self.caja_usuario = Entry(ventana, font="Helvetica 15")
        self.caja_usuario.place(x=150, y=75)
        self.caja_usuario.focus()
        self.caja_contraseña = Entry(self.ventana, font="Helvetica 15")
        self.caja_contraseña.place(x=150, y=100)
        self.caja_contraseña.config(show="*")
        self.boton = Button(ventana, text="Verificar", command = self.verificacion)
        self.boton.pack()
        self.boton.place(x=230, y=140)
        self.etiqueta = Label(ventana)
        self.etiqueta.config(bg="AntiqueWhite1")
        self.etiqueta.pack()
    def mensaje(self):
        messagebox.showerror("Comercial Coronado", "Usuario o Contraseña Incorrectos")
    def verificacion(self):
        if self.caja_contraseña.get() == "1331" and self.caja_usuario.get() == "ACL":
            self.etiqueta["text"] = "Bienvenido"
            self.boton = Button(ventana, text="Ingresar", command = menu_principal)
            self.boton.pack()
            self.boton.place(x=230,y=140)
        else:
            self.etiqueta["text"] = "Usuario o Contraseña Incorrectos"
            self.mensaje()
if __name__ == '__main__':
    ventana = Tk()
    ventana.geometry("500x200")
    ventana.resizable(0,0)
    ventana.config(bg="AntiqueWhite1")
    Aplicacion = Sistema_contable(ventana)
    ventana.mainloop()