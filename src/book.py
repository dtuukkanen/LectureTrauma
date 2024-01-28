# book.py
import pygame
import time

class Book:
    def __init__(self, x, y, target_pos, exclamation, score):
        self.image = pygame.image.load('assets/book.png')
        self.pos = [x, y]
        self.target_pos = target_pos
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hit_time = None
        self.damage = int(exclamation[1])
        self.radius = int(exclamation[2])
        self.speed = int(exclamation[3]) + score // 10

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def update(self):
        # Calculate the direction vector
        dx = self.target_pos[0] - self.pos[0]
        dy = self.target_pos[1] - self.pos[1]

        # Calculate the magnitude of the direction vector
        magnitude = (dx**2 + dy**2)**0.5

        # If the book is close enough to the target, snap it to the target and stop updating
        if magnitude < self.speed:
            self.pos = self.target_pos
            return

        # Normalize the direction vector to get a unit direction vector
        dx /= magnitude
        dy /= magnitude

        # Multiply the unit direction vector by the speed to get the velocity vector
        dx *= self.speed
        dy *= self.speed

        # Add the velocity vector to the current position to get the new position
        self.pos[0] += dx
        self.pos[1] += dy
        
        # Check if the book has reached its target position
        if self.pos == self.target_pos and self.hit_time is None:
            # Set hit_time to the current time
            self.hit_time = time.time()
