#vamos a generar un grafico a partir de la libreria matplotlib.
#primero importamos la libreria

import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,23,34,43,56]
plt.plot(x,y)
plt.xlabel("eje x") #xlabel sirve para generar el titulo del eje x
plt.ylabel("eje y") #ylabel sirve para generar el titulo del eje y
plt.title("grafico de prueba")  #.title  sirve para generar el titulo del grafico
plt.show()
#para ver el grafico en la pantalla es necesario ejecutar el comando


