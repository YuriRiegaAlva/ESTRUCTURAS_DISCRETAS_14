"""
6. Implemente un algoritmo para calcular las combinaciones de n objetos tomados de r en r, con repeticiones: C(n+r-1, r)

    Formula de combinaciones con repetición:
        C(n+r-1, r) = (n+r-1)! / (r! * (n-1)!)

"""


def comb_rep(lista,r): # Función para generar combinaciones con repetición
    if r <= 1: # Caso base
        return [[x] for x in lista]  # Retorna listas individuales
    
    combs=[] # Lista para almacenar combinaciones
 
    for i in range(len(lista)): # Itera sobre los elementos de la lista 
        t_1= lista[i]  #Toma el elemento actual
        t_rest= lista[i:] # Resto de la lista incluyendo el elemento actual, para permitir repetición
        for c in comb_rep(t_rest,r-1):  # Llama recursivamente para obtener combinaciones del resto
            combs.append([t_1] + c)  # Agrega la combinación actual a la lista

    return combs # Retorna todas las combinaciones generadas


r=-1 # Inicializa r con un valor inválido
n = int(input("Ingrese n: ")) # Solicita al usuario el valor de n

while r <= 0 or r >= n: # Valida que r esté en el rango correcto
    r = int(input("Ingrese r: ")) # Solicita al usuario el valor de r


opc = "" # Inicializa la opción del usuario

while opc != "a" and opc != "b": # Valida la opción ingresada
    opc = input("Ingrese \n(a) si quiere mostrar todas la combinaciones. \n(b) La cantidad de combinaciones \n -> ") 

if opc == "a": # Muestra todas las combinaciones con repetición
    for i in comb_rep([x for x in range(n)],r): # Itera sobre cada combinación con repetición generada
        print(i)
elif opc == "b" : # Muestra la cantidad de combinaciones con repetición
    print(len(comb_rep([x for x in range(n)],r))) # Imprime la cantidad de combinaciones con repetición generadas