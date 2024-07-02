#longitud de string 
# Funcion LEN 

esto_es_un_string ="hola soy un string"

print(len(esto_es_un_string))

string1 = "     "
print(len(string1))
#Rebanar un String
#funcion SLICING [Inicio:fin:paso]
#Inicio va a ser el primer caracter de la cadena que queremos rebanar 
#fin vas a ser el indice del ultimo caracter no incluido de la cadena que queremos rebanar 
#paso: indica cada cuntos caracteres vamos a seleccionar entre las posiciones de inicio y fin 

saludo = "hola, como estas?"
print (saludo)
saludo[0:3:1]
print(saludo[0:3:1])
print(saludo[0:3:2])
print(saludo[0:3:3])


palabra = "Pithon"
print(palabra)

print(palabra[1])


#los string son inmutables , no se pueden sustituir (reemplazar)

palabra = palabra[0:1] +"y"+ palabra[2:]
print(palabra) 

### Listas y tuplas 

mi_lista = [-11,20,3,41]
print(mi_lista)


otra_lista = ["hola","como","estas","?"]
variable_1 = "una variable"

listita = [1, -10, 132.5, "un string", "otro string", variable_1]
print(listita)


print(listita[0])

print(listita[-1])
print(listita[-2:])

listita + [otra_lista, "algo random"]
print(listita + [otra_lista, "algo random"])

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros+[11,12,13,14,15,16])

numeros = [0,2,4,5,10,15,20]
numeros[3] = 8
print(numeros)
# siempre toma los ultimos valores actualizados segun la lista (por ejemplo aca modificamos la variable y cambiaron los numeros )
#las listas si son mutables ( si podemos modificar )

letras = ["a","b","c","d"]
letras[:3] = ["A","B","C"]
print(letras)

"""equipos = ["moron" , "river", "boca"]
print(equipos)
equipos = []
print(equipos)"""

#con corchetes accedemos al indice , funcion con ()

#funcion append
#nos permite agregar un nuevo item al final de una lista . se escribe mi_lista.append(item_a_agregar) 
numeros = [1,2,3,4,5,6]
numeros.append(7)
print(numeros)
numeros.append(7*8)
print(numeros)


#tambien podemos utilizar la funcion LEN(la_lista_a_consultar_su_longitud)  en fin , suma la cantidad de items de una lista ):
print(len(numeros))
      


#funcion pop 
#es todo lo contrario a append , por que va a eliminar el ultimo item de una lista . - pop.()

"""equipos = ["moron" , "river", "boca"]
equipos.pop()

print(equipos)
"""
#elimina por defecto el último elemento de la lista, pero si se pasa como parámetro un índice permite borrar elementos diferentes al último
#####si ingreso dentro del parentesis una posicion segun indice ,pop elimina el indice correspondiente  
equipos = [1,2,3,4]
equipos.pop(2)
print(equipos)


#funcion count 
#devolverá el recuento de un elemento determinado en una lista o cadena
#se escribe la _lista_a_contar.count

numeros_varios = [1,2,3,4,5,6,44,89,52,4,5]
print(numeros_varios.count(5))
#en este caso el item 5 se repite 2 veces 

#index
# busca el item y nos devuelve en que indice esta . se escribe la_lista.index(lo que queremos buscar) 

numeros_varios = [1,2,3,4,5,6,44,89,52,4,5]
print(numeros_varios.index(52))

##___ tuplas 
#son similares a las listas , la gran dif es que son inmutables 
#es un conjunto ordenado e inmutable de elementos del mismo o diferente tipo.se representan escribiendo los elementos entre paréntesis y separados por comas.Una tupla puede no contener ningún elemento, es decir, ser una tupla vacía 
#mi_tupla(1,2,3,4,5)
#no se puede .append 

mi_tupla = (1,2,3,4,5)
print(mi_tupla)

tupla = (1,)
print(tupla)

otra_tupla = (1,5,-100,"cadena", "otra cadena/string", mi_tupla)
print(otra_tupla)
print(otra_tupla[-1])

print(otra_tupla[2:])
print(len(otra_tupla))
print(otra_tupla.index(5))
print(otra_tupla.count(1))










