saludo='hola mundo'
print(saludo)
print('bienvenido a la calculadora de propinas')
cuenta=float(input('cual fue el total de la cuenta?'))
propina=int(input('que porcentaje de propina quieres dejar'))
personas=int(input('entre cuantas personas se van a dividir la cuenta'))
total=cuenta+(cuenta*(propina/100))
porPersona=round(total/personas)
print(f'toca pagar {porPersona} por persona')
