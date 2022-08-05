print ("Ingrese el numero de partidos ganados: ")
PG = int( input())
print ("Ingrese el numero de partidos perdidos: ")
PP = int( input())
print ("Ingrese el numero de partidos empatados: ")
PE = int( input())

PPG = PG*3
PPP = PP*1
PPE = PE*0

TOT = PPG+PPP+PPE 

print ("La cantidad de puntos en el torneo es de ",TOT)