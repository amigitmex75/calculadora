from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def mostrar_menu():
    print("Calculadora")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Sumar N números")
    print("6. Salir")

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == '1':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = sumar(num1, num2)
        print("El resultado es:", resultado)
    # ... (resto de las opciones)
    elif opcion == '6':
        break
