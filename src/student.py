import pygame
import os

class Student:
    def __init__(self, x, y, width, height, rows, cols):
        self.image = pygame.image.load(
            os.path.join('assets', 'Oppilas8bit.png'))
        self.pos = [x, y]
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.lives = 100
        self.max_lives = 100

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def move(self, dx, dy):
        new_x = self.pos[0] + dx
        new_y = self.pos[1] + dy

        # Check if the new position is within the chair area
        if 0 <= new_x < self.cols * self.width:
            self.pos[0] = new_x
        if 0 <= new_y < self.rows * self.height:
            self.pos[1] = new_y
