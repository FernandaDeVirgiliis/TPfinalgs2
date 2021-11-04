from tkinter import ttk
from tkinter import *

import sqlite3

class programa:

    def __init__(self,window):
        
        self.wind = window
        self.wind.title("Programa CRUD")

        #Frame
        frame=LabelFrame(self.wind,text='Registro de empleados')
        frame.grid(row=0,column=0,columnspan=3,pady=20)

        Label(frame,text="Legajo: ").grid(row=1,column=0)
        self.legajo=Entry(frame)
        self.legajo.grid(row=1,column=1)

        Label(frame,text="Nombre y Apellido: ").grid(row=1,column=0)
        self.nombre=Entry(frame)
        self.nombre.grid(row=1,column=3)
        
        Label(frame,text="Puesto: ").grid(row=1,column=0)
        self.puesto=Entry(frame)
        self.puesto.grid(row=2,column=2)

        Label(frame,text="Sucursal: ").grid(row=1,column=0)
        self.sucursal=Entry(frame)
        self.sucursal.grid(row=2,column=4)

        #botones
        
        ttk.Button(frame,text="Registrar").grid(row=4,column=0)
        ttk.Button(frame,text="Mostrar").grid(row=4,column=2)
        ttk.Button(frame,text="Modificar").grid(row=4,column=4)
        ttk.Button(frame,text="Eliminar").grid(row=4,column=6)

        #Creacion de tablas

        self.tree=ttk.Treeview(height=10, columns=('#1','#2','#3'))
        self.tree.place(x=0, y=130)
        self.tree.heading('#0', text="Legajo", anchor=CENTER)
        self.tree.heading('#1', text="Nombre", anchor=CENTER)
        self.tree.heading('#2', text="Puesto", anchor=CENTER)
        self.tree.heading('#3', text="Sucursal", anchor=CENTER)
        



if __name__ == '__main__':
    window = Tk()
    Aplicacion = programa(window)
    window.mainloop()
        
