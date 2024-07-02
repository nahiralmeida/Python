#___ OPERADORES 

#OPERANDO [operador] operando
#   -/*+
#operadores aritmeticos (+,-,*,/)
# expresiones aritmeticas : 2+2, 5-1 , -1*100 , 20/3
#expresiones algebraicas : radio * 3,14 (nota1+ nota2)/2

#tipo logico : BOOLEANO o binario 
# es el tipo de dato mas basico de la informacion racional y representa VERDADERO Y FALSO 

#no verdadero = falso (TRUE)
#no falso = verdadero (FALSE)


#operadores relacionales : son simbolos que se usan para comparar los valores . si el resultado de la comparacion es correcto , la expresion va a ser considerada TRUE , de lo contrario sera False 

print(1+1 == 3)

# IGUALDAD 
# EL oprerador de igualdad sirve para preguntarle al programa si ambos operandos son iguales . 
#nos va a devolver TRUE si son iguales , y False si son distintos 
#ESTE OPERADOR SE ESCRIBE CON DOS SIGNOS IGUAL (==)

#ejemplo 

a = 3
print(a == 3)

print (a !=3)

#desigualdad o distinto 
#el operador distinto sirve para preguntarle a nuestro programa si ambos operandos son distintos 
#va a devolver TRUE si son distintos , False si son iguales 
#este operador se escribe con un signo de exclamacion y un signo de igual (!=)

#menor que 
#sirve para preguntar a nuestro programa si el primer operando es menor que el segundo operando 
# si el primero es menor TRUE , si el primero es mayor FALSE 
# 7 < 3 
print (7<3)

#menor igual que 
# el operador MENOR IGUAL QUE sirve para preguntar si el primer operando es menor que el segundo operando o si ambos son iguales 
# TRUE  si el primero es menor o igual al segundo , y FALSE si el primero es mayor al segundo 
# este operador se escribe con un signo menor que y un igual (<=)

print(7<=3)
print(10<=10)

#MAYOR QUE 
#el operador MAYOR IGUAL QUE sirve para preguntar si el primer operando es mayor que el segundo operando 
# TRUE si el primero es mayor al segundo , y FALSE si el primero es menor al segundo 
#(>)

print(7>6)
print(1>2)
print(7>=3)
print(10>=10)

#podemos hacer operaciones relacionales en string inclusive 

print("hola" =="hola")

b = "hola"
print(b[0] == "h")
#en este caso fue si la variable "b" indicando el indice [0] es igual a "h"

print(b[1] == "o")

print(10>= 2*4)
print(33/3 == 11)

print(True*5)

#_____operadores logicos
# NOT es la negacion , NO . Solo afecta a los tipos logicos TRUE Y FALSE , y solo requiere un oeprando en una expresion 
#
print(not True == False)


#Conjunción y Disyunción
#Conjunción viene de conjunto, agrupa uniendo
#Disyunción viene de disyunto, agrupa separando.

#AND  es conocido como el Y
#Va a unir una o varias sentencias logicas.
#Verdadero Y Verdadero

print ( 2> 1 and 5 > 2) 
print( 5> 25 and 20<1)


#True AND True - True
#True AND False - False
#False AND False - False
#False and True - False

#OR es O en ingles.
#Es Disyunción (separa)
# Si le pregunto a python por dos afirmaciones y al menos una es TRUE, python me va a decir que la afirmación es TRUE

print(2>1 or 5>2)
print(5<20 or 20<1)

# True o True - True
# True o False - True 
# False o True - True
# False o False - False 




#Ejercicio Mental Expresiones
# not False - verdadero
# not 3 == 5 - verdadero
# 33 /3 == 11 and 5>2 - verdadero
#True or False - verdadero
# True*5 == 2.5*2 or 123>= 23 - verdadero
# 12> 7 and True < False - falso

#normas de precedencia 
#1. TERMINOS ENTRE PARENTESIS 
#2. POTENCIACION Y RAICES 
#3. MULTIPLICACION Y DIVISION 
#4. SUMA Y RESTA 
 
d = 15
e = 12
print(d**e / 3 **e /e *d >= 15 and not (d%e **2) != 0)

nuemero = 15
a = 0
a +=1
print(a)

b = 50
b -=5
print(b)

c = 5
c *=10
c *=10
c *=10
c *=10

print(c)

# operador      ejemplo       equivalente 
# =              a = 2         a = 2
# +=             a += 2        a = a + 2
# -=             a -= 2        a = a - 2
# *=             a *= 2        a = a * 2
# /=             a /= 2        a = a / 2
# %=             a %= 2        a = a % 2
# **=            a **= 2       a = a ** 2







