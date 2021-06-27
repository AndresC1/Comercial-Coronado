from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Factura_compra import factura
import sqlite3

def Facturas_C():
    class Registro:
        Base_Producto = 'Base_de_datos_Productos.db'
        def __init__(self, ventana):
            self.ventana = ventana
            self.titulo = Frame(self.ventana, height="150")
            self.titulo.config(bg="DodgerBlue4")
            self.titulo.pack(fill = X)
            self.encabezado = Button(self.titulo, text="COMPRAS", font=("Arial",20,"bold"), bg="DodgerBlue4", fg="snow").place(x=450, y=50)
            self.opciones = Frame(self.ventana, height="98")
            self.opciones.config(bg="AntiqueWhite1")
            self.opciones.pack(fill = X)
            self.boton_01 = Button(self.opciones, text="Agregar",height="2", width="51", bg="CadetBlue3", command=factura).place(x=0,y=0)
            self.boton_02 = Button(self.opciones, text="Buscar",height="2", width="51", bg="CadetBlue3").place(x=368,y=0)
            self.boton_03 = Button(self.opciones, text="Eliminar",height="2", width="51", bg="CadetBlue3", command=self.delete_compra).place(x=736,y=0)
            self.boton_05 = Button(self.opciones, text="Actualizar",height="3", width="156", bg="CadetBlue3", command=self.get_product).place(x=0,y=42)
            self.datos = Frame(self.ventana)
            self.datos.pack(fill = BOTH, expand = True)
            self.tabla = ttk.Treeview(self.datos,columns=("#1","#2","#3","#4","#5","#6","#7"))
            self.tabla.column("#0", width=5)
            self.tabla.column("#1", width=120)
            self.tabla.column("#2", width=10)
            self.tabla.column("#3", width=5)
            self.tabla.column("#4", width=5)
            self.tabla.column("#5", width=330)
            self.tabla.column("#6", width=30)
            self.tabla.column("#7", width=30)
            self.tabla.pack(fill = BOTH, expand = True)
            self.tabla.heading("#0", text=" N° Fact")
            self.tabla.heading("#1", text="Proveedor")
            self.tabla.heading("#2", text="Fecha")
            self.tabla.heading("#3", text="Codigo")
            self.tabla.heading("#4", text="Cantidad")
            self.tabla.heading("#5", text="Descripcion")
            self.tabla.heading("#6", text="Precio")
            self.tabla.heading("#7", text="Total")
            self.get_product()
        def run_query(self, query, parametros = ()):
            with sqlite3.connect(self.Base_Producto) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, parametros)
                conn.commit()
            return result
        def get_product(self):
            record = self.tabla.get_children()
            for element in record:
                self.tabla.delete(element)
            query = 'SELECT * FROM Compras ORDER BY Factura ASC'
            fila_inventario = self.run_query(query)
            for row in fila_inventario:
                self.tabla.insert('',1,text=row[0],values=(row[1],row[2], row[3], row[4], row[5], row[6], row[7]))
        def delete_compra(self):
            try:
                self.tabla.item(self.tabla.selection())["values"][0]
            except IndexError as e:
                self.mensaje_f()
                return
            n = self.tabla.item(self.tabla.selection())["text"]
            p = self.tabla.item(self.tabla.selection())["values"][0]
            f = self.tabla.item(self.tabla.selection())["values"][1]
            c = self.tabla.item(self.tabla.selection())["values"][2]
            can = self.tabla.item(self.tabla.selection())["values"][3]
            query = 'DELETE FROM Compras WHERE Factura = ? AND Proveedor = ? AND Fecha = ? AND Codigo = ? AND Cantidad = ?'
            self.run_query(query, (n,p,f,c,can, ))
            self.mensaje_delete_t()
        def mensaje_delete_t(self):
            messagebox.showinfo("Comercial Coronado", "LA FACTURA A SIDO ELIMINADO")
        def mensaje_f(self):
            messagebox.showinfo("Comercial Coronado", "DEBE SELECCIONAR UNA FACTURA")
    ventana = Tk()
    ventana.geometry("1100x700")
    ventana.resizable(0,0)
    window = Registro(ventana)
    ventana.mainloop()
# Facturas_C()