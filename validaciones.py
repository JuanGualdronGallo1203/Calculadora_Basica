def obtener_numero(mensaje):
    """Obtiene un número válido del usuario."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")