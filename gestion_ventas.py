import conectormysql
import datetime as datatime
def gestionar_ventas():
    print("Bienvenido a la gestión de ventas")
    print("1. Registrar una nueva venta")
    print("2. Consultar ventas")
    print("3. Anular una venta")


    opcion = input("Ingrese una opción: ")
    conector, cursor = conectormysql.conectarDB() 

    if opcion == "1":
        print("Registrar una nueva venta")
        codigo_destino = input("Ingrese el codigo destino: ")
        cuit = input("Ingrese el cuit del cliente: ")
        fecha_de_viaje = input("(ingresar cantidad de dias (Ingrese la fecha de viaje (YYYY-MM-DD):) ")
        
        try:
            fecha_de_venta = datatime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            query = """
                    INSERT INTO ventas (codigo_destino, cuit, fecha_de_venta, cant_dias_de_viaje)
                    VALUES (%s, %s, %s, %s)
                """
            cursor.execute(query, (codigo_destino, cuit, fecha_de_venta,fecha_de_viaje)) 
            conector.commit()
            print(f"Ha agregado al venta a Cuit: {cuit}")

                
        except Exception as e:
            print("Error al agregar cliente:", e)

#gestionar_ventas()

