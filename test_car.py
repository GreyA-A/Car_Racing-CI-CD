import pytest
import pygame
from car import Car

@pytest.fixture
def default_car():
    # Pygame потребує ініціалізації відеопідсистеми для роботи з Surface у класі Car
    pygame.init()
    pygame.display.set_mode((1, 1), pygame.HIDDEN) 
    
    car = Car((400, 300), "red")
    yield car  # Повертаємо авто для тесту
    
    pygame.quit() # Очищуємо ресурси після тесту

@pytest.mark.physics
def test_car_initialization(default_car):
    assert default_car.speed == 0
    assert default_car.angle == 0
    assert default_car.pos.x == 400
    assert default_car.pos.y == 300

@pytest.mark.physics
def test_car_acceleration(default_car):
    default_car.accelerate()
    # Швидкість має дорівнювати прискоренню (0.2)
    assert default_car.speed == default_car.acceleration

@pytest.mark.physics
def test_car_brake(default_car):
    default_car.speed = 3
    default_car.brake()
    # Формула з car.py: speed - acceleration * 2 (3 - 0.4 = 2.6)
    assert default_car.speed == 2.6

@pytest.mark.physics
@pytest.mark.parametrize("direction, expected_angle", [
    (1, 4),   # Поворот вліво (куди: 1 * rotation_speed)
    (-1, -4), # Поворот вправо (куди: -1 * rotation_speed)
    (0, 0)    # Прямо
])
def test_car_turn(default_car, direction, expected_angle):
    # Щоб машина повертала, вона повинна рухатися (швидкість > 0.1)
    default_car.speed = 1
    default_car.turn(direction)
    assert default_car.angle == expected_angle