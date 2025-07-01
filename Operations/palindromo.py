# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 13:33:59 2025
@author: Arthur
@version: 1.0.0
"""

def Palindromo(palabra: str) -> int:
    """
    Función que determina si una palabra es un palíndromo.

    Un palíndromo es una palabra que se lee igual de izquierda a derecha que de derecha a izquierda.

    Parámetros:
    palabra (str): La palabra a comprobar.

    Retorna:
    int: Siempre retorna 0, ya que la función imprime el resultado directamente.
    """
    # Convertimos la palabra a minúsculas y eliminamos espacios para hacer la comparación más precisa
    palabra = palabra.lower().replace(" ", "")

    # Se divide la palabra en dos mitades para comparar si son iguales en orden inverso
    mitad1 = palabra[:len(palabra)//2]
    mitad2 = palabra[-(len(palabra)//2):][::-1]  # Invertimos la segunda mitad

    # Comparamos ambas mitades
    if mitad1 == mitad2:
        print(f"La palabra '{palabra}' es palíndromo")
    else:
        print(f"La palabra '{palabra}' no es palíndromo")

    return 0

# Ejecutar con manejo de errores
try:
    entrada = input("Ingrese una palabra: ")
    if not entrada.strip():
        raise ValueError("La entrada no puede estar vacía.")
    print(Palindromo(entrada))
except ValueError as ve:
    print(f"ERROR: {ve}")
except Exception as e:
    print(f"ERROR inesperado: {e}")
