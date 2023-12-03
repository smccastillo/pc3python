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
