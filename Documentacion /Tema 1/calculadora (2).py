'''#Entrada de datos y conversion de datos a tipos
print("Bienvenido a la calculculadora de propinas")
cuenta = float(input("¿Cual fue el monto de la cuenta?"))
porcentaje = int(input("¿Que porcentaje desea otorgar 10, 15, 30? "))
comensales = int(input("¿En cuantas personas se dividirá la cuenta?"))

#Variables y calculos
porcentaje_decimal = porcentaje / 100
propina = cuenta * porcentaje_decimal
total_cuenta = cuenta + propina
pago_x_persona = total_cuenta / comensales
pago_total = round(pago_x_persona, 2)

#Mensaje final con el resultado
print(f"Cada persona pagará: ${pago_total}")
'''
print(f'calculador de cuentas')
total= float(input('cuanto es el total de la cuenta'))
propina=int(input('que porcentaje desea agregar de propina?'))
personas=int(input('entre cuantas personas se va a dividir la cuenta'))

calc_propina=total*(propina/100)
total_mas_prop=total+calc_propina
por_persona=total_mas_prop/personas

print(f'el total a pagar por persona es de ${por_persona}')

