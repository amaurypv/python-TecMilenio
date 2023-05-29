'''listas 
las listas son una serie de datos que se pueden definir entre corchetes'''
diasSemana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
'''y se pueden acceder a los datos de la lista mediante su indice'''
print(diasSemana[0]) #imprime lunes
print(diasSemana[1]) #imprime martes
'''tambien se pueden asignar valores a las listas mediante su indice'''
diasSemana[3]='juebebes'
print(diasSemana) # imprime ['lunes', 'martes', 'miercoles', 'juebebes', 'viernes', 'sabado', 'domingo']
#cambio el dia jueves por juebebes
'''existen mas metodos que se aplican a las listas como:'''
diasSemana.append("lunes") #agrega un elemento al final de la lista
print(diasSemana) #imprime ['lunes', 'martes', 'miercoles', 'juebebes', 'viernes', 'sabado', 'domingo', 'lunes']
diasSemana.insert(0,"domingo") #agrega un elemento en la posicion 0
#para saber cuantos elementos hay en la lista se puede usar la funcion len
print(len(diasSemana)) #imprime 8
#para eliminar el ultimo elemento de la lista se puede usar la funcion pop
diasSemana.pop() #elimina el ultimo elemento de la lista
print(diasSemana) #imprime ['lunes', 'martes', 'miercoles', 'juebebes', 'viernes', 'sabado', 'domingo']
#remove() sirve para eliminar un elemento de la lista
diasSemana.remove("domingo")
print(diasSemana) #imprime ['lunes', 'martes', 'miercoles', 'juebebes', 'viernes', 'sabado']
#reverse() sirve para invertir los elementos de una lista
diasSemana.reverse()
print(diasSemana) #imprime ['sabado', 'viernes', 'juebebes', 'miercoles', 'martes', 'lunes']
#sort() sirve para ordenar los elementos de una lista
diasSemana.sort()   
print(diasSemana) #imprime ['lunes', 'martes', 'miercoles', 'juebebes', 'sabado', 'viernes']
#join() sirve para unir elementos de una lista
print(",".join(diasSemana)) #imprime lunes,martes,miercoles,juebebes,sabado,viernes
#split() sirve para dividir elementos de una lista
print(diasSemana.split(",")) #imprime ['lunes', 'martes', 'miercoles', 'juebebes', 'sabado', 'viernes']

'''tuplas
las tuplas solo se pueden definir entre parentesis y se pueden acceder a los datos de la tupla mediante su indice
'''
tupla=(1,2,3,4,5)
#para acceder a un valor de las tuplas
print(tupla[0]) #imprime 1
''' diccionarios
se definen con llaves, y tienen dos datos, llave y valor, sus valores se separan con comas'''
diccionario={"nombre":"juan","edad":20}
#para acceder a un valor  de los diccionarios se usa la llave.
print(diccionario["nombre"]) #imprime juan
#se pueden modificar los valores de los diccionarios
diccionario["nombre"]="pedro"
print(diccionario)
#se pueden agregar nuevos valores a los diccionarios
diccionario["apellido"]="perez"
print(diccionario)
#se pueden eliminar valores de los diccionarios
del diccionario["apellido"]
print(diccionario)
''' conjuntos 
los conjuntos se definen entre llaves y se pueden acceder a los datos mediante su indice'''
conjunto={1,2,3,4,5}
#para acceder a un valor de los conjuntos se usa su indice 
print(conjunto[0]) #imprime 1

#para formar funciones
def saludo(nombre):
    print(f'hola, mi nombre es {nombre}')

saludo('amaury')
#funciones lambda
suma=lambda x,y: x+y
print(suma(2,3)) #imprime 5

for i in range(1,11):
    for j in range(1,11):
        print(f'{i} * {j}= {i*j}')

letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


