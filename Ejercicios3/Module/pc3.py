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

#Clase Phone
class Perfil:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password
    def __str__(self):
        return f"{self.name} con email {self.email}"

class Phone: 
    def __init__(self,marca,modelo,memoria_ram,memoria_sd,dur_bateria):
        self.number_assign=""
        self.perfil:Perfil=""
        self.switch_phone=True
        self.estado="ACTIVO"
        self.marca=marca
        self.modelo=modelo
        self.memoria_ram=memoria_ram
        self.memoria_sd=memoria_sd
        self.dur_bateria=dur_bateria
        self.pin=""
        # Nuevos atributos
        self.llamada_en_curso = False
        self.duracion_llamada = 0

    def showPower(self):
        if self.switch_phone:
            print("el equipo está prendido")
        else:
            print("el equipo está apagado")

    def iniciar_llamada(self, numero):
        if self.switch_phone and self.estado == "ACTIVO":
            print(f"Iniciando llamada a {numero}...")
            self.llamada_en_curso = True
        else:
            print("No es posible iniciar la llamada. Verifique el estado del teléfono.")

    def finalizar_llamada(self):
        if self.llamada_en_curso:
            print("Llamada finalizada.")
            self.llamada_en_curso = False
        else:
            print("No hay ninguna llamada en curso.")

    def registrar_duracion_llamada(self, duracion):
        if self.llamada_en_curso:
            self.duracion_llamada += duracion
        else:
            print("No hay ninguna llamada en curso para registrar la duración.")

    def __str__(self):
        return f"Phone: {self.marca} {self.modelo}, Estado: {self.estado}, Duración de llamada: {self.duracion_llamada} segundos"

#Clase Persona e ingreso por teclado
class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre completo: ")
        self.edad = int(input("Ingrese la edad: "))
        self.genero = input("Ingrese el género: ")
        self.altura = float(input("Ingrese la altura: "))
        self.peso = float(input("Ingrese el peso (kg): "))

    def __str__(self):
        return f"Persona: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Altura: {self.altura} m, Peso: {self.peso} kg"