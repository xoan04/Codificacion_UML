class Persona():
    def __init__(self, email, direccion, telefono):
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.animales = {}

    def setAnimales(self, dicAnimales):
        self.animales = dicAnimales

class Fisica(Persona):
    def __init__(self, dni):
        self.dni = dni


class Juridica(Persona):
    def __init__(self, cif):
        self.cif = cif

class Animal():
    def __init__(self, tipo, nombre, edad):
        self.tipo = tipo
        self.nombre = nombre
        self.edad = edad
        self.persona = None
        self.historico = None
        self.diagnosticos = {}

    def setPersona(self, persona):
        self.persona = persona

    def setHistorico(self, historico):
        self.historico = historico

    def setDiagnosticos(self, diagnosticos):
        self.diagnosticos = diagnosticos

class Historico():
    def __init__(self, refHistorico):
        self.refHistorico = refHistorico
        self.elementosHistorico = {}

    def setElementosHistorico(self, elementosHistorico):
        self.elementosHistorico = elementosHistorico

class ElementoHistorico():
    def __init__(self):
        self.historico = None
    
    def setHistorico(self, historico):
        self.historico = historico

class Diagnostico():
    def __init__(self, fecha, descripcion):
        self.fecha = fecha
        self.descripcion = descripcion
        self.animal = None
        self.factura = None
        self.personal = None

    def setAnimal(self, animal):
        self.animal = animal
    
    def setFactura(self, factura):
        self.factura = factura

    def setPersonal(self, personal):
        self.personal = personal

class Factura():
    def __init__(self, refFactura):
        self.refFactura = refFactura
        self.diagnostico = None
        self.elementosFactura = {}

    def setDiagnostico(self, diagnostico):
        self.diagnostico = diagnostico

    def elementosFactura(self, elementosFactura):
        self.elementosFactura = elementosFactura

class ElementosFactura():
    def __init__(self, elemento, precio, cantidad):
        self.elemento = elemento
        self.precio = precio
        self.cantidad = cantidad
        self.factura = None

    def setFactura(self, factura):
        self.factura = factura

class Personal():
    def __init__(self, nombre, apellidos, fechaContratacion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.fechaContratacion = fechaContratacion
        self.diagnosticos = {}

    def setDiagnosticos(self, diagnosticos):
        self.diagnosticos = diagnosticos

class Veterinario(Personal):
    def __init__(self):
        pass

class Auxiliar(Personal):
    def __init__(self):
        pass