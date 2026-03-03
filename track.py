import pygame

class Track:
    def __init__(self, width, height):
        self.image = pygame.Surface((width, height))
        self.image.fill((50, 200, 50))

        pygame.draw.rect(self.image, (100, 100, 100), (100, 100, width - 200, height - 200), border_radius=50)
        self.rect = self.image.get_rect()