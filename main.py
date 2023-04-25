import csv

def opcion1(lista):
    contador = 0
    for i in lista:
        if i[1] > '17' and i[3] == '1': #se asume que 1 es hombre
            contador += 1
    print("La cantidad de hombres mayores de 17 es: ", contador)

def opcion2(lista):
    contador = 0
    for i in lista:
        if i[1] > '17' and i[3] == '0': #se asume que 1 es hombre
            contador += 1
    print("La cantidad de mujeres mayores de 17 es: ", contador)

def opcion3(lista):
    contador = 0
    for i in lista:
        if i[1] < '13' and i[3] == '1': #se asume que 1 es hombre
            contador += 1
    print("La cantidad de niños menores de 13 es: ", contador)

def opcion4(lista):
    contador = 0
    for i in lista:
        if i[1] < '13' and i[3] == '0': #se asume que 1 es hombre
            contador += 1
    print("La cantidad de niñas menores de 13 es: ", contador)

def opcion5():
    print("Has seleccionado la opción 5.")

def menu():

    with open('train_and_test2.csv') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=',')
        lista_datos = []
        for fila in lector_csv:
            lista_datos.append(fila)
    
    print("Seleccione una opción:")
    print("1. Hombres mayores de 17")
    print("2. Mujeres mayores de 17")
    print("3. Ninios menores de 13")
    print("4. Ninias menores de 13")
    print("5. Hombres y mujeres entre 13 y 17")
    print("6. Salir")

    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        opcion1(lista_datos)
    elif opcion == "2":
        opcion2(lista_datos)
    elif opcion == "3":
        opcion3(lista_datos)
    elif opcion == "4":
        opcion4(lista_datos)
    elif opcion == "5":
        opcion5()
    elif opcion == "6":
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


while True:
    menu()
