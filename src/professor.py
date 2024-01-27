# professor.py
import time
import pygame
import random
from book import Book

# Initialize Pygame
pygame.init()

# Define the font
font = pygame.font.Font(None, 36)  # Use the default font and a size of 36


class Professor:
    def __init__(self, x, y, width, height):
        self.image = pygame.image.load('assets/Uolevi.png')
        self.pos = [x, y]
        self.width = width
        self.height = height
        self.books = []
        self.message = None

    def draw(self, screen):
        screen.blit(self.image, self.pos)
        for book, throw_time in self.books:
            book.draw(screen)

    def throw_book(self, target_pos):
        # Create a new book and add it to the list of books
        book = Book(self.pos[0], self.pos[1], target_pos)
        self.books.append((book, time.time()))

        # Make the professor "speak"
        self.message = font.render(
            get_random_exclamation('professor_exclamation.txt')[0], True, (255, 255, 255))

# Reads a random line from exclamations and returns it as list including (name;damage;radius;speed)
def get_random_exclamation(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        exclamations = file.readlines()
        exclamation = random.choice(exclamations).strip().split(';')
    return exclamation
