import random
import csv
import math

#La aplicación debe permitir analizar los sueldos de 10 empleados, los cuales para efectos de este prototipo se crearán de
#forma aleatoria entre $300.000 y $2.500.000. Utilice la siguiente lista para asignar los sueldos a cada empleado

#Listas para guardar empleados y sueldos
empleados = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos = []

#Función para asignar sueldos aleatorios

def generar_sueldos():
    for _ in range(10):
        sueldos.append(random.randint(300000, 2500000))


