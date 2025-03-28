from operaciones import suma, resta, multiplicacion, division
from interfaz import mostrar_menu, obtener_opcion
from validaciones import obtener_numero

def ejecutar_calculadora():
    """Función principal que ejecuta la calculadora."""
    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == "5":
            print("¡Gracias por usar la calculadora! Hasta luego.")
            break

        # Obtener los números
        num1 = obtener_numero("Ingrese el primer número: ")
        num2 = obtener_numero("Ingrese el segundo número: ")

        # Realizar la operación seleccionada
        if opcion == "1":
            resultado = suma(num1, num2)
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif opcion == "2":
            resultado = resta(num1, num2)
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif opcion == "3":
            resultado = multiplicacion(num1, num2)
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif opcion == "4":
            resultado = division(num1, num2)
            print(f"Resultado: {num1} / {num2} = {resultado}")

if __name__ == "__main__":
    ejecutar_calculadora()