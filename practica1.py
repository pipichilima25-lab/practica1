
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
materia = input("Ingrese su materia favorita: ")

print("Hola", nombre, "tenés", edad, "años y tu materia favorita es", materia)

if edad >= 16:
    print("Puede votar próximamente")
else:
    print("Todavía no puede votar")

# 1. ¿Qué es una variable en programación?
# Una variable es un espacio donde se guarda un dato para poder utilizarlo después en el programa.

# 2. ¿Para qué sirve input()?
# Sirve para pedirle un dato al usuario y guardarlo en el programa.

# 3. ¿Qué función cumple print()?
# Sirve para mostrar información o mensajes en la pantalla.

# 4. ¿Qué es una condición (if)?
# Es una forma de hacer que el programa tome una decisión dependiendo de si se cumple o no una condición.//

alumnos = [
    {
        "nombre": "Yasmin",
        "materia": "Sistema Operativo",
        "edad": 18
    },
    {
        "nombre": "Jorge",
        "materia": "Matematica",
        "edad": 18
    },
    {
        "nombre": "Jeremias",
        "materia": "Base de Datos",
        "edad": 19
    },
    {
        "nombre": "Ismael",
        "materia": "Ingles",
        "edad": 18
    },
    {
        "nombre": "Renzo",
        "materia": "Redes",
        "edad": 18
    }
]
#Recorrer la lista
for alumno in alumnos:
    print(alumno["nombre"], "-", alumno["materia"])

    # Función para buscar un alumno
def buscar_alumno():
    nombre_buscar = input("Ingrese el nombre del alumno: ")

    for alumno in alumnos:
        if alumno["nombre"].lower() == nombre_buscar.lower():
            print("Alumno encontrado")
            print("Nombre:", alumno["nombre"])
            print("Materia favorita:", alumno["materia"])
            print("Edad:", alumno["edad"])
            return

    print("Alumno no encontrado")


# Llamar a la función
buscar_alumno()

# Estadísticas
print("Cantidad total de alumnos:", len(alumnos))

mayores_16 = 0

for alumno in alumnos:
    if alumno["edad"] > 16:
        mayores_16 += 1

print("Cantidad de alumnos mayores de 16:", mayores_16)

#1. ¿Qué es una lista en Python?
#Una lista en Python es una forma de guardar varios datos juntos dentro de una misma variable. Los elementos se escriben entre corchetes [] y pueden ser números, textos u otros datos.

#2. ¿Qué es un diccionario?
#Un diccionario es una forma de guardar información organizada en pares de clave y valor. Se escribe entre llaves {}. Por ejemplo, podemos tener "nombre": "Juan" y "edad": 16.

#3. ¿Cuál es la diferencia entre una lista y un diccionario?
#La diferencia es que una lista guarda elementos en un orden y se puede acceder a ellos por su posición. En cambio, un diccionario guarda los datos utilizando una clave para identificar cada valor.

#4. ¿Para qué sirve un for?
#El for sirve para recorrer los elementos de una lista, diccionario u otra colección de datos. Por ejemplo, podemos usarlo para mostrar uno por uno los alumnos que tenemos guardados en una lista.

#5. ¿Qué es un JSON? ¿Para qué sirve? ¿Dónde se usa? ¿Cómo lo relacionarías con las listas y diccionarios de Python?
#JSON significa JavaScript Object Notation. Es un formato que sirve para guardar y compartir información de una manera organizada y fácil de leer.
#Se usa mucho para enviar información entre programas, páginas web y servidores. Por ejemplo, cuando una página web necesita recibir información de un servidor, puede utilizar JSON.
#Lo relacionaría con las listas y diccionarios de Python porque su forma de organizar los datos es muy parecida. Un objeto JSON se parece a un diccionario de Python y una lista de JSON se parece a una lista de Python. Por eso es fácil trabajar con información JSON desde Python.
