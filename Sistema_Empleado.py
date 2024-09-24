print('***Sistema de Empleados***')
nombre_empleado = input("Ingrese el nombre de empleado: ")
edad_empleado = float(input('Salario del empleado: '))
es_jefe_departamento = input("Es Jefe de departamneto (SI/NO)?: ")

#Vamos a convertir un tipo bool la variable ess jefe de departamento
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

print(f'Nombre del empleado: {nombre_empleado}')
print(f'salario del empleado: {edad_empleado:.4f}')
print(f'Es jefe de departamento?: {es_jefe_departamento}')



