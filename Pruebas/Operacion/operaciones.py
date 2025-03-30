# Funciones para cada operación
def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: No se puede dividir entre 0"
    else:
        return x / y

# Menú de opciones
def menu():
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

# Ciclo principal
while True:
    menu()
    operacion = input("Ingrese el número de la operación (1/2/3/4) o 'salir' para terminar: ")
    
    if operacion == 'salir':
        print("¡Gracias por usar la calculadora!")
        break
    
    if operacion in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if operacion == '1':
            print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")
        elif operacion == '2':
            print(f"Resultado: {num1} - {num2} = {resta(num1, num2)}")
        elif operacion == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicacion(num1, num2)}")
        elif operacion == '4':
            print(f"Resultado: {num1} / {num2} = {division(num1, num2)}")
    else:
        print("Opción no válida, por favor intente nuevamente.")
