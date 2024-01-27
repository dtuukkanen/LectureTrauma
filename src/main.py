import sys
import time
import pygame
from student import Student
from professor import Professor
import random

# pygame setup
pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

# Define the font
font = pygame.font.Font(None, 36)  # Use the default font and a size of 36

# Set the dimensions of each chair and the number of chairs in each row and column
chair_width, chair_height = 32, 32
rows, cols = 20, 20

# Load the chair image
chair_image = pygame.image.load('assets/chair.png')

# Load the student
student = Student(0, 0, chair_width, chair_height, rows, cols)

# Load the professor
professor_x = (cols * chair_width) // 2 - chair_width // 2
professor_y = rows * chair_height
professor = Professor(professor_x, professor_y, chair_width, chair_height)

# Book time alive
book_time_alive = 10

# Define a new event type for removing books
REMOVE_BOOK_EVENT = pygame.USEREVENT + 1
THROW_BOOK_EVENT = pygame.USEREVENT + 1

pygame.time.set_timer(THROW_BOOK_EVENT, 3000)  # 3000 milliseconds = 3 seconds

# In the main game loop:
while running:
    # In your main game loop:
    current_time = time.time()
    professor.books = [(book, throw_time) for book,
                       throw_time in professor.books if current_time - throw_time < book_time_alive]

    # Update and draw the books
    for book, throw_time in professor.books:
        book.update()
        book.draw(screen)

        # Check if the book has been stationary for more than 1 second
        if book.hit_time is not None and time.time() - book.hit_time > 1:
            professor.books.remove((book, throw_time))

    # Check for collisions between the student and the books
    for book, throw_time in professor.books:
        if pygame.Rect(student.pos[0], student.pos[1], student.width, student.height).colliderect(pygame.Rect(book.pos[0], book.pos[1], book.width, book.height)):
            student.lives -= 1
            professor.books.remove((book, throw_time))

        if student.lives <= 0:
            running = False

    # Update and draw the books
    for book, throw_time in professor.books:
        # book.update()
        book.draw(screen)

    # Draw the student's lives
    lives_text = font.render(f"Lives: {student.lives}", True, (255, 255, 255))
    screen.blit(lives_text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                student.move(0, -chair_height)
            elif event.key == pygame.K_DOWN:
                student.move(0, chair_height)
            elif event.key == pygame.K_LEFT:
                student.move(-chair_width, 0)
            elif event.key == pygame.K_RIGHT:
                student.move(chair_width, 0)
        elif event.type == THROW_BOOK_EVENT:
            # Generate a random position within the screen bounds
            random_pos = (random.randint(0, (cols * chair_width)),
                          random.randint(0, cols * chair_height))
            professor.throw_book(random_pos)
            # Set a timer to remove the book after 3 seconds
            pygame.time.set_timer(REMOVE_BOOK_EVENT, 3000)
        elif event.type == REMOVE_BOOK_EVENT:
            # Remove the book when the timer event is triggered
            if professor.books:
                professor.books.pop(0)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Draw the chairs
    for row in range(rows):
        for col in range(cols):
            screen.blit(chair_image, (col * chair_width, row * chair_height))

    # Draw the student
    student.draw(screen)

    # Draw the professor
    professor.draw(screen)

    # Draw the professor's message
    if professor.message:
        screen.blit(professor.message,
                    (professor.pos[0], professor.pos[1] - 20))

    pygame.display.flip()

    pygame.display.update()
    clock.tick(60)

pygame.quit()

print("Game Over!")
