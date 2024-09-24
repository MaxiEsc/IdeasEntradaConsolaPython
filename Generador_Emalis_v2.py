#Generador de emails version 2

nombre = input("Ingrese su nomber por favor:\t")
apellido = input("Ingrese si apellido por favor:\t")
nombre_empresa = input("Ingrese el nombre de su empresa:\t")
extension_dominio= input("Ingrese la extension de dominio:\t")

nombre = nombre.replace(' ', '.').lower()
apellido = apellido.replace(' ','.').lower()
nombre_empresa = nombre_empresa.replace(' ', '')

email = nombre + '.' + apellido + '.'+ '@' + nombre_empresa + '.' + extension_dominio
print(f'El email generado es: {email}')