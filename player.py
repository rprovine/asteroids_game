import pygame
from constants import PLAYER_RADIUS

PLAYER_TURN_SPEED = 360
class CircleShape:
    def __init__(self, x, y, radius):
        self.position = pygame.Vector2(x, y)
        self.radius = radius

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, 2)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate counter-clockwise
        if keys[pygame.K_d]:
            self.rotate(dt)   # Rotate clockwise

   
