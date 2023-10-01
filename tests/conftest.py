"""Configuration test file."""

import pytest

from clase_python.model.car import Car

@pytest.fixture()
def car():
    return Car('bmw', 2004, 4)


