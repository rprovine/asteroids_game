import pygame
from constants import PLAYER_RADIUS, PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shapes import CircleShape
from shot import Shot

PLAYER_TURN_SPEED = 360
class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        pygame.sprite.Sprite.__init__(self)
        
        # Add self to any containers that were specified
        self.add(self.containers)
        
        self.rotation = 0
        self.shoot_timer = 0  # Initialize timer at 0

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
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Only shoot if the cooldown timer has expired
        if self.shoot_timer <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # Reset the timer

    def update(self, dt):
        # Decrease the shoot timer
        self.shoot_timer -= dt
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate counter-clockwise
        if keys[pygame.K_d]:
            self.rotate(dt)   # Rotate clockwise
        if keys[pygame.K_SPACE]:
            self.shoot()

   
