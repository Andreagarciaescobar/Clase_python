""" Class for car model."""

from clase_python.model.car import VehicleABC

MAX_DISTANCE_CAN_TRAVEL = 5

AVAILABLE_CAR_BRANDS = ['Nissan', 'Toyota', 'bmw']


class Car(VehicleABC):
    
    
    def __init__(self, brand: str, model: int, door_quantity: int) -> None:
        """Constructor for car class."""

        self.brand = brand 
        self.model = model
        self.door_quantity = door_quantity
        self.distance_traveled = 0
        self.velocidad = 0

    def move (self, additional_distance) -> None:

        if additional_distance <= MAX_DISTANCE_CAN_TRAVEL:
            self.distance_traveled += additional_distance 
        else:
            self.distance_traveled += MAX_DISTANCE_CAN_TRAVEL
        
    def vel(self, acelerar) -> None:

        if vel(acelerar== True) :
            self.velocidad += + 10
        else:
            self.velocidad = 0 

    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, brand):
        if brand in AVAILABLE_CAR_BRANDS:
            self._brand = brand
        else:
            print("Ingrese una opcion valida.")



