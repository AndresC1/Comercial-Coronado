from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def fact_compra():
    class Buscar_fact:
        Base_Producto = 'Base_de_datos_Productos.db'
        def __init__(self, ventana):
            self.ventana = ventana
            # Proveedores
            self.proveedores()
            #Frame de titulo
            self.titulo = Frame(self.ventana, height="70")
            self.titulo.config(bg="DodgerBlue4")
            self.titulo.pack(fill = X)
            self.encabezado = Label(self.titulo, text="Buscar Factura De Compras", font=("Arial",15,"bold"), bg="DodgerBlue4", fg="snow").place(x=300, y=20)
            #Frame de Entry
            self.panel = Frame(self.ventana, height="180")
            self.panel.config(bg="AntiqueWhite1")
            self.panel.pack(fill = X)
            #Fecha
            Label(self.panel, text="Fecha:",bg="AntiqueWhite1").place(x=180,y=20)
            Label(self.panel, text="/",bg="AntiqueWhite1", font="15").place(x=240,y=17)
            Label(self.panel, text="/",bg="AntiqueWhite1", font="15").place(x=273,y=17)
            self.caja_dia = Entry(self.panel, font="Helvetica 9", width="2")
            self.caja_dia.place(x=220,y=20)
            self.caja_dia.focus()
            self.caja_mes_01 = Entry(self.panel, font="Helvetica 9", width="2")
            self.caja_mes_01.place(x=255,y=20)
            self.caja_a = Entry(self.panel, font="Helvetica 9", width="4")
            self.caja_a.place(x=286,y=20)
            #Mes
            Label(self.panel, text="Proveedor",bg="AntiqueWhite1").place(x=190,y=50)
            self.var=StringVar(self.panel)
            self.var.set("Mes")
            opciones=[]
            for i in range(len(self.pro_co)):
                opciones.append(self.pro_co[i])
            opcion=OptionMenu(self.panel,self.var,*opciones)
            opcion.config(width=15, bg="AntiqueWhite1")
            opcion.place(x=220, y=46)
            #Producto
            Label(self.panel, text="Producto",bg="AntiqueWhite1").place(x=160,y=80)
            self.caja_producto = Entry(self.panel, font="Helvetica 9", width="20")
            self.caja_producto.place(x=220,y=80)
            #Numero Factura
            Label(self.panel, text="Numero de Factura",bg="AntiqueWhite1").place(x=110,y=110)
            self.num_fact = Entry(self.panel, font="Helvetica 9", width="12")
            self.num_fact.place(x=220,y=110)
            #Codigo del producto
            Label(self.panel, text="Codigo",bg="AntiqueWhite1").place(x=170,y=140)
            self.cod_fact = Entry(self.panel, font="Helvetica 9", width="12")
            self.cod_fact.place(x=220,y=140)
            #Boton Guardar
            self.guardar = Button(self.panel, text="Buscar",height="4", width="20", bg="DodgerBlue4", fg="snow", command=self.verificaciones).place(x=500,y=35)
            #Frame de total
            self.opciones = Frame(self.ventana, height="40")
            self.opciones.pack(fill = X)
            #Tabla
            self.datos = Frame(self.ventana)
            self.datos.pack(fill = BOTH, expand = True)
            self.tabla = ttk.Treeview(self.datos,columns=("#1","#2","#3","#4","#5","#6","#7"))
            self.tabla.column("#0", width=5)
            self.tabla.column("#1", width=20)
            self.tabla.column("#2", width=20)
            self.tabla.column("#3", width=20)
            self.tabla.column("#4", width=200)
            self.tabla.column("#5", width=20)
            self.tabla.column("#6", width=20)
            self.tabla.column("#7", width=35)
            self.tabla.pack(fill = BOTH, expand = True)
            self.tabla.heading("#0", text=" N° ")
            self.tabla.heading("#1", text="Fecha")
            self.tabla.heading("#2", text="Mes")
            self.tabla.heading("#3", text="Codigo")
            self.tabla.heading("#4", text="Descripcion")
            self.tabla.heading("#5", text="Cantidad")
            self.tabla.heading("#6", text="Precio")
            self.tabla.heading("#7", text="Total")
        def run_query(self, query, parametros = ()):
            with sqlite3.connect(self.Base_Producto) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, parametros)
                conn.commit()
            return result
        def validacion_fecha(self):
            self.fecha = f"{self.caja_dia.get()}/{self.caja_mes_01.get()}/{self.caja_a.get()}"
            return len(self.caja_dia.get()) != 0 and len(self.caja_mes_01.get()) != 0 and len(self.caja_a.get()) != 0
        def validacion_mes(self):
            return self.var.get() != "Mes"
        def validacion_desc(self):
            return len(self.caja_producto.get()) != 0
        def validacion_num(self):
            return len(self.num_fact.get()) != 0
        def validacion_cod(self):
            return len(self.cod_fact.get()) != 0
        def verificaciones(self):
            q=0
            self.per=0
            self.vt=0
            self.datos = list()
            self.acciones = list()
            if self.validacion_fecha():
                self.datos.append(self.fecha)
                self.acciones.append(1)
                q=1
            if self.validacion_mes():
                self.datos.append(self.var.get())
                self.acciones.append(2)
                q=1
            if self.validacion_desc():
                self.datos.append(self.caja_producto.get())
                self.acciones.append(4)
                q=1
            if self.validacion_num():
                self.datos.append(int(self.num_fact.get()))
                self.acciones.append(0)
                q=1
            if self.validacion_cod():
                self.datos.append(self.cod_fact.get())
                self.acciones.append(3)
                q=1
            record = self.tabla.get_children()
            for element in record:
                self.tabla.delete(element)
            query = 'SELECT * FROM Factura ORDER BY Codigo DESC'
            fila_inventario = self.run_query(query)
            for row in fila_inventario:
                if len(self.datos) == 1:
                    if row[self.acciones[0]] == self.datos[0]:
                        self.tabla.insert("", row[0], text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                        self.tot(row[7],1)
                else:
                    if len(self.datos) == 2:
                        if row[self.acciones[0]] == self.datos[0] and row[self.acciones[1]] == self.datos[1]:
                            self.tabla.insert("", row[0], text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                            self.tot(row[7],1)
                    else:
                        if len(self.datos) == 3:
                            if row[self.acciones[0]] == self.datos[0] and row[self.acciones[1]] == self.datos[1] and row[self.acciones[2]] == self.datos[2]:
                                self.tabla.insert("", row[0], text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                                self.tot(row[7],1)
                        else:
                            if len(self.datos) == 4:
                                if row[self.acciones[0]] == self.datos[0] and row[self.acciones[1]] == self.datos[1] and row[self.acciones[2]] == self.datos[2] and row[self.acciones[3]] == self.datos[3]:
                                    self.tabla.insert("", row[0], text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                                    self.tot(row[7],1)
                            else:
                                if len(self.datos) == 5:
                                    if row[self.acciones[0]] == self.datos[0] and row[self.acciones[1]] == self.datos[1] and row[self.acciones[2]] == self.datos[2] and row[self.acciones[3]] == self.datos[3] and row[self.acciones[4]] == self.datos[4]:
                                        self.tabla.insert("", row[0], text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                                        self.tot(row[7],1)
            if q==0:
                messagebox.showerror("COMERCIAL CORONADO", "DEBE DE LLENAR ALGUNO DE LOS CAMPOS")
            else:
                Label(self.opciones, text=f"Total:\t\t{self.per}").place(x=400, y=20)
                Label(self.opciones, text=f"Ventas Totales:\t\t{self.vt}").place(x=40, y=20)
        def tot(self, v, vv):
            self.per = v + self.per
            self.vt = vv + self.vt
        def proveedores(self):
            self.pro_co = list()
            pop_b=list()
            query = 'SELECT * FROM Compras ORDER BY Codigo DESC'
            fila_inventario = self.run_query(query)
            for row in fila_inventario:
                self.pro_co.append(row[1])
            print(self.pro_co)
            for i in range(len(self.pro_co)):
                for j in range(i+1,len(self.pro_co)):
                    if self.pro_co[i] == self.pro_co[j]:
                        for x in range(len(pop_b)):
                            if pop_b[x] != j:
                                pop_b.append(j)
            print(pop_b)
    ventana = Tk()
    ventana.geometry("800x560")
    ventana.resizable(0,0)
    window = Buscar_fact(ventana)
    ventana.mainloop()
fact_compra()