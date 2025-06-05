import conectormysql

def gestionar_clientes():

    while True:
        print("Gestionar clientes")
        print("1. Agregar nuevo cliente")
        print("2. Modificar cliente")
        print("3. Eliminar cliente")
        print("4. Ver clientes")
        print("5. Atrás")
        opcion= input("Ingrese opción:")
        print(f"Seleccionó opción: {opcion}")
        conn, cursor = conectormysql.conectarDB()

        if opcion=="1": #agregar cliente
            print("Agregar nuevo cliente")
            print("Ingrese los datos del cliente")
            # Ingreso de datos
            cuit = input("Cuit: ")
            razon_social = input("Razon Social: ")
            mail = input("ingresar mail: ")

            # Consulta SQL para insertar
            query = """
                INSERT INTO clientes (cuit, razon_social , mail)
                VALUES (%s, %s, %s)
            """
            # Ejecutar con los valores ingresados
            cursor.execute(query, (cuit, razon_social, mail))
            conn.commit()

            print(f"Cliente insertado cliente cuit: {cuit}")

        elif opcion=="2": #modifcar
            print("Modificar cliente")
            cuit = input("Ingrese el cuit del cliente que desea modificar: ")
            cursor.execute("SELECT * FROM clientes WHERE cuit = %s", (cuit,))
            cliente = cursor.fetchone()    #crea una tupla con los datos del cliente.

            if cliente:
                print("Datos actuales del cliente:",cliente)   #imprimo lod datos del cliente 
                razon_social=input("Ingrese la nueva razón social: ")
                mail=input("Ingrese el nuevo mail:")

                cursor.execute("""
                UPDATE clientes
                SET razon_social =%s, mail =%s 
                WHERE cuit = %s""", (razon_social ,mail,cuit))
                conn.commit()
                print("cliente modificado")
            else:
                print("No se encontro cliente con ese cuit")

        elif opcion=="3": #eliminar cliente
            cuit=input("ingresar cuit del cliente que quiera eliminar:")
            sql = "DELETE FROM clientes WHERE cuit = %s "
            cursor.execute(sql,(cuit,))
            conn.commit()
            print(f"elimino el cliente cuit: {cuit}")

        elif opcion=="5":
            break
        else:
            break
    cursor.close()
    conn.close()

# gestionar_clientes()
