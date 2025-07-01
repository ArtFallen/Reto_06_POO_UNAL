# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 18:33:36 2025
@author: Arthur
@version: 1.0.0
"""

def MayorSumaConsecutiva(lista: list) -> int:
    """
    Determina la mayor suma entre pares de números consecutivos en una lista.
    
    Parámetros:
    lista (list): Lista de números enteros.

    Retorna:
    int: El valor máximo de la suma entre dos elementos consecutivos.
    """
    if not lista or len(lista) < 2:
        raise ValueError("La lista debe contener al menos dos números.")
    
    maximo = float('-inf')
    for i in range(len(lista) - 1):
        valor = lista[i] + lista[i + 1]
        if valor > maximo:
            maximo = valor
    return maximo

if __name__ == "__main__":
    entrada = input("Ingrese una lista de números (Ejemplo: 1,3,4,5,6): ")
    
    try:
        # Convertir entrada a lista de enteros
        lista = list(map(int, entrada.split(',')))
        
        # Calcular mayor suma consecutiva
        resultado = MayorSumaConsecutiva(lista)
        print(f"La mayor suma consecutiva es: {resultado}")

    except ValueError as ve:
        # Error en la conversión o en la validación de tamaño
        print(f"ERROR: {ve}")
    except Exception as e:
        # Cualquier otro error inesperado
        print(f"ERROR inesperado: {e}")
