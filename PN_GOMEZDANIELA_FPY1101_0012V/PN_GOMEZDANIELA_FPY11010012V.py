import random
import csv
import math

#La aplicación debe permitir analizar los sueldos de 10 empleados, los cuales para efectos de este prototipo se crearán de
#forma aleatoria entre $300.000 y $2.500.000. Utilice la siguiente lista para asignar los sueldos a cada empleado

#Listas para guardar trabajadores y sueldos
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos = []

#Menú
def menu():
    while True:
        print("\nMenú:")
        print("1.- Asignar sueldos aleatorios")
        print("2.- Clasificar sueldos")
        print("3.- Ver estadísticas")
        print("4.- Reporte de sueldos")
        print("5.- Salir del programa")

        #Leer la opcion del usuario
        opcion = input("Seleccione una opción: ")

        #Ejecutar lo que leigió el usuairo
        if opcion == '1':
            generar_sueldos()
        elif opcion == '2':
            clasificar_sueldos()



#Función para asignar sueldos aleatorios

def generar_sueldos():
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos asignados:", sueldos)

#Funcion para clasificar sueldos

def clasificar_sueldos():
    sueldos_ordenados = sorted(sueldos)
    mediana = sueldos_ordenados[len(sueldos_ordenados) // 2]
    print("Sueldo medio:", mediana)

