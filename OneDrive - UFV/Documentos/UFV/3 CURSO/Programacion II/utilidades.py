"""
Título: Clase estática de utilidades
Autor: alejandro.gonzález
Fecha: 15/10/2025
Descripción: La clase utilidades agrupa métodos útiles para operaciones comunes.
Al ser estática, no requiere crear instancias para usarse.
"""

class Utilidades:
    """Clase estática con métodos utilitarios."""

    @staticmethod
    def es_primo(numero: int) -> bool:
        """
        Devuelve True si el número es primo, False si no lo es.
        """
        if numero <= 1:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

    @staticmethod
    def factorial(numero: int) -> int:
        """
        Devuelve el factorial de un número, si es negativo devuelve None.
        """
        if numero < 0:
            return None
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

    @staticmethod
    def es_palindromo(cadena: str) -> bool:
        """
        Devuelve True si la cadena es un palíndromo. Ignora mayúsculas, minúsculas y espacios.
        """
        texto = cadena.replace(" ", "").lower()
        return texto == texto[::-1]

    @staticmethod
    def suma_digitos(numero: int) -> int:
        """
        Devuelve la suma de los dígitos de un número entero.
        """
        return sum(int(digito) for digito in str(abs(numero)))

# -------------------------------
# Ejemplos
# -------------------------------
if __name__ == "__main__":
    print("¿7 es primo?", Utilidades.es_primo(7))
    print("Factorial de 5:", Utilidades.factorial(5))
    print("¿'Solos' es palíndromo?", Utilidades.es_palindromo("Solos"))
    print("Suma de los dígitos de 204:", Utilidades.suma_digitos(204))
