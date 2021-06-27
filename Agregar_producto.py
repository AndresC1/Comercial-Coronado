from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def agregar_producto():
    class Agregar:
        Base_Producto = 'Base_de_datos_Productos.db'
        def __init__(self, ventana):
            self.ventana = ventana
            self.titulo = Frame(self.ventana, height="70")
            self.titulo.config(bg="DodgerBlue4")
            self.titulo.pack(fill = X)
            self.encabezado = Label(self.titulo, text="Agregar Producto", font=("Arial",15,"bold"), bg="DodgerBlue4", fg="snow").place(x=170, y=20)
            self.formulario = Frame(self.ventana, height="550")
            self.formulario.config(bg="AntiqueWhite1")
            self.formulario.pack(fill = X)
            # Codigo
            Label(self.formulario, text="Codigo", font=("Arial",15,"bold"),bg="AntiqueWhite1").place(x=110, y=45)
            # Descripcion
            Label(self.formulario, text="Descripcion", font=("Arial",15,"bold"),bg="AntiqueWhite1").place(x=75, y=100)
            # Existencia
            Label(self.formulario, text="Existencia", font=("Arial",15,"bold"),bg="AntiqueWhite1").place(x=90, y=155)
            # Unidad de medida
            Label(self.formulario, text="Unidad de Medida", font=("Arial",15,"bold"),bg="AntiqueWhite1").place(x=20, y=210)
            # Precio Unitario
            Label(self.formulario, text="Precio Unitario", font=("Arial",15,"bold"),bg="AntiqueWhite1").place(x=50, y=265)
            # Caja Codigo
            self.caja_codigo = Entry(self.formulario, font="Helvetica 15", width="23")
            self.caja_codigo.place(x=210, y=45)
            self.caja_codigo.focus()
            # Caja Descripcion
            self.caja_Descripcion = Entry(self.formulario, font="Helvetica 15", width="23")
            self.caja_Descripcion.place(x=210, y=100)
            # Caja Existencia
            self.caja_Existencia = Entry(self.formulario, font="Helvetica 15", width="23")
            self.caja_Existencia.place(x=210, y=155)
            # Caja Unidad de medida
            self.caja_unidad_Medida = Entry(self.formulario, font="Helvetica 15", width="23")
            self.caja_unidad_Medida.place(x=210, y=210)
            # Caja Precio Unitario
            self.caja_Precio_U = Entry(self.formulario, font="Helvetica 15", width="23")
            self.caja_Precio_U.place(x=210, y=265)
            self.guardar = Button(self.formulario, text="Guardar",height="4", width="70", bg="DodgerBlue4", fg="snow", command=self.agregar_datos).place(x=0,y=329)
        def run_query(self, query, parametros = ()):
            with sqlite3.connect(self.Base_Producto) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, parametros)
                conn.commit()
            return result
        def validacion(self):
            return len(self.caja_codigo.get()) != 0 and len(self.caja_Descripcion.get()) != 0 and len(self.caja_Existencia.get()) != 0 and len(self.caja_Precio_U.get()) != 0 and len(self.caja_unidad_Medida.get()) != 0
        def agregar_datos(self):
            if self.validacion():
                query = 'INSERT INTO productos VALUES(?, ?, ?, ?, ?)'
                parametros = (self.caja_codigo.get(), self.caja_Descripcion.get(), self.caja_Existencia.get(), self.caja_Precio_U.get(), self.caja_unidad_Medida.get())
                self.run_query(query, parametros)
                self.caja_codigo.delete(0, END)
                self.caja_Descripcion.delete(0, END)
                self.caja_Existencia.delete(0, END)
                self.caja_Precio_U.delete(0, END)
                self.caja_unidad_Medida.delete(0, END)
                messagebox.showinfo("Comercial Coronado", "PRODUCTO GUARDADO")
                self.ventana.destroy()
            else:
                messagebox.showerror("Comercial Coronado", "TODOS LOS CAMPOS DEBEN ESTAR LLENOS")
    ventana = Tk()
    ventana.geometry("500x470")
    ventana.resizable(0,0)
    window = Agregar(ventana)
    ventana.mainloop()

