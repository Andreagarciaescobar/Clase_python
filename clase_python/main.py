
from clase_python.model.car import Car


def main():
    

    carro1: Car("Nissan, 2022, 4")

    carro1.move(4)

    carro1.vel(True)

    print(carro1.distance_traveled)
    print(carro1.velocidad)

if __name__ =="__main__":
    main()