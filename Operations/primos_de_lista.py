# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 18:11:06 2025
@author: Arthur
@version: 1.0.0
"""

# Importamos la biblioteca sympy que tiene funciones matemáticas, incluyendo verificación de números primos
import sympy as sp

def PrimosDeLista(numeros: list) -> list:
    """
    Recibe una lista de números, filtra los primos y devuelve una nueva lista sin duplicados.

    Parámetros:
        numeros (list): Lista de números enteros.

    Retorna:
        list: Lista con los números primos encontrados en la lista original.
    """
    primos = []
    for primo in numeros:
        if sp.isprime(primo):
            if primo not in primos:
                primos.append(primo)
    return primos

# Solicita al usuario que ingrese una lista de números separados por comas
entrada = input("Ingrese una lista de números (Ejemplo: 1,3,4,5,6): ")

try:
    # Limpiar espacios y convertir a enteros
    lista = [int(num.strip()) for num in entrada.split(',') if num.strip()]
    
    if not lista:
        raise ValueError("La lista no puede estar vacía.")

    # Llama a la función y muestra los primos
    print(f"Estos son los primos de la lista: {PrimosDeLista(lista)}")

except ValueError as ve:
    print(f"ERROR: {ve}")
except Exception as e:
    print(f"ERROR inesperado: {e}")
