base1 = int(input("Escriba la base del numero a convertir: "))
base2 = int(input("EScriba la base a convertir del numero: "))
unidades = int(input("Escriba la cantidad de unidades del número: "))
print("\n -- ESCRIBA EL NUMERO DE DERECHA A IZQUIERDA --\n\nTENGA EN CUENTA:")
print("1=1    A=10 \n2=2    B=11 \n3=3    C=12 \n4=4    D=13 \n5=5    E=14 \n6=6    F=15 \n7=7 \n8=8 \n9=9\n")

arreglo = []
bases = []

i=0
j=0
k=0

#Guarda el número unidad por unidad
while i < unidades: 
  i+=1
  num = int(input("_"))
  arreglo.append(num)

#Bases elevadas hasta el exponente máximo igual a unidades
while j < unidades:
  bases.append(pow(base1, j))
  j+=1
  
#Multiplicación de arreglo(unidades del número) por bases(bases con potencia)
# mult funciona similar a una lista
mult = list(map(lambda x, y: x*y, arreglo, bases))

#Creación del decimal a través de la suma de la multiplicación
decimal = 0
for d in mult:
  decimal+=d

#Código ascii no extendido hasta 128
if decimal <= 128:
  print("\nEl número en código ASCII representa el caracter:",chr(decimal))
else:
  print("\nEl número es superior a 128")

#Resto de decimal para formar el número binario
decimal2 = decimal
binario=""
while decimal2>0:
  bins = decimal2 % 2
  binario = str(bins)+binario
  decimal2 = int(decimal2/2)
print("BINARIO:",binario)


#respuesta en string para poder agregar las letras
respuesta = ""
while decimal > 0:
  aux=decimal % base2

  if aux<10:
    #str para concatenar int con string
    respuesta = str(aux)+respuesta
  if aux==10:
    respuesta = "A"+respuesta
  if aux==11:
    respuesta = "B"+respuesta
  if aux==12:
    respuesta = "C"+respuesta
  if aux==13:
    respuesta = "D"+respuesta
  if aux==14:
    respuesta = "E"+respuesta
  if aux==15:
    respuesta = "D"+respuesta

  decimal = int(decimal/base2)

print("La conversión del número de base ",str(base1)," a base ",str(base2)," es: ",respuesta,"\n")