#Importaciones
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from empleado import Empleados
from repositorio_empleados import RepositorioEmpleados
import sqlite3

class programa:
    #Defino el nombre de la base de datos
    base_nombre='bd.db'

    def __init__(self,window):
        '''Objeto constructor'''
        self.wind = window
        self.wind.geometry("850x300")
        self.wind.title("Programa CRUD")
        self.repositorio = RepositorioEmpleados()
      

        #Menu
        menubar=Menu(self.wind)
        menubasedat=Menu(menubar, tearoff=0)
        ayudamenu=Menu(menubar, tearoff=0)
        ayudamenu.add_command(label="Limpiar campos", command='')

        menubar.add_cascade(label="Ayuda", menu=ayudamenu)

        buscar=Menu(menubar, tearoff=0)
        buscar.add_command(label="Buscar por nombre", command='')

        menubar.add_cascade(label="Filtrar", menu=buscar)

        self.wind.config(menu=menubar)
        
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
        self.puesto=ttk.Combobox(frame,width=17)
        self.puesto.grid(row=3,column=1)
        opciones=["Operativo","Administrativo","Gerencial"]
        self.puesto['values']=opciones
        
    
        Label(frame,text="Sucursal: ").grid(row=3,column=3)
        self.sucursal=Entry(frame)
        self.sucursal.grid(row=3,column=4)

        
        #botones
        ttk.Button(frame,text="Registrar",command=self.agregar_empleado).grid(row=5,column=0)
        ttk.Button(frame,text="Modificar",command=self.ventana_editar_empleado).grid(row=5,column=3)
        ttk.Button(frame,text="Eliminar",command=self.eliminar_empleado).grid(row=5,column=6)
        

        #Creacion de tablas
        self.tree=ttk.Treeview(height=10, columns=('#1','#2','#3'))
        self.tree.place(x=0, y=250)
        self.tree.heading('#0', text="Legajo", anchor=CENTER)
        self.tree.heading('#1', text="Nombre", anchor=CENTER)
        self.tree.heading('#2', text="Puesto", anchor=CENTER)
        self.tree.heading('#3', text="Sucursal", anchor=CENTER)

        self.get_empleados()

    def get_seleccion(self):
        # Limpio la tabla antes de arrancar la query
        print (self.opcion.get())

    def run_query(self,query,parameters=()):
        '''Esta funcion realiza una conexión y consulta con la BBDD'''
        with sqlite3.connect(self.base_nombre) as conn:
                cursor=conn.cursor()
                result=cursor.execute(query,parameters)
                conn.commit()
        return result

    def get_empleados(self):
        # Limpio la tabla antes de arrancar la query
        elementos = self.tree.get_children()
        for element in elementos:
            self.tree.delete(element)
        
        #consulta de datos
        query = 'SELECT * FROM empleados'
        db_rows=self.run_query(query)
        # Insertar la consulta dentro de la tabla
        for row in db_rows:
            self.tree.insert('', 0, text = (row[0]), values = (row[1],row[2], row[3]))

    def agregar_empleado(self):
        '''Esta funcion sirve para registrar a un nuevo empleado'''
        parametros = Empleados(self.legajo.get(),self.nombre.get(),self.puesto.get(),self.sucursal.get())
        print (parametros)
        parametrito = self.repositorio.registrar(parametros)
        print (parametrito)
        if parametrito:
            messagebox.showinfo(message="Empleado registrado", title="Registrado")
        else:
            messagebox.showwarning(message="Error en la base de datos", title="Precaución")

        self.get_empleados()
        return parametros

    def ventana_editar_empleado(self):
        '''Ventana para editar un empleado'''
        try:
            self.tree.item(self.tree.selection())['text']
        except IndexError:
            # cambiar por ventana de error(show warning) -> self.message['text'] = 'Por favor, seleccione un registro'
            return
        legajo = self.tree.item(self.tree.selection())['text']
        nombre_anterior = self.tree.item(self.tree.selection())['values'][0]
        puesto_anterior = self.tree.item(self.tree.selection())['values'][1]
        sucursal_anterior = self.tree.item(self.tree.selection())['values'][2]
        self.ventana_edicion = Toplevel()
        self.ventana_edicion.title = 'Editar cliente'

        # Legajo
        Label(self.ventana_edicion, text = 'Legajo: ').grid(row = 0, column = 0)
        Entry(self.ventana_edicion, textvariable = StringVar(self.ventana_edicion, value = legajo), state = 'readonly').grid(row = 0, column = 1)

        # Nombre anterior
        Label(self.ventana_edicion, text = 'Nombre anterior: ').grid(row = 2, column = 0)
        Entry(self.ventana_edicion, textvariable = StringVar(self.ventana_edicion, value = nombre_anterior), state = 'readonly').grid(row = 2, column = 1)

        # Nombre actual
        Label(self.ventana_edicion, text = 'Nombre actual: ').grid(row = 3, column = 0)
        nuevo_nombre = Entry(self.ventana_edicion)
        nuevo_nombre.grid(row = 3, column = 1)

        # Puesto anterior
        Label(self.ventana_edicion, text = 'Puesto anterior: ').grid(row = 4, column = 0)
        Entry(self.ventana_edicion, textvariable = StringVar(self.ventana_edicion, value = puesto_anterior), state = 'readonly').grid(row = 4, column = 1)

        # Puesto nuevo
        Label(self.ventana_edicion, text = 'Puesto actual: ').grid(row = 5, column = 0)
        nuevo_puesto = Entry(self.ventana_edicion)
        nuevo_puesto.grid(row = 5, column = 1)

        # Sucursal anterior
        Label(self.ventana_edicion, text = 'Sucursal anterior: ').grid(row = 6, column = 0)
        Entry(self.ventana_edicion, textvariable = StringVar(self.ventana_edicion, value = sucursal_anterior), state = 'readonly').grid(row = 6, column = 1)

        # Sucursal actual
        Label(self.ventana_edicion, text = 'Sucursal actual: ').grid(row = 7, column = 0)
        nueva_sucursal = Entry(self.ventana_edicion)
        nueva_sucursal.grid(row = 7, column = 1)

        # Botón de guardar cambios
        ttk.Button(self.ventana_edicion,text ='Actualizar',command=lambda:self.editar_empleado(legajo,nuevo_nombre.get(),nuevo_puesto.get(),nueva_sucursal.get())).grid(row=8,column=0)

    #Funcion editar
    def editar_empleado(self,legajo,nuevo_nombre,nuevo_puesto,nueva_sucursal):
        '''Esta funcion sirve para editar a un empleado'''
        parametros = Empleados(legajo,nuevo_nombre,nuevo_puesto,nueva_sucursal)
        print (parametros)
        parametrito = self.repositorio.actualizar(parametros)
        print (parametrito)
        if parametrito:
            messagebox.showinfo(message="Empleado registrado", title="Registrado")
        else:
            messagebox.showwarning(message="Error en la base de datos", title="Precaución")

        self.get_empleados()
        return parametros
    

    #Funcion eliminar
    def eliminar_empleado(self):
        '''Ésta función sirve para eliminar a un empleado existente'''
        legajo = self.tree.item(self.tree.selection())['text']
        nombre = self.tree.item(self.tree.selection())['values'][0]
        puesto = self.tree.item(self.tree.selection())['values'][1]
        sucursal = self.tree.item(self.tree.selection())['values'][2]
        try:
            self.tree.item(self.tree.selection())['text']
        except IndexError: 
            messagebox.showwarning(message="Selecciona un empleado", title="Aviso")
            return
        parametro = Empleados(legajo,nombre,puesto,sucursal)
        self.repositorio.eliminar(parametro)
        messagebox.showinfo(message="Empleado eliminado", title="Eliminar")
        self.get_empleados()


                
    
if __name__ == '__main__':
    window= Tk()
    Aplicacion = programa(window)
    window.mainloop()
        
