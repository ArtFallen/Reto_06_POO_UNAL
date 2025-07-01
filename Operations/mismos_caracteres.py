# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 00:25:58 2025
@author: Arthur
@version: 1.0.0
"""

from collections import defaultdict

def MismosCaracteres(lista: list) -> list:
    """
    Retorna los elementos de la lista que tienen los mismos caracteres (anagramas).

    Parámetros:
    lista (list[str]): Lista de cadenas de texto a evaluar.

    Retorna:
    list[str]: Lista con las palabras que tienen al menos un anagrama en la lista original.
    """
    if not lista or not all(isinstance(p, str) for p in lista):
        raise ValueError("La lista debe contener únicamente cadenas de texto no vacías.")

    grupos = defaultdict(list)

    for palabra in lista:
        clave = ''.join(sorted(palabra.strip().lower()))  # estandarizar espacios y mayúsculas
        grupos[clave].append(palabra.strip())

    resultado = []
    for grupo in grupos.values():
        if len(grupo) > 1:
            resultado.extend(grupo)

    return resultado

if __name__ == "__main__":
    entrada = input("Ingrese una lista de palabras (Ejemplo: hola, pero, huevo): ")
    try:
        lista = [pal.strip() for pal in entrada.split(',') if pal.strip()]
        resultado = MismosCaracteres(lista)
        if resultado:
            print("Estos son los elementos de la lista que tienen los mismos caracteres:")
            print(resultado)
        else:
            print("No se encontraron palabras con los mismos caracteres (anagramas).")

    except ValueError as ve:
        print(f"ERROR: {ve}")
    except Exception as e:
        print(f"ERROR inesperado: {e}")
