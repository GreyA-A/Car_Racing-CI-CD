from unittest.mock import patch
import pygame
from collections import defaultdict
from main import InputHandler, Config

# 1. Тестування парсера (argparse) через підміну sys.argv


def test_config_default():
    # Підміняємо аргументи командного рядка на пустий список
    with patch('sys.argv', ['main.py']):
        config = Config()
        assert config.difficulty == "normal"
        assert config.car_color == "red"


def test_config_custom():
    # Зімітуємо запуск: python main.py --difficulty hard --color blue
    with patch('sys.argv', ['main.py', '--difficulty', 'hard', '--color', 'blue']):
        config = Config()
        assert config.difficulty == "hard"
        assert config.car_color == "blue"

# 2. Мокування (Mocking): імітація натискання клавіш


@patch('pygame.key.get_pressed')
def test_input_handler_accelerate(mock_get_pressed):
    # Створюємо фейковий список натиснутих клавіш (усі False)
    fake_keys = defaultdict(bool)
    # Робимо так, ніби натиснута кнопка "W"
    fake_keys[pygame.K_w] = True

    # Вказуємо моку повернути наш фейковий список
    mock_get_pressed.return_value = fake_keys

    handler = InputHandler()
    actions = handler.get_input()

    # Перевіряємо, чи InputHandler правильно зрозумів натискання
    assert actions["accelerate"] is True
    assert actions["brake"] is False
    assert actions["left"] is False
