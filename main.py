# Variables
salir = False
opc = int(input("""Introduce una opción:
Opción 1: Registrar un usuario
Opción 2: Ver todos o un usuario
"""))

# Listas y/o diccionarios
usuarios = {123:["david","lattanzio","españa",7189563],
            456:["alvaro","garcia","españa",163481]}
compras = {987:[123]}
while salir == False:
    match opc:
        case 1:
            print("Ha escogido registrar un usuario")
            dni = int(input("Cuál es el dni del usuario: "))
            nombre = input("Escribe el nombre: ")
            apellido = input("Escribe el apellido: ")
            pais = input("Escribe el pais: ")
            telefono = input("Escribe el telefono: ")

            usuarios[dni] = [nombre, apellido, pais, telefono]
            opc = int(input("""

Introduce una opción:
Opción 1: Registrar un usuario
Opción 2: Ver todos o un usuario
"""))
        case 2:
            # A partir de aquí se elige la opcion, ver todos los  usuarios o uno en concreto
            opc2 = int(input("""

Para ver todos o varios usuarios:
Opción 1: Ver todos
Opción 2: Ver un usuario
"""))
            match opc2:
                case 1:
                    # print(usuarios)
                    for clave, valor in usuarios.items():
                        print("DNI: ", clave, end=": ")
                        for dato in valor:
                            print(dato, end=" ")
                    opc = int(input("""

Introduce una opción:
Opción 1: Registrar un usuario
Opción 2: Ver todos o un usuario
"""))
                case 2:
                    usuario = int(
                        input("Introduce el dni de un usuario para ver sus datos: "))
                    if usuario in usuarios.keys():
                        print(usuario, end=": ")
                        for dato in usuarios[usuario]:
                            print(dato, end=" ")

                    opc = int(input("""

Introduce una opción:
Opción 1: Registrar un usuario
Opción 2: Ver todos o un usuario
"""))
                case _:
                    opc = int(input("""
Introduce una opción: 
Opción 1: Registrar un usuario
Opción 2: Ver todos o un usuario
"""))
        case 3:
            print("Ha escogido registrar una compra")
            idcompra = int(input("Escribe el numero de compra: "))
            dni = int(input("Cuál es el dni del usuario: "))
            productos = []
            cantp = int(
                input("Introduce la cantidad de productos que quieres registrar: "))
            print("Introduce los productos")
            for i in range(0, cantp):
                productos.append(input())
            compras[idcompra] = [dni, productos]
            #// compras[idcompra][0]
            for x in compras[idcompra][1]:
                print(x)
            opc = int(input(""" 

Introduce una opción: 
Opción 1: Registrar un usuario
Opción 2: Ver todos o un usuario
"""))
        case 4:
            print("Ha escogido ver una compra")
            compra = int(input("Introduce número de compra: "))
            if compra in compras.keys():
                print(compra, end=": ")
                for dato in compras[compra][1]:
                    print(dato, end=" ")
                    
            opc = int(input(""" 

Introduce una opción: 
Opción 1: Registrar un usuario
Opción 2: Ver todos o un usuario
"""))



