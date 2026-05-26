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


class InputHandler:
    def get_input(self):
        keys = pygame.key.get_pressed()
        actions = {
            "accelerate": keys[pygame.K_UP] or keys[pygame.K_w],
            "brake": keys[pygame.K_DOWN] or keys[pygame.K_s],
            "left": keys[pygame.K_LEFT] or keys[pygame.K_a],
            "right": keys[pygame.K_RIGHT] or keys[pygame.K_d]
        }
        return actions


class Game:
    def __init__(self):
        pygame.init()
        self.config = Config()

        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Car Racing - CI/CD Project")

        self.clock = pygame.time.Clock()
        self.is_running = True

        self.track = Track(self.screen_width, self.screen_height)
        self.car = Car((self.screen_width // 2, self.screen_height - 150), self.config.car_color)
        self.input = InputHandler()

        if self.config.difficulty == "hard":
            self.car.max_speed = 7
        elif self.config.difficulty == "easy":
            self.car.max_speed = 4

        self.font = pygame.font.SysFont(None, 36)
        self.laps = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        actions = self.input.get_input()

        if actions["accelerate"]:
            self.car.accelerate()
        if actions["brake"]:
            self.car.brake()
        if actions["left"]:
            self.car.turn(1)
        elif actions["right"]:
            self.car.turn(-1)

        self.car.update_physics()

        if self.track.check_collision(self.car):
            self.car.speed *= 0.8

        if self.track.update_checkpoints(self.car):
            self.laps += 1

    def render(self):
        self.screen.fill((0, 0, 0))

        self.track.render(self.screen)
        self.car.render(self.screen)

        time_text = self.font.render(f"Last lap: {self.track.get_finish_time()} s", True, (255, 255, 255))
        laps_text = self.font.render(f"Laps: {self.laps}", True, (255, 255, 255))
        diff_text = self.font.render(f"Difficulty: {self.config.difficulty}", True, (255, 255, 255))

        self.screen.blit(time_text, (10, 10))
        self.screen.blit(laps_text, (10, 40))
        self.screen.blit(diff_text, (10, 70))

        pygame.display.flip()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
