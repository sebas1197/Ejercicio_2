
def opcion1(lista):
    print("Has seleccionado la opción 1.")

def opcion2():
    print("Has seleccionado la opción 2.")

def opcion3():
    print("Has seleccionado la opción 3.")

def opcion4():
    print("Has seleccionado la opción 4.")

def opcion5():
    print("Has seleccionado la opción 5.")

def menu():

    
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
        opcion2()
    elif opcion == "3":
        opcion3()
    elif opcion == "4":
        opcion4()
    elif opcion == "5":
        opcion5()
    elif opcion == "6":
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


while True:
    menu()