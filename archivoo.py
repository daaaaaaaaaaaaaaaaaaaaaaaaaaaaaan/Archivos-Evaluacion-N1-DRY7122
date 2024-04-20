#Solicitar información al usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
sección= input("Ingrese su sección: ")
sede = input("Ingrese su sede actual: ")

#Imprimir mensaje con la info recopilada
print("\n¡Hola,  {} {}!\nBienvenido a la sección {} en la sede {}. "
.format(nombre, apellido, sección, sede))
