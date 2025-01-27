import pygame
import random
from shapes import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        pygame.sprite.Sprite.__init__(self)
        self.add(self.containers)
        self.velocity = pygame.Vector2(0, 0)  # Will be set after creation
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        # Always destroy this asteroid
        self.kill()
        
        # If this was a small asteroid, we're done
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        # Calculate new radius for child asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Generate random split angle
        split_angle = random.uniform(20, 50)
        
        # Create two new velocity vectors
        vel1 = self.velocity.rotate(split_angle) * 1.2
        vel2 = self.velocity.rotate(-split_angle) * 1.2
        
        # Create two new smaller asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vel1
        
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vel2 