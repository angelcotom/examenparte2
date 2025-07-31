def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Calcular MCD")
    print("2. Crear una cadena repetida N veces")
    print("3. Contar cuántas veces aparece una letra en una cadena")
    print("4. Convertir un número decimal a binario")
    print("5. Calcular cuántos dígitos tiene un número")
    print("6. Salir")

    opcion = input("Elige una opción (1-6): ")

    match opcion:
        case "1":
            calcular_mcd()
        case "2":
            crear_cadena_Nveces()
        case "3":
            buscar_letra()
        case "4":
            decimal_a_binario()
        case "5":
            calcular_digitos()
        case "6":
            print("Gracias por usar el programa.")
            return
        case _:
            print("Opción no válida. Intenta otra vez.")

    mostrar_menu()



def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


def calcular_mcd():
    print("\nCalcular MCD")
    try:
        a = int(input("Ingresa el primer número: "))
        b = int(input("Ingresa el segundo número: "))
        resultado = mcd(a, b)
        print(f"El MCD de {a} y {b} es: {resultado}")
    except ValueError:
        print("Por favor, ingresa solo números enteros.")
        calcular_mcd()



def crear_cadena_Nveces():
    print("\nCrear una cadena repetida N veces")
    try:
        texto = input("Ingresa la palabra o cadena: ")
        repeticion = int(input("¿Cuántas veces deseas repetirla?: "))
        for i in range(1, repeticion + 1):
            print(f"{i}. {texto}")
    except ValueError:
        print("Error: debes ingresar un número entero.")
        crear_cadena_Nveces()



def contar_letra(cadena, letra):
    if cadena == "":
        return 0
    elif cadena[0] == letra:
        return 1 + contar_letra(cadena[1:], letra)
    else:
        return contar_letra(cadena[1:], letra)


def buscar_letra():
    print("\nContar letras en una cadena")
    cadena = input("Escribe una palabra o frase: ").lower()
    letra = input("¿Qué letra quieres contar?: ").lower()

    if len(letra) != 1:
        print("Debes ingresar solo una letra.")
        return buscar_letra()

    cantidad = contar_letra(cadena, letra)
    print(f"La letra '{letra}' aparece {cantidad} veces en '{cadena}'.")



def decimal_a_binario():
    print("\nConvertir número decimal a binario")
    try:
        num = int(input("Ingresa un número decimal: "))
        binario = convertir_binario(num)
        print(f"El número {num} en binario es: {binario}")
    except ValueError:
        print("Por favor, ingresa solo números enteros.")
        decimal_a_binario()


def convertir_binario(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return convertir_binario(num // 2) + str(num % 2)



def calcular_digitos():
    print("\nCalcular cuántos dígitos tiene un número")
    try:
        numero = int(input("Ingresa un número entero: "))
        digitos = contar_digitos(abs(numero))
        print(f"El número tiene {digitos} dígitos.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
        calcular_digitos()


def contar_digitos(num):
    if num < 10:
        return 1
    else:
        return 1 + contar_digitos(num // 10)



mostrar_menu()


