# professor.py
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
        for book in self.books:
            book.draw(screen)

    def throw_book(self, target_pos):
        # Create a new book and add it to the list of books
        book = Book(self.pos[0], self.pos[1], target_pos)
        self.books.append(book)

        # Make the professor "speak"
        self.message = font.render(
            get_random_exclamation('professor_exclamation.txt'), True, (255, 255, 255))


def get_random_exclamation(file_path):
    with open(file_path, 'r') as file:
        exclamations = file.readlines()
    return random.choice(exclamations).strip()
