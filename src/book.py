# book.py
import pygame
import time

class Book:
    def __init__(self, x, y, target_pos):
        self.image = pygame.image.load('assets/book.png')
        self.pos = [x, y]
        self.target_pos = target_pos
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 1
        self.hit_time = None

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def update(self):
        # Move towards the target position
        if self.pos[0] < self.target_pos[0]:
            self.pos[0] += self.speed
        elif self.pos[0] > self.target_pos[0]:
            self.pos[0] -= self.speed
        if self.pos[1] < self.target_pos[1]:
            self.pos[1] += self.speed
        elif self.pos[1] > self.target_pos[1]:
            self.pos[1] -= self.speed

        # Check if the book has become stationary
        if self.pos == self.target_pos:
            # Set hit_time to the current time
            self.hit_time = time.time()