import random

def run():
    number_found = False
    random_number = random.randint(1, 20)
    intento = 1

    while not number_found:
        number=int(input("Ingresa un número: \n"))

        if intento < 5:
            if number==random_number:
                print("Felicitaciones! has adivinado")
                number_found = True
            elif number > random_number:
                print("El número ingresado es muy grande") 
                intento += 1
            else:
                print("El número ingresado es muy pequeño")
                intento += 1
        else:
            print("Te quedaste sin intentos")
            number_found = True


if __name__ == "__main__":
    run()