'''#Ejercicio 1
print((3+2)/(2*5)**2)'''

'''#Ejercicio 2
horas=float(input("ingrese la cantidad de horas: "))
costoHrs=float(input("Ingrese el costo por horas: "))
pago=horas*costoHrs
print("El precio a cobrar es de:",pago)'''

'''#Ejercicio 3
peso=float(input("Ingrese su peso: ",))
altura=float(input("Ingrese su altura: ",))
mc= (peso)/(altura*altura)
print("su IMC es de: ",mc)'''

'''#ejercicio 4
trompo = 30
yoyo = 20
cat = int(input("Digite la cantidad de trompos que compro: "))
cay = int(input("Digite la cantidad de yoyos que compro: "))
pt = cat*trompo
py = cay*yoyo
ppaq = pt+py
print("El peso total del paquete equivale a: ", ppaq, "Kg")

#Ejercicio 5
pan = 1000
PND = pan*0.40 #60% de descuento
cantidad = int(input("Ingrese la cantidad de panes que comprara: "))
total = cantidad * PND
print("El valor de los panes es de (60% descuento):",total,"colones")

#Ejercicio 6
inicial = int(input("Digite el monto inicial que va a ingresar"))
aumento1= (inicial/100)*4
año1 = inicial+aumento1
print ("Total del primer año: ",año1)
aumento2= (año1/100)*4
año2 = (año1+aumento2)
print ("Total en el segundo año: ",año2)
aumento3= (año2/100)*4
año3 = (año2+aumento3)
print ("Total en el tercer año: ",(round (año3,2)))

cantidad = float(input("Ingrese la cantidad que va a invertir"))
interes = float(input("Ingrese el porcentaje de intereses anual"))
años = int(input("Ingrese la cantidad de años"))
print ("Capital final: "+str(round(cantidad * (interes/100+1)**años,2100)))'''
