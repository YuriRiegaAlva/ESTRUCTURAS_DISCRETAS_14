#3. comparacion algoritmos con y sin itertools
import math
def combina(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))  # Calcula C(n,r) = n! / (r! * (n-r)!)
def combinacion(r, n):
    s = [0]  # Lista auxiliar con 0 inicial para indexar desde posición 1
    for i in range(1, r+1):  # Recorre desde 1 hasta r
        s.append(i)  # Agrega i a la lista para formar [0, 1, 2, ..., r]
    print(s[1:r+1],end=" ")  # Imprime la primera combinación [1, 2, ..., r]
    for i in range(2, combina(n, r)+1):  # Itera desde la 2da hasta la última combinación
        m = r  # Inicializa m en la última posición de la combinación
        val_min = n  # Inicializa val_min con el valor máximo posible
        while (s[m] == val_min):  # Busca desde la derecha el primer elemento que puede incrementarse
            m = m - 1  # Retrocede una posición a la izquierda
            val_min = val_min - 1  # Decrementa el valor máximo permitido para esa posición
        s[m] = s[m] + 1  # Incrementa en 1 el elemento que puede crecer
        for j in range(m+1, r+1):  # Recorre las posiciones a la derecha de m
            s[j] = s[j-1] + 1  # Asigna valores consecutivos: s[j-1]+1
        print(s[1:r+1],end=" ")  # Imprime la nueva combinación generada

#3.1. Combinaciones cuando n = 6 y r = 3.
print("Combinaciones sin itertools cuando n=6 y r=3:")
combinacion(3, 6)
print("\nCombinaciones con itertools cuando n=6 y r=3:")
import itertools
print(list(itertools.combinations(range(1, 7), 3)))
#3.2. Combinaciones cuando n = 6 y r = 2.
print("Combinaciones sin itertools cuando n=6 y r=2:")
combinacion(2, 6)
print("\nCombinaciones con itertools cuando n=6 y r=2:")
import itertools
print(list(itertools.combinations(range(1, 7), 2)))
#3.3. Combinaciones cuando n = 7 y r = 5
print("Combinaciones sin itertools cuando n=7 y r=5:")
combinacion(5, 7)
print("\nCombinaciones con itertools cuando n=7 y r=5:")
import itertools
print(list(itertools.combinations(range(1, 8), 5)))


