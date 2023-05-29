peso = float (input("Proporciona tu peso en kg:"))
estatura = float (input("Proporciona tu estatuta en mts:"))

imc = round(peso / estatura**2,2)

print(f"Tu IMC es: {imc}")
if imc >= 30.00:
    print("Tu nivel de peso es obeso")
elif imc >= 25.00:
    print("Tu nivel de peso es sobrepeso")
elif imc >= 18.5:
    print("Tu nivel de peso es normal")
else :
    print("Tu nivel de peso es bajo")

'''
#pon tu calificacion, si tienes de 0 a 60, si tienes de 61 a 70 aprobado, si tienes de 71 a 80 bueno, 
#si tienes de 81 a 90 muy bueno, si tienes de 91 a 100 excelente.

calificacion=int(input('cual es tu calificacion'))
if calificacion<=100 and calificacion>90:
    print('excelente')
elif calificacion <=91 and calificacion>80:
    print('muy bueno')
elif calificacion<=81 and calificacion>70:
    print('bueno')
elif calificacion<=71 and calificacion>=60:
    print('aprobado')
elif calificacion<60:
    print('reprobado')   
'''
