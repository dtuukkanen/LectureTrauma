import sys
import pygame
from student import Student
from professor import Professor

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

THROW_BOOK_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(THROW_BOOK_EVENT, 3000)  # 3000 milliseconds = 3 seconds

# In the main game loop:
while running:
    # Update and draw the books
    for book in professor.books:
        book.update()
        book.draw(screen)

    # Check for collisions between the student and the books
    for book in professor.books:
        if pygame.Rect(student.pos[0], student.pos[1], student.width, student.height).colliderect(pygame.Rect(book.pos[0], book.pos[1], book.width, book.height)):
            student.lives -= 1
            professor.books.remove(book)

        if student.lives <= 0:
            running = False

    # Draw the student's lives
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
            professor.throw_book(student.pos)

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
