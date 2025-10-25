"""
4. Implemente un algoritmo que halle el número de disposiciones de las letras de TALLAHASSEE, que no tengan letras A adyacentes

"""

from itertools import permutations # Importa la función permutations del módulo itertools


texto = "TALLAHASSEE"  # Texto de ejemplo

disposiciones = set(permutations(texto)) # Genera todas las disposiciones posibles y elimina duplicados usando un conjunto

# Filtra las disposiciones para eliminar aquellas con letras A adyacentes
disposiciones = [d for d in disposiciones if 'AA' not in d]

print("Cantidad de disposiciones:", len(disposiciones)) # Imprime la cantidad de disposiciones únicas encontradas