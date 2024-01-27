# book.py
import pygame


class Book:
    def __init__(self, x, y, target_pos):
        self.image = pygame.image.load('assets/book.png')
        self.pos = [x, y]
        self.target_pos = target_pos
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 2

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def update(self):
        # Calculate the direction vector
        dx = self.target_pos[0] - self.pos[0]
        dy = self.target_pos[1] - self.pos[1]

        # Calculate the magnitude of the direction vector
        magnitude = (dx**2 + dy**2)**0.5

        # Normalize the direction vector to get a unit direction vector
        dx /= magnitude
        dy /= magnitude

        # Multiply the unit direction vector by the speed to get the velocity vector
        dx *= self.speed
        dy *= self.speed

        # Add the velocity vector to the current position to get the new position
        self.pos[0] += dx
        self.pos[1] += dy