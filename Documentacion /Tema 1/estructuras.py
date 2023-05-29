#estructuras de python 
lista=['lunes','martes','miercoles','jueves','viernes']
#las listas son dinamicas, es decir se pueden quitar o agrgar elementos. 
#para agregar un elemento se utiliza .append()
lista.append('sabado')
#se usa tambien extend() pero para eso se necesitan corchetes
lista.extend(['domingo','lunes'])
lista.pop() #para eliminar el ultimo elemento de la lista. 
lista.remove('lunes') #remove tenemos que decirle que elemento queremos eliminar
print(lista) #imprime ['martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
print(len(lista))

#las tuplas son inmutables, es decir, no se pueden modificar. 
tupla=('lunes','martes','miercoles','jueves','viernes')
print(tupla) #imprime ('lunes', 'martes', 'miercoles', 'jueves', 'viernes')
'''los diccionarios son dinamicos, es decir, se pueden agregar o eliminar elementos. 
se componen por  llaves y valores.
'''
diccionario={'nombre':'juan','edad':23,'ciudad':'medellin'}
#para acceder a un elemento se utiliza la llave
print(diccionario['nombre'])
#para agregar un elemento se utiliza la llave
diccionario['pais']='colombia'
#para eliminar un elemento se utiliza la llave
del diccionario['pais']
diccionario['genero']='masculino'
print(diccionario)
#conjuntos o sets 
#los conjuntos son inmutables, es decir, no se pueden modificar.

