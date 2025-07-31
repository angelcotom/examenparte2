def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Calcular MCD")
    print("2. crear una cadena repetida N veces")
    print("3. Cuenta cuantas veces aparece un letra en una cadena")
    print("4. Convierte un numero decimal a un binario")
    print("5. Calcular cuantos digitos tiene un numero")
    print("6. Salir")


    opcion = input("Elige una opción (1-5): ")

    match opcion:
        case "1":
            calcular_mcd()
            mostrar_menu()
        case "2":
            crear_cadena_Nveces ()
            mostrar_menu()
        case "3":
            print("cuenta cuantas veces aparece una letra en una cadena.")
            mostrar_menu()
        case "4":
            print("Convierte un numero decinmal a un binario.")
            mostrar_menu()
        case "5":
            print("Calvular cuantos digitos tiene un numero.")
        case "6":
            print(" Opción no válida. Intenta otra vez.")
            mostrar_menu()


def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


def calcular_mcd():
    print("\n Calcular MCD")
    try:
        a = int(input("Ingresa el primer número: "))
        b = int(input("Ingresa el segundo número: "))
        resultado = mcd(a, b)
        print(f"el MCD de {a} y {b} es: {resultado}")
    except ValueError:
        print(" Por favor, Ingresa solo números enteros.")
        calcular_mcd()



mostrar_menu()


