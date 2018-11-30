'''
Miguel Márquez
Caracas, 28-11-2018
VenCERT
El siguiente algoritmo, imprime números aleatorios sin repetir, en un rango del 1 al 7,   
'''
import random #llama la libreria random
from datetime import datetime #llama la libreria datetime

random.seed(datetime.now())#se carga la semilla de random con el reloj de la c

#se define la función aleatorizar
def aleatorizar():

	aleatorio= [-1,-1,-1,-1,-1,-1,-1]# inicializar arreglo (lista) con elemento -1
	contador= 1# incializar  contador en 1 para el primer bucle
 
	while contador <= 7:# el arreglo tendra soslo 7 elementos, asi que el bucle while solo hara 7 siclos

		contador2=0# se inicializa el segundo contador para el segundo bucle en 0
		rand=random.randint(1, 7)# numeros aleatorios del 1 al 7 se guardaran en una variable llamada "rand"	

		while contador2 < contador:#

			if aleatorio[contador2] == rand:

				contador -=1
				break
			else:
				if aleatorio[contador2] == -1:

					aleatorio[contador2]= rand
					print(rand)

				contador2+=1
			#if

		#while

		contador+=1

	#while

#funcion

aleatorizar()
