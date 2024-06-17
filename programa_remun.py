from os import system
lista_trabajador=[]

def menu_principal():
    opciones = {
        '1': ('Registrar trabajador', reg_trabajador),
        '2': ('Listar todos los trabajadores', listar_trabajador),
        '3': ('Imprimir planilla de sueldos', imprimir_trabajador),
        '4': ('Salir del programa', salir)
    }

    generar_menu(opciones, '4')

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        system("cls")
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print() # se imprime una línea en blanco para clarificar la salida por pantalla

def mostrar_menu(opciones):
    print(lista_trabajador)
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def reg_trabajador():
    print('Has elegido la opción 1')
    print()
    nombre=input("Ingrese el nombre: ")
    lista_trabajador.append(nombre)
    apellido=input("Ingrese el apellido: ")
    lista_trabajador.append(apellido)
    cargo=input("Ingrese el cargo: ")
    lista_trabajador.append(cargo)
    sueldo=int(input("Ingrese su sueldo bruto: "))
    lista_trabajador.append(sueldo)
    desc_salud=round(sueldo*0.07)
    lista_trabajador.append(desc_salud)
    des_afp=round(sueldo*0.12)
    lista_trabajador.append(des_afp)
    


def listar_trabajador():
    print('Has elegido la opción 2')
    print()
    print(f"Trabajadores: \n Nombres: {lista_trabajador[0]}\n Apellidos: {lista_trabajador[1]} ")
    input()


def imprimir_trabajador():
    print('Has elegido la opción 3')
    input()


def salir():
    print('Saliendo')


menu_principal()