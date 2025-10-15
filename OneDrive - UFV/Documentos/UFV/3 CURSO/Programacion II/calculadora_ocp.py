"""
Título: Calculadora básica aplicando el principio abierto-cerrado
Autor: alejandro.gonzalez
Fecha: 15/10/2025
Descripción: Calculadora que permite agregar nuevas operaciones sin modificar su código base.
Se aplica el principio de abierto-cerrado (OCP) usando herencia y polimorfismo.
"""

from abc import ABC, abstractmethod

# -------------------------------
# Clase base abstracta
# -------------------------------
class Operacion(ABC):
    @abstractmethod
    def calcular(self, a: float, b: float) -> float:
        """Este método lo deben implementar todas las operaciones."""
        pass


# -------------------------------
# Operaciones básicas
# -------------------------------
class Suma(Operacion):
    def calcular(self, a: float, b: float) -> float:
        return a + b


class Resta(Operacion):
    def calcular(self, a: float, b: float) -> float:
        return a - b


class Multiplicacion(Operacion):
    def calcular(self, a: float, b: float) -> float:
        return a * b


class Division(Operacion):
    def calcular(self, a: float, b: float) -> float:
        if b == 0:
            return "Error: no se puede dividir entre cero."
        return a / b


# -------------------------------
# Calculadora principal
# -------------------------------
class Calculadora:
    def __init__(self):
        # Estás son las operaciones disponibles en esta calculadora
        self.operaciones = {
            "sumar": Suma(),
            "restar": Resta(),
            "multiplicar": Multiplicacion(),
            "dividir": Division(),
        }

    def agregar_operacion(self, nombre: str, operacion: str):
        """Sirve para agregar nuevas operaciones sin cambiar el código existente."""
        self.operaciones[nombre] = operacion

    def ejecutar(self, nombre_operacion: str, a: float, b: float):
        if nombre_operacion not in self.operaciones:
            return f"Operación no válida: {nombre_operacion}"
        return self.operaciones[nombre_operacion].calcular(a, b)


# -------------------------------
# Ahora, aplicando el principio OCP, añado la operación potencia sin modificar la calculadora.
# -------------------------------
class Potencia(Operacion):
    def calcular(self, a: float, b: float) -> float:
        return a ** b


# -------------------------------
# Ejemplo
# -------------------------------
if __name__ == "__main__":
    calculadora = Calculadora()
    
    # Agrego la operación de potencia sin modificar la clase
    calculadora.agregar_operacion("potencia", Potencia())

    print("Operaciones disponibles: sumar, restar, multiplicar, dividir, potencia")

    while True:
        op = input("\nEscribe una operación (o 'salir' para terminar): ").lower()
        if op == "salir":
            print("¡Chao!")
            break

        try:
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
        except ValueError:
            print("Por favor ingresa solo números.")
            continue

        resultado = calculadora.ejecutar(op, a, b)
        print(f"Resultado de {op}: {resultado}")
