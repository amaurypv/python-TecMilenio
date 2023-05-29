# el bucle while se usa cuando no sabemos cuantas veces se va a repetir un bloque de codigo
#dar un ejemplo en el que se usa el bucle while

#definir una lista que tenga los planetas del sistema solar
planetas=["mercurio","venus","tierra","marte","jupiter","saturno","urano","neptuno"]
#crear un bucle while que recorra la lista de planetas y que imprima cada uno de ellos
while planetas:
    planeta=planetas.pop() #para que el metodo no se cicle se tiene que eliminar el ultimo elemento de la lista
    print(f'{planeta} es un planeta') #la letra f se usa para concatenar los strings con variables

planetas2=['mercurio','venus','tierra','marte','jupiter','saturno','urano','neptuno']
#para agregar un elemento a la lista se usa el metodo append
planetas2.append('pluton')
print(planetas2)
#para saber cuantos elementos tiene una lista se usa el metodo len
planetas2.pop()
print(len(planetas2)) #imprime 9 
#definir una lista con las gravedades de cada planeta 
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
#calcular cuanto pesaria un autobus que en tierra pesa 12.5 toneladas en cada planeta. 
n=0 #se define una variable en cero que es la recorrera los planetas. 
for i in gravity_on_planets: #se hace un bucle por la lista de las gravedades
    peso=12.5*i #se multiplica el peso del camion por cada gravedad 
    print(f'en {planetas2[n]} el peso del autobus es de {peso} kgs') #se imprime     
    n+=1 #se amenta n en uno cada vez que se ejecute el bucle para que avance en cada planeta. 
#para conocer el mayor y el menor de una lista se una min y max
menor=min(gravity_on_planets)
mayor=max(gravity_on_planets)

print(f'el planeta en el que menos pesa el autobus es {planetas2[gravity_on_planets.index(menor)]} con una gravedad de {menor}')
print(f'el planeta en el que mas pesa el autobus es {planetas2[gravity_on_planets.index(mayor)]}con una gravedad de {mayor}')

#para cortar listas se utiliza [ini:termina +1]
#ejemplo para seleccionar los tres primeros elementos de la lista:
tresPrimeros=planetas2[0:3] #imprime ['mercurio', 'venus', 'tierra']
#para imprimir de la posición 3 en adelante (incluyendo la posición)
ultimosTres=planetas2[3:] #imprime ['marte', 'jupiter', 'saturno', 'urano', 'neptuno']

#para ordenar una lista se usa .sort()
azar=[4,56,7,2,5,7,8,2,39,7]
azar.sort() #imprime [2, 2, 4, 5, 7, 7, 7, 8, 39, 56]
print(azar)
azar.sort(reverse=True) #imprime [56, 39, 8, 7, 7, 7, 5, 4, 2, 2]
