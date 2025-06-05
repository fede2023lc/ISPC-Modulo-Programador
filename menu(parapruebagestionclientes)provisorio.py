import gestion_clientes
"""
import gestion_destinos
import gestion_ventas
import Funciones
"""
# Programa principal
while True:

    print("==============================")
    print("Bienvenido a skyroute")
    print("1. Gestionar Clientes")
    print("2. Gestionar Ventas")
    print("3. Gestionar Destinos")
    print("4. Consultar Ventas")
    print("5. Boton de Arrepentimiento")
    print("6. Reportes por sesión")
    print("7. Acerca del Sistema")
    print("8. SALIR")
    print("==============================")
    opcion = input("Ingrese una opción: ")
    print(f"Seleccionó opción: {opcion}")
    
    if opcion == "1":
        gestion_clientes.gestionar_clientes()
    elif opcion == "8":
        print("Seleccionó SALIR. \nGracias por usar Sistema de Gestión de Ventas de Skyroute. Hasta luego.")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
