import random
letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numeros=['0','1','2','3','4','5','6','7','8','9']
simbolos=['!','#','$','%','&','/','(',')','*','+']

azar=random.randint(0,len(letras)-1)
numlet=int(input('Cuantas letras quieres que tenga tu contraseña? '))
numnum=int(input('Cuantos numeros quieres que tenga tu contraseña? '))
numsim=int(input('Cuantos simbolos quieres que tenga tu contraseña? '))
password=[]
for i in range(numlet):
    azar=random.randint(0,len(letras)-1)
    password.append(letras[azar])

for j in range(numnum):
    azar=random.randint(0,len(numeros)-1)
    password.append(numeros[azar])

for k in range(numsim):
    azar=random.randint(0,len(simbolos)-1)
    password.append(simbolos[azar])

#para revolver el contenido de la lista password
random.shuffle(password)  
print(f'tu nueva contraseña es:{"".join(password)}')   
    