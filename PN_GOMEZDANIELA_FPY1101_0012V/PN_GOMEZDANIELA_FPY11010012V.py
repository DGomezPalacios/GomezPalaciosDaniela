import random
import csv
import math

#La aplicación debe permitir analizar los sueldos de 10 empleados, los cuales para efectos de este prototipo se crearán de
#forma aleatoria entre $300.000 y $2.500.000. Utilice la siguiente lista para asignar los sueldos a cada empleado

#Listas para guardar trabajadores y sueldos
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos = {}

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
        elif opcion == '3':
            estadisticas_sueldos()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5':
            salir()
            break
        else:
            print("Opción no válida, intente nuevamente.")


#Función para asignar sueldos aleatorios

def generar_sueldos():
    for i in range(10):
        sueldos[trabajadores[i]] = random.randint(300000, 2500000)
    print("Sueldos asignados:")
    for trabajador, sueldo in sueldos.items():
        print(f"Trabajador: {trabajador}, Sueldo: ${sueldo}")

#Funcion para clasificar sueldos en 3 categotrias

def clasificar_sueldos():
    clasificados = {"<800": [], "800>=2mm": [], "+2mm": []}
    for empleado, sueldo in sueldos.items():
        if sueldo < 800000:
            clasificados["<800"].append(empleado)
        elif 800000 <= sueldo <= 2000000:
            clasificados["800>=2mm"].append(empleado)
        else:
            clasificados["+2mm"].append(empleado)
    
    print("\nClasificación de sueldos:")
    print("Sueldos menores a $800.000:", len(clasificados["<800"]))
    for t in clasificados["<800"]:
        print(f"Nombre empleado: {t} Sueldo: ${sueldos[t]}")
    
        # Mostrar sueldos entre $800.000 y $2.000.000
    print("Sueldos entre $800.000 y $2.000.000:", len(clasificados["800>=2mm"]))
    for t in clasificados["800>=2mm"]:
        print(f"Nombre empleado: {t} Sueldo: ${sueldos[t]}")
    
    # Mostrar sueldos superiores a $2.000.000
    print("Sueldos superiores a $2.000.000:", len(clasificados["+2mm"]))
    for t in clasificados["+2mm"]:
        print(f"Nombre empleado: {t} Sueldo: ${sueldos[t]}")
    
    #sumar el toal de sueldos

    total_sueldos = sum(sueldos.values())
    print(f"\nTOTAL SUELDOS: ${total_sueldos}")

#Funcion de estadisticas de sueldos

def estadisticas_sueldos():
    sueldos_list = list(sueldos.values())
    sueldo_max = max(sueldos_list)
    sueldo_min = min(sueldos_list)
    promedio = sum(sueldos_list) / len(sueldos_list)
    media_geom = math.exp(sum(math.log(s) for s in sueldos_list) / len(sueldos_list))

    #impimir
    print("\nEstadísticas:")
    print(f"Sueldo máximo: ${sueldo_max}")
    print(f"Sueldo mínimo: ${sueldo_min}")
    print(f"Promedio de sueldos: ${promedio}")
    print(f"Media geométrica de sueldos: ${media_geom}")

#función para mostrar el detalle de los sueldos de los trabajadores, según la siguiente regla de negocio:
#Descuento salud 7%
#Descuento AFP 12%
#Sueldo líquido calculado en base al sueldo base menos el descuento en salud y menos el descuento afp

def reporte_sueldos():
    desc_salud = 0.07  
    desc_afp = 0.12    
    
    with open('reporte_sueldos.csv', 'w', newline='') as csvfile:
        # darle los nombres a las colujmnas
        fieldnames = ['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # escribir los encabezads
        writer.writeheader()
        # escribir los datos de los trabajdores
        for i, sueldo in enumerate(sueldos):
            salud = sueldo * desc_salud
            afp = sueldo * desc_afp
            sueldo_liq = sueldo - salud - afp
            writer.writerow({
                'Nombre empleado': trabajadores[i],
                'Sueldo Base': sueldo,
                'Descuento Salud': salud,
                'Descuento AFP': afp,
                'Sueldo Líquido': sueldo_liq
            })

    print("Reporte generado y exportado a 'reporte_sueldos.csv'")

    #Funcion para dsalir del progrmama
def salir():
    print("Finalizando programa...")
    print("\nNombre: Daniela Gómez Palacios \nRUT: 18.593.726-7")



if __name__ == "__main__":
    menu()