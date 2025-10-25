"""
 Implemente un algoritmo para calcular las combinaciones r de n elementos C(n,r) siendo n y r números enteros donde 0 ≤ r ≤ n.
"""


def comb(lista,r): # Función para generar combinaciones
    if r <= 1: # Caso base
        return [[x] for x in lista] # Retorna listas individuales
    
    combs=[] # Lista para almacenar combinaciones

    for i in range(len(lista)): # Itera sobre los elementos de la lista
        t_1= lista[i] # Toma el elemento actual
        t_rest= lista[i+1:] # Resto de la lista sin el elemento actual 
        for c in comb(t_rest,r-1): # Llama recursivamente para obtener combinaciones del resto
            combs.append([t_1] + c) # Agrega la combinación actual a la lista

    return combs # Retorna todas las combinaciones generadas

r=-1 # Inicializa r con un valor inválido
n = int(input("Ingrese n: ")) # Solicita al usuario el valor de n

while r <= 0 or r >= n: # Valida que r esté en el rango correcto
    r = int(input("Ingrese r: ")) # Solicita al usuario el valor de r


opc = "" # Inicializa la opción del usuario

while opc != "a" and opc != "b": # Valida la opción ingresada
    opc = input("Ingrese \n(a) si quiere mostrar todas la combinaciones. \n(b) La cantidad de combinaciones \n -> ") 

if opc == "a": # Muestra todas las combinaciones
    for i in comb([x for x in range(n)],r): # Itera sobre cada combinación generada
        print(i)
elif opc == "b" : # Muestra la cantidad de combinaciones
    print(len(comb([x for x in range(n)],r))) # Imprime la cantidad de combinaciones generadas