import pygame

class Track:
    def __init__(self, width, height):
        self.image = pygame.Surface((width, height))
        grass_color = (50, 200, 50)
        self.image.fill(grass_color)

        pygame.draw.rect(self.image, (100, 100, 100), (100, 100, width - 200, height - 200), border_radius=50)
        pygame.draw.rect(self.image, grass_color, (250, 250, width - 500, height - 500), border_radius=50)
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_threshold(self.image, grass_color, (1, 1, 1, 255))
        
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
    
    def update_checkpoints(self, car):
        target_rect = self.checkpoints[self.current_checkpoint]

        if car.rect.colliderect(target_rect):
            self.current_checkpoint += 1

            if self.current_checkpoint >= len(self.checkpoints):
                self.current_checkpoint = 0
                self.last_finish_time = pygame.time.get_ticks() - self.start_time
                self.start_time = pygame.time.get_ticks()

                return True
        return False

    def get_finish_time(self):
        return self.last_finish_time / 1000.0 if self.last_finish_time > 0 else None
    
    def render(self, surface):
        surface.blit(self.image, self.rect.topleft)