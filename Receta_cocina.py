#Creacion de programa que registra la receta

print("*** Receta de Cocina ***")
nombre_receta = input("Ingresa el nombre de la receta: ")
nombre_ingredientes = input("Ingresa la cantidad de ingredientes: ")
tiempo_preparacion = int(input("Ingresa el tiempo de preparacion (min): "))
dificultad = input("ingresa la dificultad para realizar este plato: ")
print('___'* 15)
print(f'El nombre del plato de esta receta es: {nombre_receta}')
print(f'Lista de ingredientes: {nombre_ingredientes}')
print(f'Tiempo de preparacion: {tiempo_preparacion}')
print(f'la dificultad para la realizacion de este plato es : {dificultad}')


