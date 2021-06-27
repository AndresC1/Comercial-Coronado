from tkinter import *
from tkinter import ttk
import sqlite3

def prueba():
    class pru:
        Base_Producto = 'Base_de_datos_Productos.db'
        def __init__(self, ventana):
            self.ventana = ventana
            self.var=StringVar(self.ventana)
            self.var.set("Mes")
            opciones=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
            opcion=OptionMenu(self.ventana,self.var,*opciones)
            opcion.config(width=15)
            opcion.pack(side='left', padx=30, pady=30)
            
            Button(self.ventana, command=self.valor).place(x=0,y=0)
        def valor(self):
            print(self.var.get())
    ventana = Tk()
    ventana.geometry("800x560")
    ventana.resizable(0,0)
    window = pru(ventana)
    ventana.mainloop()
prueba()