import pygame
import sys
import os

from student import Student

Student = Student(0, 0, 64, 64)

# Initialize Pygame
pygame.init()

# Set the dimensions of each chair and the number of chairs in each row and column
chair_width, chair_height = 32, 32
rows, cols = 5, 5

# Set the dimensions of the screen
screen_width = chair_width * cols
screen_height = chair_height * rows
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the chair image
chair_image = pygame.image.load(os.path.join('assets', 'chair.png'))

# Create a matrix of chairs
for row in range(rows):
    for col in range(cols):
        screen.blit(chair_image, (col * chair_width, row * chair_height))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
