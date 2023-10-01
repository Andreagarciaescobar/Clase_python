"""Test for Car class."""


class TestCar:
    """Test class for Car model"""

    def test_move_distance_traveled_modified(self, car):
        
        car.move(4)
        assert car.distance_traveled ==4

        car.move(5)
        assert car.distance_traveled == 9
    
    def test_move_velocidad_modifications(self):
        pass
   