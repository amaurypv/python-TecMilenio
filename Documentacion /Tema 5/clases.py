'''#definir una clase llamada auto 
class Auto:
    def __init__(self, marca, modelo, color): #se pone def __init__ y siempre seguido de self 
        self.marca = marca
        self.modelo = modelo
        self.color = color

#definir una clase de perros
class perro:
    def __init__(self, nombre, raza, color): # una clase se inicia siempre con def __init__(self)
        self.nombre = nombre #se define las variables siempre con self.nombre
        self.raza = raza
        self.color = color
        #definir metodos
    def presentarse(self):
        print(f"mi perro se llama {self.nombre} y es de raza {self.raza} y de color {self.color}")

#a partir de la clase perro crear un objeto 
mi_perro = perro("Puppy", "french", "blanco")
perro_2 = perro("golliat", "pitbull", "negro")
perro_3 = perro("sanson", "golden retriever", "canela")
perro_4 =perro('kalizi','shitzu','pinto')

perro_2.presentarse()
perro_3.presentarse()
perro_4.presentarse()'''

#crear un clase que se llame cubo 

class clase_cubo:
    def __init__(self,color,textura):
        self.color=color
        self.textura=textura
    def mostrar_caracteristicas(self):
        print(f"el color del cubo es {self.color} y es de {self.textura}")
    def set_textura(self,textura_nueva):
        self.textura=textura_nueva
    def get_color(self):   #este es un getter (obtienes el color)
        return self.color
    def set_color(self,color_nuevo):
        self.color=color_nuevo

#se define una variable cubo a partir de la clase_cubo
cubo=clase_cubo('azul','madera')

cubo.mostrar_caracteristicas()
#para cambiar el color de un objeto 
cubo.set_color('rojo')
cubo.mostrar_caracteristicas()
#para obtener el color de un objeto
color_cubo=cubo.get_color()
print(color_cubo)
#existe otra forma de obtener el color de un objeto
color2=cubo.color
print(color2)


print('vamos a definir un cubo')
colornuevo=input('\n que color quieres el cubo')
texturanueva=input('\nde que textura quieres el cubo?')
cubo3=clase_cubo(colornuevo,texturanueva)
opcion=''
while opcion!='s':
    print('\n opciones para  trabajar el cubo')
    print('a. cambiar de color')
    print('b. cambiar de textura')
    print('c. mostrar el cubo')
    print('s. salir')
    opcion=input('selecciona una opcion')
    if opcion=='a':
        color4=input('que color quieres?')
        cubo3.set_color(color4)
    elif opcion=='b':
        textura4=input('que textura quieres poner?')
        cubo3.set_textura(textura4)
    elif(opcion=='c'):
        cubo3.mostrar_caracteristicas()
