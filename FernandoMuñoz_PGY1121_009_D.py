import random

vehiculos = []

def grabar_vehiculo():
    tipo = input("Ingrese el tipo de vehículo: ")
    patente = input("Ingrese la patente del vehículo: ")
    marca = input("Ingrese la marca del vehículo: ")
    precio = 0
    try:
        precio = int(input("Ingrese el precio del vehículo: "))
    except ValueError:
        print("Error: El precio debe ser un número entero.")
        return

    multas = []
    fecha_registro = input("Ingrese la fecha de registro del vehículo: ")
    nombre_dueño = input("Ingrese el nombre del dueño del vehículo: ")

    if len(patente) != 6 or not patente.isalnum():
        print("La patente ingresada es incorrecta.")
        return
    
    if len(marca) < 2 or len(marca) > 15:
        print("La marca debe tener entre 2 y 15 caracteres.")
        return
    
    if precio <= 5000000:
        print("El precio debe ser mayor a $5.000.000.")
        return
    
    vehiculo = {
        "tipo": tipo,
        "patente": patente,
        "marca": marca,
        "precio": precio,
        "multas": multas,
        "fecha_registro": fecha_registro,
        "nombre_dueño": nombre_dueño
    }

    vehiculos.append(vehiculo)
    print("Vehículo grabado exitosamente.")

def buscar_vehiculo():
    patente = input("Ingrese la patente del vehículo a buscar: ")

    for vehiculo in vehiculos:
        if vehiculo["patente"] == patente:
            print("Información del vehículo:")
            print(f"Tipo: {vehiculo['tipo']}")
            print(f"Patente: {vehiculo['patente']}")
            print(f"Marca: {vehiculo['marca']}")
            print(f"Precio: {vehiculo['precio']}")
            print(f"Fecha de registro: {vehiculo['fecha_registro']}")
            print(f"Nombre del dueño: {vehiculo['nombre_dueño']}")
            return

    print("No se encontró ningún vehículo con la patente ingresada.")

def imprimir_certificados():
    for vehiculo in vehiculos:
        certificado_emision = random.randint(1500, 3500)
        certificado_anotaciones = random.randint(1500, 3500)
        certificado_multas = random.randint(1500, 3500)

        print("Certificado de Emisión de Contaminantes")
        print(f"Patente: {vehiculo['patente']}")
        print(f"Dueño: {vehiculo['nombre_dueño']}")
        print(f"Monto: ${certificado_emision}")
        print("")

        print("Certificado de Anotaciones Vigentes")
        print(f"Patente: {vehiculo['patente']}")
        print(f"Dueño: {vehiculo['nombre_dueño']}")
        print(f"Monto: ${certificado_anotaciones}")
        print("")

        print("Certificado de Multas")
        print(f"Patente: {vehiculo['patente']}")
        print(f"Dueño: {vehiculo['nombre_dueño']}")
        print(f"Monto: ${certificado_multas}")
        print("")

def menu():
    print("------ Menú ------")
    print("1. Grabar vehículo")
    print("2. Buscar vehículo")
    print("3. Imprimir certificados")
    print("4. Salir")

while True:
    menu()
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        grabar_vehiculo()
    elif opcion == "2":
        buscar_vehiculo()
    elif opcion == "3":
        imprimir_certificados()
    elif opcion == "4":
        print("Gracias por usar el programa.")
        print("Autor: Fernando Muñoz")
        print("Versión: 1.0")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
