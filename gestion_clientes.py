import conectormysql  #módulo para obtener el conector y cursor de MySQL para poder hacer modificaciones en la base de datos skyroute

def gestionar_clientes():

    while True:
        print("Gestionar clientes")
        print("1. Agregar nuevo cliente")
        print("2. Ver clientes")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Atrás")
        opcion= input("Ingrese opción:")
        print(f"Seleccionó opción: {opcion}")
        conector, cursor = conectormysql.conectarDB() 
        #conector y cursor son los return de la funcion conectarDB definida en el modulo conectormysql.py
        #conector es la conexion a la base de datos y cursor es el cursor para ejecutar consultas SQL
        if opcion=="1": #agregar cliente
            print("Agregar nuevo cliente")
            print("Ingrese los datos del cliente")
            # Ingreso de datos
            cuit = input("Cuit: ")
            razon_social = input("Razon Social: ")
            mail = input("ingresar mail: ")
            
            try:
                # Consulta SQL para insertar
                query = """
                    INSERT INTO clientes (cuit, razon_social , mail)
                    VALUES (%s, %s, %s)
                """
                # %s es un marcador de posición para los valores que se van a insertar
                # Los valores se pasan como una tupla al ejecutar la consulta
                cursor.execute(query, (cuit, razon_social, mail)) # Ejecutar consulta con los valores ingresados
                conector.commit()# Commit para guardar los cambios en la base de datos
                print(f"Ha agregado al cliente {razon_social} Cuit: {cuit}")
            except Exception as e:
                print("Error al agregar cliente:", e)
        # Si ocurre un error, se captura la excepción y se imprime un mensaje de error
        #Acá pueden ocurrir varios tipos de errores al ingresar datos por teclado, como por ejemplo:
        # - Error de duplicado de clave primaria (si el cuit ya existe) 
        # - Error de tipo de dato (si se ingresa letras en lugar de números en el cuit)
        elif opcion=="2": #ver clientes
            print("Lista de Clientes de skyroute")
            print("================================")
            cursor.execute("SELECT * FROM clientes")#consulta SQL para seleccionar todos los clientes
            clientes = cursor.fetchall()   #fetchall crea una lista de clientes (lista de tuplas)

            if clientes:
                for x in clientes:
                    print(x)
                    print("=========")
            else:
                print("No hay clientes registrados")

        elif opcion=="3": #modifcar
            print("Modificar cliente")
            cuit = input("Ingrese el cuit del cliente que desea modificar: ")
            cursor.execute("SELECT * FROM clientes WHERE cuit = %s", (cuit,)) #Consulta SQL para seleccionar el cliente por cuit
            # %s es un marcador de posición para el valor del cuit
            cliente = cursor.fetchone()    #crea una tupla con los datos del cliente.

            if cliente:
                print("Datos actuales del cliente:",cliente)   #imprimo tupla cliente
                razon_social=input("Ingrese la nueva razón social: ")
                mail=input("Ingrese el nuevo mail:") #el cuit no se modifica, ya que es la clave primaria

                cursor.execute("""
                UPDATE clientes
                SET razon_social =%s, mail =%s 
                WHERE cuit = %s""", (razon_social ,mail,cuit))
                conector.commit() # Commit para guardar los cambios en la base de datos
                print("cliente modificado")
            else:
                print("No se encontro cliente con ese cuit")

        elif opcion=="4": #eliminar cliente
            cuit=input("ingresar cuit del cliente que quiera eliminar:") 
            cursor.execute("SELECT * FROM clientes WHERE cuit = %s", (cuit,))
            cliente = cursor.fetchone() #fetchone crea una tupla con los datos del cliente

            if cliente:
                print("¿Está seguro que desea eliminar el cliente:", cliente, "?")
                print("Esta acción no se puede deshacer ⚠️")
                respuesta = input("Ingrese 'si' para confirmar o 'no' para cancelar: ")
                if respuesta.lower() == 'si':
                    sql = "DELETE FROM clientes WHERE cuit = %s "
                    cursor.execute(sql,(cuit,)) 
                    conector.commit()
                    print(f"elimino el cliente cuit: {cuit}")
                else:
                    print("Eliminación cancelada.")
            else:
                print("No se encontro cliente con ese cuit")

        elif opcion=="5":
            break
        else:
            print("Opción no valida.")
        print("================================")
    cursor.close()
    conector.close()

# gestionar_clientes()
