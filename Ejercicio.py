from num1 import num1


def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2): 
    return num1 * num2
'''Aqui en esta parte nos va ayudar a definir la funcion que necesitamos es lo que va a realizar la operación'''
def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: División por cero."

while True:
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input(" Por favor Seleccione la operación que desea realizar (1/2/3/4/5): ")

    if opcion == '5':
        print("¡Hasta luego!")
        break
''''''
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print("El resultado de la suma es:", suma(num1, num2))
    elif opcion == '2':
        print("El resultado de la resta es:", resta(num1, num2))
    elif opcion == '3':
        print("El resultado de la multiplicación es:", multiplicacion(num1, num2))
    elif opcion == '4':
        print("El resultado de la división es:", division(num1, num2))
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
