'''
titulo: principio de sustitución de Liskov
autor: alejandro.gonzalez
fecha: 22.10.2025
descripcion: jerarquía de vehículos que cumpla con el principio de sustitución de Liskov.
Esto significa que cualquier instancia de una subclase debe poder usarse donde esperemos 
una instancia de la clase base sin cambiar el comportamiento correcto del programa.
'''

# Clase base Vehiculo
class Vehiculo:
    def acelerar(self):
        """Simula que el vehículo acelera"""
        return "El vehículo acelera"

    def frenar(self):
        """Simula que el vehículo frena"""
        return "El vehículo frena"


# Subclase Coche
class Coche(Vehiculo):
    def acelerar(self):
        # Mensaje específico para diferenciar la subclase
        return "El coche acelera y gana velocidad"

    def frenar(self):
        return "El coche frena suavemente"


# Subclase Bicicleta
class Bicicleta(Vehiculo):
    def acelerar(self):
        return "La bicicleta acelera pedaleando"

    def frenar(self):
        return "La bicicleta frena con los frenos manuales"


# Subclase Moto
class Moto(Vehiculo):
    def acelerar(self):
        return "La moto acelera con fuerza"

    def frenar(self):
        return "La moto frena con el freno delantero y trasero"

# Función que acepta cualquier vehiculo y utiliza sus métodos acelerar y frenar

def usar_vehiculo(vehiculo: Vehiculo):
    print(vehiculo.acelerar())
    print(vehiculo.frenar())


# Instancias de las subclases
coche = Coche()
bicicleta = Bicicleta()
moto = Moto()

# Función según los diferentes tipos de vehículos
print("Usando un coche:")
usar_vehiculo(coche)

print("\nUsando una bicicleta:")
usar_vehiculo(bicicleta)

print("\nUsando una moto:")
usar_vehiculo(moto)
