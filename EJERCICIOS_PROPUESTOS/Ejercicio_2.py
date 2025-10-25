"""
2. Implemente un algoritmo que enumere todas las selecciones de tamaño 2 de los objetos 1,2,3,4,5,6 

"""

from itertools import combinations # Importa la función combinations del módulo itertools

objetos = [1, 2, 3, 4, 5, 6] # Lista de objetos

selecciones = list(combinations(objetos, 2)) # Genera todas las selecciones de tamaño 2

for i in selecciones: # Itera sobre cada selección generada
    print(i) # Imprime la selección actual
 
print("Cantidad de selecciones de tamaño 2:", len(selecciones)) # Imprime la cantidad total de selecciones generadas