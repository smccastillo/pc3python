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

from Module.pc3 import Producto, Phone, Persona, CIRCULO, Catalogo

rad = float(input("Ingrese el radio del círculo: "))
circulo1 = CIRCULO(rad)

area = circulo1.calcular_area()

print(circulo1)
print(f"Área del círculo: {area}")

catalogo = Catalogo()
prod1 = Producto("Motor", 1999.99)
prod2 = Producto("Batería", 899.99)
catalogo.agregar_producto(prod1)
catalogo.agregar_producto(prod2)

producto = Producto("Ejemplo", "PERU-0001-2023")
print(producto)

telf = Phone("Motorola", "G53", "16GB", "512 GB", "18 horas")
telf.iniciar_llamada("123456789")
telf.registrar_duracion_llamada(120)
telf.finalizar_llamada()
print(telf)

pers1= Persona()
print(pers1)