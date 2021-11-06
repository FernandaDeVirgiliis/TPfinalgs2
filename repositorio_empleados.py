class repositorio_empleados:
    
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
            messagebox.showinfo(message="Empleado registrado", title="Registrado")    
        else:
            messagebox.showwarning(message="Ingresar datos", title="Precaución")
        #Vuelvo a mostrar a los empleados
        self.get_empleados()

    #Funcion actualizar
    def actualizar(self):
        '''Esta función sirve para modificar un empleado existente'''
        try:
            self.tree.item(self.tree.selection())['text']
        except IndexError: 
            messagebox.showwarning(message="Selecciona un empleado", title="Aviso")
            return
        Legajoedit=self.tree.item(self.tree.selection())['text']
        
        

    #Funcion eliminar
    def eliminar(self):
        '''Ésta función sirve para eliminar a un empleado existente'''
        try:
            self.tree.item(self.tree.selection())['text']
        except IndexError: 
            messagebox.showwarning(message="Selecciona un empleado", title="Aviso")
            return
        nombredelete = self.tree.item(self.tree.selection())['text']
        querydelete='DELETE FROM empleados WHERE Legajo = ?'
        self.run_query(querydelete, (nombredelete, ))
        messagebox.showinfo(message="Empleado eliminado", title="Eliminar")
        
        self.get_empleados()
         







    #Filtro
    #Informe

if __name__ == '__main__':
    window = Tk()
    Aplicacion = programa(window)
    window.mainloop()
        
