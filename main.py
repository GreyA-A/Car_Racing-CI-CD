import pygame
import sys
import argparse
from car import Car
from track import Track

class Config:
    def __init__(self):
        self.difficulty = "normal"
        self.car_color = "red"
        self.map_id = 1
        self.parse_args()

    def parse_args(self):
        parser = argparse.ArgumentParser(description="Car Racing Game (CI/CD Pipeline)")
        parser.add_argument("--difficulty", choices=["easy", "normal", "hard"], default="normal", help="Difficulty level")
        parser.add_argument("--color", choices=["red", "blue", "green"], default="red", help="Car color")
        
        args = parser.parse_args()
        self.difficulty = args.difficulty
        self.car_color = args.color