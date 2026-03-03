import pygame

class Track:
    def __init__(self, width, height):
        self.image = pygame.Surface((width, height))
        self.image.fill((50, 200, 50))

        pygame.draw.rect(self.image, (100, 100, 100), (100, 100, width - 200, height - 200), border_radius=50)
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.mask.clear()
        grass_color = (50, 200, 50)
        for x in range(width):
            for y in range(height):
                if self.image.get_at((x, y))[:3] == grass_color:
                    self.mask.set_at((x, y), 1)