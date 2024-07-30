"""#  Conjuntos / set 
 conjunto = {1,2,3,4,5}
otro_conjunto = {"hola", "como", "estas"}
conjunto_vacio = set()

 # son heterogeneos 
 variable1 = "esto es una variable"
datos = {1,-5,123.57, "una cadena", "otro string", variable1}
print(datos) """

# puede incluir numeros , variables , strings o tuplas . 
# pero no puede incluir objetos como listas , diccionarios incluso otros conjuntos 

""" lista = ({1,2,3,4,5,6})
print(lista)
print(set([1,1,2,2,2,3,3,4,4,]))"""

#funciones integradas en set/conjuntos
""" numeros = {1,2,3,4}
numeros.add(5)
print(numeros) """

#UPDATE
numeros = {1,2,3,4}
numeros.update([5,6,4,7,8])
print(numeros)

#LEN
print(len(numeros))

#discard
numeros.discard(2)
print(numeros)

#remove
#remove y discard funcionan de igual manera , a diferencia que en discard si el elemento pasado como argumento no existe , lo ignora . en cambio con remove nos devolvera un error 


#in
print(2 in numeros)
print (3 in numeros)

#clear 

"""numeros.clear()"""

#pop (retornan un elemnto en forma aleatoria )
"""numeros1 = {1,2,3,4,5,6}
while numeros1: 
   print("se esta borrando:", numeros1.pop())"""

#   diccionario / dict 

colores = {"amarillo": "yellow", "azul": "blue","rojo": "red"}
print(colores["amarillo"])
colores["amarillo"] = "white"
print(colores)

edades = {"juan": 26, "esteban": 35, "maria": 29}
edades["juan"] +=5
edades["maria"] *=2
print(edades)

#add
numeros3 = {"uno": 1, "dos": 2}
numeros3["cinco"]= 5
print(numeros3)

#update
numeros3.update({"seis":6})
print(numeros3)

#len
print(len(numeros3))

#del
del numeros3["dos"]
print(numeros3)

#in
print("uno" in numeros3 )

#clear
"""numeros3.clear()"""

#pop
print(numeros3.pop("uno"))








