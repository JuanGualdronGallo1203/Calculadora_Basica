def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n=== CALCULADORA BÁSICA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def obtener_opcion():
    """Obtiene la opción seleccionada por el usuario."""
    while True:
        opcion = input("Seleccione una opción (1-5): ")
        if opcion in ["1", "2", "3", "4", "5"]:
            return opcion
        print("Opción inválida. Intente nuevamente.")