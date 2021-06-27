from tkinter import *
from tkinter import ttk
from Invenatario import productos
from Factura import factura
from Mostrar_factura import Facturas
from Compra import Facturas_C

def menu_principal():
    class Menu_inicio:
        def __init__(self, ventana):
            self.ventana = ventana
            self.ventana.title("Menu")
            self.titulo = Frame(self.ventana, height="200")
            self.titulo.config(bg="DodgerBlue4")
            self.titulo.pack(fill = X)
            self.titulo_menu = Button(self.titulo, text="COMERCIAL CORONADO", font=("Arial",30,"bold"), bg="DodgerBlue4", fg="snow").place(x=220, y=60)
            self.opciones = Frame(self.ventana, bg="AntiqueWhite1")
            self.opciones.pack(fill = BOTH, expand = True)
            # Botones de opciones
            self.productos = Button(self.opciones, text="INVENTARIO", font=("Arial",10,"bold"), bg="DodgerBlue4", fg="snow", width="23", height="5", command=productos).place(x=150, y=100)
            self.factura = Button(self.opciones, text="INGRESO DE FACTURA", font=("Arial",10,"bold"), bg="DodgerBlue4", fg="snow", width="23", height="5", command=factura).place(x=650, y=100)
            self.ventas = Button(self.opciones, text="REGISTRO DE VENTAS", font=("Arial",10,"bold"), bg="DodgerBlue4", fg="snow", width="23", height="5", command=Facturas).place(x=150, y=250)
            self.compras = Button(self.opciones, text="INGRESO DE COMPRAS", font=("Arial",10,"bold"), bg="DodgerBlue4", fg="snow", width="23", height="5", command=Facturas_C).place(x=650, y=250)
    ventana = Tk()
    ventana.geometry("1000x700")
    ventana.resizable(0,0)
    window = Menu_inicio(ventana)
    ventana.mainloop()
#menu_principal()