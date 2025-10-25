#1.1   C(10,8)= 10!/(10-8)!*8! = 45
import itertools #Se importa la herramienta itertools
preguntas=[x for x in range(1,11)] #Se crea una lista simulando las 10 preguntas
print(len(list(itertools.combinations(preguntas,8)))) #Se llama a la funcion para que encuentre la cantidad de combinaciones posibles

#1.2  C(5,4)= 5!/(5-4)!*4!=5 ;   C(5,4)*C(5,4) = 25
import itertools #Se importa la herramienta itertools
preguntas_5=[x for x in range(1,6)] #Se crea una lista simulando ahora 5 preguntas de las 10
combinatoria=(len(list(itertools.combinations(preguntas_5,4)))) #Se llama a la funcion para que encuentre la cantidad de combinaciones posibles
comb_total=combinatoria*combinatoria #se halla multiplicando la misma combinatoria debido a que es el mismo caso
print(comb_total) #Se imrprime la cantidad total

#1.3 C(6,1)=6!/(6-1)!*1!=6 o C(6,5)=6!/(6-5)!*5!=6
"""Se usan 6 elementos ya que estamos tomando en cuenta los tres "0" como un bloque haciendo
   que hayan solo 6 elementos de los 8 digitos de la cadena de bits y se puede hacer de ambas
   formas, tomando el bloque de tres "0" o tomando los cinco "1"."""
import itertools #Se importa la herramienta itertools
digitos=[x for x in range(1,7)] #Se crea una lista simulando ahora 5 preguntas de las 10
print(len(list(itertools.combinations(digitos,5)))) #Se llama a la funcion para que encuentre la cantidad de combinaciones posibles

#1.4 C(4,3)=4!/(4-3)!*3!=4; por lo tanto deberian ser 4 las combinaciones mostradas
import itertools #Se importa la herramienta itertools
X=["a","b","c","d"] #Se crea una lista con los elementos a combinar
print("Las combinaciones posibles de la lista de elementos son: \n",list(itertools.combinations(X,3))) #Se llama a la funcion para muestre todas las combinaciones posibles

#1.5 C(10,3)=120;C(10,2)=45;C(10,1)=10;C(10,0)=1; total=176
"""Se halla la cantidad de combinaciones posibles cuando se lanzan 10 monedas y se quiere saber
   la cantidad de combinaciones posibles cuando salen exactamente 3 caras, 2 caras, 1 cara y 0 caras."""
import itertools #Se importa la herramienta itertools
moneda=[x for x in range(1,11)] #Se crea una lista simulando el lanzamiento de las  10 monedas
comb_total=0 #Se inicializa la variable que llevara el conteo total de combinaciones
for i in range(4): #Se itera desde 0 hasta 3 para hallar las combinaciones de cada caso
    comb=len(list(itertools.combinations(moneda,i))) #Se halla la cantidad de combinaciones posibles para el caso actual
    comb_total= comb_total+comb #Se va sumando al conteo total
    if i == 3: #Si se esta en el caso de 3 caras
        print("Combinaciones cuando son exactamente 3 caras:",comb)
print("Combinaciones cuando a los sumo son 3 caras:",comb_total)

#1.6 CR(10,5)=C(10+5-1,5)=C(14,5)=2002; CR(5,5)=C(5+5-1,5)=C(9,5)=126; CR(8,5)=C(8+5-1,5)=C(12,5)=792
import itertools #Se importa la herramienta itertools
niños=5 #Se crea una lista simulando los niños a repartir los dulces
dulces=[x for x in range(1,11)] #Se define la cantidad de dulces a repartir
print("Combinaciones sin resctriccion de 10 dulces entre 5 niños:",len(list(itertools.combinations_with_replacement(moneda,niños)))) #Se halla la combinatoria con repeticion para el primer caso
print("Combinaciones que cada niño reciba al menos 1 dulce:",len(list(itertools.combinations_with_replacement(dulces[5:],niños)))) #Se halla la combinatoria con repeticion para el segundo caso
print("Combinaciones que el mayor reciba al menos 2 dulces:",len(list(itertools.combinations_with_replacement(dulces[2:],niños)))) #Se halla la combinatoria con repeticion para el tercer caso
