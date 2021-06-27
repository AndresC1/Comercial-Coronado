from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import sqlite3

def factura():
    class Factura_Comercial:
        Base_Producto = 'Base_de_datos_Productos.db'
        def __init__(self,ventana):
            self.ventana = ventana
            # Encabezado
            self.datos_cliente = Frame(self.ventana, height="210")
            self.datos_cliente.config(bg="DodgerBlue4")
            self.datos_cliente.pack(fill = X)
            self.total_fact = 0
            self.dia = datetime.now()
            self.numero_factura()
            Label(self.datos_cliente, text="COMERCIAL CORONADO", font=("Arial",20,"bold"),bg="DodgerBlue4",fg="snow").place(x=300, y=20)
            Label(self.datos_cliente, text="FACTURA COMERCIAL", font=("Arial",18,"bold"),bg="DodgerBlue4",fg="snow").place(x=340, y=70)
            Label(self.datos_cliente, text="Nombre del cliente:", font=("Arial",12,"bold"),bg="DodgerBlue4",fg="snow").place(x=25, y=130)
            Label(self.datos_cliente, text="Factura N°:", font=("Arial",12,"bold"),bg="DodgerBlue4",fg="snow").place(x=530, y=130)
            Label(self.datos_cliente, text="Fecha:", font=("Arial",12,"bold"),bg="DodgerBlue4",fg="snow").place(x=30, y=170)
            Label(self.datos_cliente, text=f"{self.dia.day}/{self.dia.month}/{self.dia.year}", font=("Arial",12,"bold"),fg="snow",bg="DodgerBlue4").place(x=140, y=170)
            caja_nombre = Entry(self.datos_cliente, font="Helvetica 11", width="40")
            caja_nombre.place(x=185, y=130)
            self.caja_numero_fac = Entry(self.datos_cliente, textvariable = StringVar(self.datos_cliente, value = self.numero), state="readonly", font="Helvetica 11", width="15")
            self.caja_numero_fac.place(x=630, y=130)
            caja=Entry(self.datos_cliente)
            caja_01=Entry(self.datos_cliente)
            caja_nombre.focus()
            # Acciones
            self.menu_acciones = Frame(self.ventana, height="55")
            self.menu_acciones.config(bg="red")
            self.menu_acciones.pack(fill = X)
            self.boton_01 = Button(self.menu_acciones, text="Agregar Producto",height="3", width="70", bg="CadetBlue3",command=self.agregar).place(x=0,y=0)
            self.boton_02 = Button(self.menu_acciones, text="Eliminar Producto",height="3", width="70", bg="CadetBlue3", command=self.delete_product).place(x=500,y=0)
            # Tabla
            self.datos = Frame(self.ventana)
            self.datos.pack(fill = X)
            self.tabla = ttk.Treeview(self.datos,columns=("#1","#2","#3"))
            self.tabla.column("#0", width=35)
            self.tabla.column("#1", width=390)
            self.tabla.column("#2", width=50)
            self.tabla.column("#3", width=50)
            self.tabla.pack(fill = BOTH, expand = True)
            self.tabla.heading("#0", text="Cantidad")
            self.tabla.heading("#1", text="Descripcion")
            self.tabla.heading("#2", text="Precio Unitario")
            self.tabla.heading("#3", text="Total")
            # Total
            self.total = Frame(self.ventana, height="100", bg="DodgerBlue4")
            self.total.pack(fill = X)
            # Total Valores
            self.etiqueta = Label(self.total)
            self.etiqueta.place(x=800,y=38)
            self.etiqueta.config(bg="DodgerBlue4", fg="snow")
            self.etiqueta.pack()
            #Guardar Factura
            self.save = Frame(self.ventana)
            self.save.pack(fill = X)
            self.boton_confirm = Button(self.save, text="REGISTRAR FACTURA", height="100", bg="CadetBlue3", command=self.terminar)
            self.boton_confirm.pack(fill = X)
        def mensaje_delete_t(self):
            messagebox.showinfo("Comercial Coronado", "EL PRODUCTO A SIDO ELIMINADO")
        def mensaje_f(self):
            messagebox.showinfo("Comercial Coronado", "DEBE SELECCIONAR UN PRODUCTO")
        def mensaje_edit_t(self):
            messagebox.showinfo("Comercial Coronado", "EL PRODUCTO A SIDO EDITADO")
        def agregar(self):
            self.ventana.iconify()
            #ventana emergente
            self.win_add = Toplevel()
            self.win_add.geometry("290x171")
            self.win_add.resizable(0,0)
            #Ingreso de datos
            Label(self.win_add, text="Codigo", font=("Arial",15,"bold"),bg="AntiqueWhite1").place(x=0, y=0)
            self.caja_producto = Entry(self.win_add, font="Helvetica 15", width="15")
            self.caja_producto.place(x=100, y=0)
            self.caja_producto.focus()
            Label(self.win_add, text="Cantidad", font=("Arial",15,"bold"),bg="AntiqueWhite1").place(x=0, y=50)
            self.caja_cantidad = Entry(self.win_add, font="Helvetica 15", width="15")
            self.caja_cantidad.place(x=100, y=50)
            #Boton de guardar
            guardar = Button(self.win_add, text="Guardar",height="4", width="40", bg="DodgerBlue4", fg="snow", command=self.agregar_factura).place(x=0,y=100)
            #muestra de ventana
            self.win_add.mainloop()
        def search_product(self):
            q=0
            if self.validacion():
                self.codigo_producto = self.caja_producto.get()
                self.cant_producto = float(self.caja_cantidad.get())
                query = 'SELECT * FROM Productos ORDER BY Codigo DESC'
                fila_inventario = self.run_query(query)
                for row in fila_inventario:
                    if row[0] == self.codigo_producto:
                        if (row[2]-self.cant_producto) >= 0:
                            self.producto_fact = row[3]*self.cant_producto
                            self.tabla.insert('',int(self.cant_producto), text=int(self.cant_producto), values=(row[1], row[3], self.producto_fact))
                            self.descripcion_producto = row[1]
                            self.precio_producto = row[3]
                            self.total_fact = self.total_fact + self.producto_fact
                            self.total_view()
                            self.win_add.destroy()
                            q=1
                            return q
                        else:
                            messagebox.showinfo("COMERCIAL CORONADO", "NO POSEE LA SUFICIENTE EXISTENCIA DE ESTE PRODUCTO")
                            q=1
                            return 0
                if q == 0:
                    messagebox.showinfo("COMERCIAL CORONADO", "El producto no fue encontrado")
                    return q
            else:
                    messagebox.showinfo("COMERCIAL CORONADO", "DEBE DE LLENAR TODOS LOS CAMPOS")
                    return q
        def validacion(self):
            return len(self.caja_producto.get()) != 0 and len(self.caja_cantidad.get()) != 0
        def run_query(self, query, parametros = ()):
            with sqlite3.connect(self.Base_Producto) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, parametros)
                conn.commit()
            return result
        def total_view(self):
            self.etiqueta["text"] = f"TOTAL:\tC${self.total_fact}"
        def agregar_factura(self):
            v = self.search_product()
            if v == 1:
                self.fecha = f"{self.dia.day}/{self.dia.month}/{self.dia.year}"
                self.mes = self.validacion_mes()
                query = 'INSERT INTO Factura VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
                num_fac = self.numero
                fecha_fac = self.fecha
                mes_fac = self.mes
                cod_fac = self.codigo_producto
                des_fac = self.descripcion_producto
                cant_fac = int(self.cant_producto)
                precio_fact = self.precio_producto
                pro_fact = self.producto_fact
                parametros = (num_fac, fecha_fac, mes_fac, cod_fac, des_fac, cant_fac, precio_fact, pro_fact)
                self.run_query(query, parametros)
                self.update_existencia()
                self.ventana.deiconify()
        def validacion_mes(self):
            meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
            n_meses = (1,2,3,4,5,6,7,8,9,10,11,12)
            for i in range(12):
                if n_meses[i] == self.dia.month:
                    return meses[i]
        def numero_factura(self):
            query = 'SELECT * FROM Factura ORDER BY Numero_Fac ASC'
            fila_inventario = self.run_query(query)
            for row in fila_inventario:
                self.numero = row[0]+1
        def update_existencia(self):
            query = 'SELECT * FROM Productos ORDER BY Codigo DESC'
            fila_inventario = self.run_query(query)
            for row in fila_inventario:
                if row[0] == self.codigo_producto:
                    self.c_n = row[0]
                    self.d_n = row[1]
                    self.e_n = row[2]-int(self.cant_producto)
                    self.e_o = row[2]
                    self.p_n = row[3]
                    self.u_n = row[4]
            self.val()
        def update_Delete_products(self):
            query = 'SELECT * FROM Productos ORDER BY Codigo DESC'
            fila_inventario = self.run_query(query)
            for row in fila_inventario:
                if row[1] == self.tabla.item(self.tabla.selection())["values"][0]:
                    self.c_n = row[0]
                    self.d_n = row[1]
                    self.e_n = row[2]+int(self.tabla.item(self.tabla.selection())["text"])
                    self.e_o = row[2]
                    self.p_n = row[3]
                    self.u_n = row[4]
            self.val()
        def val(self):
            query_1 = 'UPDATE Productos SET Codigo = ?, Descripcion = ?, Existencia = ?, Precio = ?, Medida = ?'\
                        'WHERE Codigo = ? AND Descripcion = ? AND Existencia = ? AND Precio = ? AND Medida = ?'
            parametros = (self.c_n, self.d_n, self.e_n, self.p_n, self.u_n, self.c_n, self.d_n, self.e_o, self.p_n, self.u_n)
            self.run_query(query_1, parametros)
        def delete_product(self):
            try:
                self.tabla.item(self.tabla.selection())["values"][0]
            except IndexError as e:
                self.mensaje_f()
                return
            c = self.tabla.item(self.tabla.selection())["values"][0]
            f = self.numero
            ca = self.tabla.item(self.tabla.selection())["values"][2]
            self.total_fact = self.total_fact - float(ca)
            self.total_view()
            query = 'DELETE FROM Factura WHERE Descripcion = ? AND Numero_Fac = ? AND Total = ?'
            self.run_query(query, (c, f, ca))
            self.update_Delete_products()
            self.tabla.delete(self.tabla.selection())
            self.mensaje_delete_t()
        def terminar(self):
            self.ventana.destroy()
    ventana = Tk()
    ventana.geometry("1000x600")
    ventana.resizable(0,0)
    window = Factura_Comercial(ventana)
    ventana.mainloop()