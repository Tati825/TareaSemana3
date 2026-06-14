class Mascota:
    # Creando el constructor
    def __init__(pet, nombre, especie, edad):
        pet.nombre = nombre
        pet.especie = especie
        pet.edad = edad

    # Método para recopilar información
    def mostrar_informacion(pet):
        print("\nLa mascota es:")
        print(f"Nombre : {pet.nombre}")
        print(f"Especie: {pet.especie}")
        print(f"Edad   : {pet.edad} años")

    # Método para saber el sonido de la mascota dependiendo cuál hayan elegido
    def hacer_sonido(pet):
        if pet.especie.lower() == "perro":
            print(f"{pet.nombre} hace: Guau")
        elif pet.especie.lower() == "gato":
            print(f"{pet.nombre} hace: Miau")
        else:
            print(f"{pet.nombre} hace otro sonido")
