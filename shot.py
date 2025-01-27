import pygame
from shapes import CircleShape

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        pygame.sprite.Sprite.__init__(self)
        self.add(self.containers)
        self.velocity = pygame.Vector2(0, 0)  # Will be set after creation
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
        
    def update(self, dt):
        self.position += self.velocity * dt 