#$Generador
from fun_random import numero

import random
from random import randint

nombre = input("¿Cual es tu nombre?: ")
apellido = input('¿Cual es tu apellido?: ')
anio_nacimiento = input('¿Cual es tu año de nacmiento (YYYY)?: ')
numero_randopm = str(randint(1000,9999))

id_unico = nombre[0:2].upper() + apellido[0:2].upper() + anio_nacimiento[len(anio_nacimiento)-2:len(anio_nacimiento)] + numero_randopm

print(f"Hola {nombre}")
print('\tTu nuevo número de identificacion (ID) generado por el sistema es: ')
print(f'\t{id_unico}\n\tFelicidades!')