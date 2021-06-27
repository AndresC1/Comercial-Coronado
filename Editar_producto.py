from tkinter import *
from tkinter import ttk
import sqlite3

def editar():
    class Editar_P:
        Base_Producto = 'Base_de_datos_Productos.db'
        def __init__(self, ventana):
            self.ventana = ventana
            self.titulo = Frame(self.ventana, height="70")
            self.titulo.config(bg="DodgerBlue4")
            self.titulo.pack(fill = X)
            self.encabezado = Label(self.titulo, text="Editar Producto", font=("Arial",15,"bold"), bg="DodgerBlue4", fg="snow").place(x=300, y=20)
            self.panel = Frame(self.ventana, height="100")
            self.panel.config(bg="AntiqueWhite1")
            self.panel.pack(fill = X)
            # panel de busqueda
            self.encabezado = Label(self.panel, text="Buscar Producto", font=("Arial",10,"bold"), bg="AntiqueWhite1").place(x=320, y=0)
            self.Codigo = Label(self.panel, text="Codigo",bg="AntiqueWhite1").place(x=100,y=25)
            self.Descripcion = Label(self.panel, text="Descripcion",bg="AntiqueWhite1").place(x=100,y=55)
            self.caja_codigo = Entry(self.panel, font="Helvetica 12", width="23")
            self.caja_codigo.place(x=200,y=25)
            self.caja_codigo.focus()
            self.caja_descripcion = Entry(self.panel, font="Helvetica 12", width="23")
            self.caja_descripcion.place(x=200,y=55)
            self.buscar = Button(self.panel, text="Buscar",height="4", width="20", bg="DodgerBlue4", fg="snow", command=self.search_product).place(x=500,y=15)
            self.buscar = Button(self.panel, text="Buscar",height="1", width="2", bg="DodgerBlue4", fg="snow", command=self.edit_product).place(x=500,y=5)
            self.datos = Frame(self.ventana)
            self.datos.pack(fill = BOTH, expand = True)
            self.tabla = ttk.Treeview(self.datos,columns=("#1","#2","#3","#4"))
            self.tabla.column("#0", width=35)
            self.tabla.column("#4", width=70)
            self.tabla.column("#1", width=390)
            self.tabla.column("#2", width=50)
            self.tabla.column("#3", width=70)
            self.tabla.pack(fill = BOTH, expand = True)
            self.tabla.heading("#0", text="Codigo")
            self.tabla.heading("#4", text="Unidad de Medida")
            self.tabla.heading("#1", text="Descripcion")
            self.tabla.heading("#2", text="Existencia")
            self.tabla.heading("#3", text="Precio Unitario")
        def validacion(self):
            return len(self.caja_codigo.get()) != 0 and len(self.caja_descripcion.get()) != 0
        def run_query(self, query, parametros = ()):
            with sqlite3.connect(self.Base_Producto) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, parametros)
                conn.commit()
            return result
        def search_product(self):
            codigo = self.caja_codigo.get()
            des = self.caja_descripcion.get()
            record = self.tabla.get_children()
            for element in record:
                self.tabla.delete(element)
            query = 'SELECT * FROM Productos ORDER BY Codigo DESC'
            fila_inventario = self.run_query(query)
            for row in fila_inventario:
                if self.validacion():
                    if row[0] == codigo and row[1] == des: 
                        self.tabla.insert('',1,text=row[0],values=(row[1],row[2], row[3], row[4]))       
                else:
                    if row[0] == codigo: 
                        self.tabla.insert('',1,text=row[0],values=(row[1],row[2], row[3], row[4]))
                    else:
                        if row[1] == des: 
                            self.tabla.insert('',1,text=row[0],values=(row[1],row[2], row[3], row[4]))
        def edit_product(self):
            #Guardar datos viejos en variables
            cod = self.tabla.item(self.tabla.selection())["text"]
            des = self.tabla.item(self.tabla.selection())["values"][0]
            u_m = self.tabla.item(self.tabla.selection())["values"][3]
            pu = self.tabla.item(self.tabla.selection())["values"][2]
            ex = self.tabla.item(self.tabla.selection())["values"][1]
            #Frame
            self.edit = Frame(self.ventana, height="100")
            self.edit.config(bg="CadetBlue3")
            self.edit.pack(fill = X)
            #Label de datos
            self.encabezado = Label(self.edit, text="Edicion de datos", font=("Arial",10,"bold"), bg="CadetBlue3").place(x=320, y=0)
            self.Codigo_nuevo = Label(self.edit, text="Codigo",bg="CadetBlue3").place(x=40,y=25)
            self.unidad_nuevo = Label(self.edit, text="Unidad de medida",bg="CadetBlue3").place(x=40,y=60)
            self.descripcion_nuevo = Label(self.edit, text="Descripcion",bg="CadetBlue3").place(x=220,y=25)
            self.precio_nuevo = Label(self.edit, text="Precio Unitario",bg="CadetBlue3").place(x=310,y=60)
            self.cant_nuevo = Label(self.edit, text="Existencia",bg="CadetBlue3").place(x=560,y=25)
            #Salida de datos
            self.caja_codigo_nuevo = Entry(self.edit, textvariable = StringVar(self.edit, value = cod), state="readonly", font="Helvetica 12", width="12")
            self.caja_codigo_nuevo.place(x=100,y=25)
            self.caja_unidad_nuevo = Entry(self.edit, textvariable = StringVar(self.edit, value = u_m), font="Helvetica 12", width="15")
            self.caja_unidad_nuevo.place(x=160,y=60)
            self.caja_descripcion_nuevo = Entry(self.edit, textvariable = StringVar(self.edit, value = des), font="Helvetica 12", width="29")
            self.caja_descripcion_nuevo.place(x=290,y=25)
            self.caja_precio_nuevo = Entry(self.edit, textvariable = StringVar(self.edit, value = pu), font="Helvetica 12", width="14")
            self.caja_precio_nuevo.place(x=400,y=60)
            self.caja_cant_nuevo = Entry(self.edit, textvariable = StringVar(self.edit, value = ex), font="Helvetica 12", width="12")
            self.caja_cant_nuevo.place(x=620,y=25)
            #Boton de guardar
            self.guardar = Button(self.edit, text="Guardar",height="2", width="20", bg="DodgerBlue4", fg="snow").place(x=570,y=52)
    ventana = Tk()
    ventana.geometry("800x510")
    ventana.resizable(0,0)
    window = Editar_P(ventana)
    ventana.mainloop()