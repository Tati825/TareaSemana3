# Primera función para registrar los datos de la mascota
def registrar():
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = int(input("Ingrese la edad de la mascota en años: "))
    return nombre, especie, edad


# Segunda función para presentar los datos una vez registrados
def mostrar(nombre, especie, edad):
    print("\nLa nueva mascota")
    print(f"Nombre : {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad   : {edad} años")


# Llamada de las funciones registrar y mostrar
nombre, especie, edad = registrar()
mostrar(nombre, especie, edad)
