import pygame

class CircleShape:
    def __init__(self, x, y, radius):
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        
    def collides_with(self, other):
        # Calculate distance between centers
        distance = self.position.distance_to(other.position)
        # Check if distance is less than sum of radii
        return distance <= self.radius + other.radius 