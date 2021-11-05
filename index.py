#Importaciones
from tkinter import ttk
from tkinter import *

import sqlite3

class programa:

    #Defino el nombre de la base de datos
    base_nombre='bd.db'

    def __init__(self,window):
        '''Objeto constructor'''
        
        self.wind = window
        self.wind.title("Programa CRUD")

        #Frames
        frame=LabelFrame(self.wind,text='Registro de empleados')
        frame.grid(row=0,column=0,columnspan=5,pady=30)

        Label(frame,text="Legajo: ").grid(row=2,column=0)
        self.legajo=Entry(frame)
        self.legajo.grid(row=2,column=1)

        Label(frame,text="Nombre y Apellido: ").grid(row=2,column=3)
        self.nombre=Entry(frame)
        self.nombre.grid(row=2,column=4)
        
        Label(frame,text="Puesto: ").grid(row=3,column=0)
        self.puesto=Entry(frame)
        self.puesto.grid(row=3,column=1)

        Label(frame,text="Sucursal: ").grid(row=3,column=3)
        self.sucursal=Entry(frame)
        self.sucursal.grid(row=3,column=4)

        #botones
        ttk.Button(frame,text="Registrar",command=self.registrar).grid(row=5,column=0)
        ttk.Button(frame,text="Mostrar").grid(row=5,column=2)
        ttk.Button(frame,text="Modificar").grid(row=5,column=4)
        ttk.Button(frame,text="Eliminar").grid(row=5,column=6)

        #Creacion de tablas
        self.tree=ttk.Treeview(height=10, columns=('#1','#2','#3'))
        self.tree.place(x=0, y=120)
        self.tree.heading('#0', text="Legajo", anchor=CENTER)
        self.tree.heading('#1', text="Nombre", anchor=CENTER)
        self.tree.heading('#2', text="Puesto", anchor=CENTER)
        self.tree.heading('#3', text="Sucursal", anchor=CENTER)

        self.get_empleados()

    def run_query(self,query,parameters=()):
        '''Esta funcion realiza una conexión y consulta con la BBDD'''
        with sqlite3.connect(self.base_nombre) as conn:
                cursor=conn.cursor()
                result=cursor.execute(query,parameters)
                conn.commit()
        return result

    def get_empleados(self):
        #consulta de datos
        query = 'SELECT * FROM empleados'
        db_rows=self.run_query(query)
        # Insertar la consulta dentro de la tabla
        for row in db_rows:
            self.tree.insert('', 0, text = (row[0]), values = (row[1],row[2], row[3]))
                
    def registrar(self):
        '''Esta funcion sirve para registrar a un nuevo empleado'''
        Legajo=self.legajo.get()
        Nombre=self.nombre.get()
        Puesto=self.puesto.get()
        Sucursal=self.sucursal.get()

	#Ejecuto la query	
        if(Legajo !=''and Nombre !='' and Puesto !='' and Sucursal !=''):
            queryInsert ='INSERT INTO empleados VALUES(?,?,?,?)'
            parameters=(self.legajo.get(),self.nombre.get(),self.puesto.get(),self.sucursal.get())
            execute = self.run_query(queryInsert,parameters)
            print("Empleado registrado")    
        else:
            print("Inserte datos")
        #Vuelvo a mostrar a los empleados
        self.get_empleados()

if __name__ == '__main__':
    window = Tk()
    Aplicacion = programa(window)
    window.mainloop()
        
