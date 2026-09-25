nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
materia = input("Ingrese su materia favorita: ")

print("Hola", nombre, "tenés", edad, "años y tu materia favorita es", materia)

if edad >= 16:
    print("Puede votar próximamente")
else:
    print("Todavía no puede votar")
