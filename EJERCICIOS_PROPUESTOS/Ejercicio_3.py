"""
3. Implemente un algoritmo que halle el número de disposiciones de las letras de un texto introducido. 
    Por ejemplo si el texto es TALLAHASSEE, el número de disposiciones de las letras son: formas 
"""


from itertools import permutations


texto = "TALLAHASSEE"

disposiciones = set(permutations(texto))


print("Cantidad de disposiciones:", len(disposiciones))