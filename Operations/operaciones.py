# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 17:04:37 2025
@author: Arthur
@version: 1.0.0
"""

def Operaciones(numero1: float, numero2: float, operador: str) -> float:
    """
    Realiza una operación matemática entre dos números.

    Parámetros:
        numero1 (float): El primer número.
        numero2 (float): El segundo número.
        operador (str): El operador a utilizar. Puede ser '+', '-', '*', '/'.

    Retorna:
        float: El resultado de la operación.
    """
    if operador == '+':
        return numero1 + numero2
    elif operador == '-':
        return numero1 - numero2
    elif operador == '*':
        return numero1 * numero2
    elif operador == '/':
        if numero2 != 0:
            return numero1 / numero2
        else:
            raise ValueError("No se puede dividir entre cero.")
    else:
        raise ValueError("Operador no válido. Debe ser '+', '-', '*' o '/'.")

if __name__ == "__main__":
    try:
        num_1 = float(input("Ingrese el primer número a operar: "))
        num_2 = float(input("Ingrese el segundo número a operar: "))
        operador = input("Ingrese el operador (*,+,-,/): ").strip()

        resultado = Operaciones(num_1, num_2, operador)
        print(f"El resultado de {num_1} {operador} {num_2} es {resultado}")

    except ValueError as ve:
        print(f"ERROR: {ve}")
    except Exception as e:
        print(f"ERROR inesperado: {e}")
