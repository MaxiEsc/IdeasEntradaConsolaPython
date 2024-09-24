#primer programa con un modulo importado con valores aleatorios

import random
from random import randint

#Generar un numero aleatorio entre 1 y 10
numero = randint(1,10)
print(f'Numero aleatorio entre 1 y 10: {numero}')

#Simular un lanzamoiento de dado
dado = random.randint(1,6)
print(f'resultado del lanzamiento de dado: {dado}')