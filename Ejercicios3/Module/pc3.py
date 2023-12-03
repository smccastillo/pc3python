# Área de un círculo
class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = 3.14159 * (self.radio ** 2)
        return area

# Tienda autopartes - Catalogar productos
class Producto:
    def __init__(self, nombre, precio, lanzamiento):
        self.nombre = nombre
        self.precio = precio
        self.lanzamiento = lanzamiento

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"{producto.nombre} - {producto.precio} - {producto.lanzamiento}")

#Clase Producto, idenfiticar país y lote
class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def identificar_pais_y_lote(self):
        partes = self.codigo.split('-')
        
        if len(partes) == 3:
            pais = partes[0]
            lote = partes[1]
            return pais, lote
        else:
            return None, None

    def __str__(self):
        pais, lote = self.identificar_pais_y_lote()
        return f"Producto: {self.nombre}, Código: {self.codigo}, País: {pais}, Lote: {lote}"


