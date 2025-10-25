"""
5. En el algoritmo anterior que el usuario especifique qué letra del texto introducido no debe estar consecutiva 

"""


from itertools import permutations # Importa la función permutations del módulo itertools


texto = "TALLAHASSEE"  # Texto de ejemplo

disposiciones = set(permutations(texto)) # Genera todas las disposiciones posibles y elimina duplicados usando un conjunto

# Filtra las disposiciones para eliminar aquellas con letras A adyacentes, para ello convierte cada tupla en cadena y verifica la ausencia de 'AA'
letra_no_consecutiva = input("Ingrese la letra que no debe estar consecutiva: ")

disposiciones = [d for d in disposiciones if letra_no_consecutiva*2 not in ''.join(d)]

print("Cantidad de disposiciones sin letras", letra_no_consecutiva, "adyacentes:", len(disposiciones)) # Imprime la cantidad de disposiciones únicas encontradas