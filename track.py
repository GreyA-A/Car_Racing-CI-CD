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

        self.checkpoints = [
            pygame.Rect(width // 2, 100, 10, 100),
            pygame.Rect(width - 200, height // 2, 100, 10),
            pygame.Rect(width // 2, height - 200, 10, 100),
            pygame.Rect(100, height // 2, 100, 10)
        ]
        self.current_checkpoint = 0

        self.start_time = pygame.time.get_ticks()
        self.last_finish_time = 0
    
    def check_collision(self, car):
        car_mask = pygame.mask.from_surface(car.image)
        offset = (int(car.rect.x - self.rect.x), int(car.rect.y - self.rect.y))

        overlap = self.mask.overlap(car_mask, offset)
        return overlap is not None
    
    def render(self, surface):
        surface.blit(self.image, self.rect.topleft)