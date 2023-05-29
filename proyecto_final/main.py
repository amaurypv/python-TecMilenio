''' Crea una función cuyo objetivo sea imprimir en pantalla un menú que presente las 
siguientes opciones: 
a. Pedidos
b. Clientes
c. Menú
d. Salir'''

op=["a. Pedidos","b. Clientes","c. Menú",'d. Salir']
def opciones ():
    print('bienvenidos, nuestras opciones son las siguientes')
    for i in op:
        print(i)
opciones()
seleccion=input('por favor seleccione una opcion (a,b,c,d) ')
def ped ():
    prod=input('ingresa el nombre del producto ')
    precio=float(input('ingresa el precio del producto '))
    qty=int(input(f'cuantas {prod}s va a pedir '))
    print('El resumen de su pedido es el siguiente')
    print(f'usted pidió {qty} {prod}s a un precio de {precio}')    
    print ('total a pagar: $', precio*qty)

while  seleccion !='d':
    if seleccion =='a':
        ped()
        opciones()
    seleccion=input('por favor seleccione una opcion (a,b,c,d) ')