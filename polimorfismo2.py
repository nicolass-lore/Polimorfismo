class Calzado:
    def __init__(self, fecha_creacion, made_in, marca, tipo, numero, suela ):
        self.fecha_creacion = fecha_creacion
        self.made_in = made_in
        self.marca =  marca
        self.tipo = tipo
        self.numero = numero
        self.suela = suela
def made_in(self):
    return f"made_in: {self.made_in}"

def fecha_creacion(self):
    return f"fecha_creacion: ${self.fecha_creacion}"

def marca(self):
    return f"marca: {self.marca}"

def tipo(self):
    return f"tipo: {self.tipo}"

def numero(self):
    return f"numero: {self.numero}"

def suela(self):
    return f"suela: {self.suela}"
class Zapatilla(Calzado):
    def __init__(self, fecha_creacion, made_in, marca, tipo, numero, suela, tipo_deportivo, materiales, modelo, stock):
        super().__init__(fecha_creacion, made_in, marca, tipo, numero, suela, tipo_deportivo, modelo, materiales, stock )
        self.tipo_deportivo = tipo_deportivo
        self.modelo = modelo
        self. modelo = materiales
        self.stock = stock
    def mostrar_tipo_deportivo(self):
        return f"tipo de depotivo: {self.tipo_deportivo}"

    def mostrar_modelo(self):
        return f"modelo: {self.modelo}"

    def mostrar_materiales(self):
        return f"materiales: {self.materiales}"
    
    def mostrar_stock(self):
        return f"stock: {self.stock}"
Zapatilla1= Zapatilla()
Zapatilla2= Zapatilla()
