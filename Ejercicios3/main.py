from Module.pc3 import CIRCULO

circ1 = CIRCULO(4)

from Module.operacionesMI import dividir

def mostrar_opciones():
    print("Menú:")
    print("1. Dividir dos números")
    print("2. Salir")

def main():
    try:
        while True:
            mostrar_opciones()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                
                resultado = dividir(num1, num2)
                if resultado is not None:
                    print(f"Resultado de la división: {resultado}")
            elif opcion == "2":
                print("Saliendo del programa.")
                break
            else:
                print(f"Opción no válida. La ruta del directorio de trabajo es: {os.getcwd()}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        print("Proceso terminado.")
if __name__ == "__main__":
    main()

