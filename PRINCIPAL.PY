import LISTAS
import TUPLAS
import CONJUNTO
import DICCIONARIO
import COMBINADAS
import ZIP


def menu_principal():
    while True:
        print("\n===================================")
        print("        MENU GENERAL")
        print("===================================")
        print("1. Ejercicios de Listas")
        print("2. Ejercicios de Tuplas")
        print("3. Ejercicios de Conjuntos")
        print("4. Ejercicios de Diccionarios")
        print("5. Ejercicios de Estructuras Combinadas")
        print("6. Ejercicios con zip()")
        print("7. Salir")
        print("===================================")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            LISTAS.menu_listas()

        elif opcion == "2":
            TUPLAS.menu_tuplas()

        elif opcion == "3":
            CONJUNTO.menu_conjuntos()

        elif opcion == "4":
            DICCIONARIO.menu_diccionarios()

        elif opcion == "5":
            COMBINADAS.menu_combinadas()

        elif opcion == "6":
            ZIP.menu_zip()

        elif opcion == "7":
            print("\nPrograma finalizado.")
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("\nOpcion no valida.")
            print("Seleccione una opcion del 1 al 7.")


menu_principal()