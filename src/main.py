import sys
import time
import pygame
import random

from student import Student
from professor import Professor
from scoreboard import Scoreboard
from saveScore import save_scoreboard

# Health bar function
def draw_health_bar(screen, pos, health, max_health):
    # Set the dimensions and position of the health bar
    bar_width = 100
    bar_height = 20
    x, y = pos

    # Check if the position is within the screen boundaries
    screen_width, screen_height = screen.get_size()
    if x < 0 or y < 0 or x + bar_width > screen_width or y + bar_height > screen_height:
        print(f"Health bar position ({x}, {y}) is out of screen boundaries!")
        return

    # Calculate the width of the health portion of the bar
    fill = (health / max_health) * bar_width
    # Draw the outline of the health bar
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x, y, bar_width, bar_height), 1)
    # Draw the health portion of the bar
    if fill > 0:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, fill, bar_height))

def draw_chairs(screen, rows, cols, chair_width, chair_height, chair_image):
    # Draw the chairs
    for row in range(rows):
        for col in range(cols):
            screen.blit(chair_image, (col * chair_width, row * chair_height))
            
def main():
    # pygame setup
    pygame.init()
    
    screen_width, screen_height = 480, 360
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    running = True

    # Define the font
    font = pygame.font.Font(None, 36)  # Use the default font and a size of 36

    # Set the dimensions of each chair and the number of chairs in each row and column
    chair_width, chair_height = 32, 32
    rows, cols = 8, 10

    # Load the chair image
    chair_image = pygame.image.load('assets/chair_blue.png')

    # Initialize the mixer module
    pygame.mixer.init()
    # Load the music files
    pygame.mixer.music.load('assets/sounds/lecture.ogg')
    explosion_sound = pygame.mixer.Sound('assets/sounds/explosion.wav')
    hurt_sound = pygame.mixer.Sound('assets/sounds/hurt.wav')
    throw_book_sound = pygame.mixer.Sound('assets/sounds/throw_book.wav')
    move_sound = pygame.mixer.Sound('assets/sounds/move1.wav')
    # Play the music file
    pygame.mixer.music.play(-1)  # -1 means to loop the music

    # Load the student
    student = Student(0, 0, chair_width, chair_height, rows, cols)

    # Load the professor
    professor_x = (cols * chair_width) // 2 - chair_width // 2
    professor_y = rows * chair_height
    professor = Professor(professor_x, professor_y, chair_width, chair_height)

    # Book time alive
    book_time_alive = 10

    # Initialize the scoreboard
    scoreboard = Scoreboard(325, 20, font)

    # Define a new event type for removing books
    REMOVE_BOOK_EVENT = pygame.USEREVENT + 1
    THROW_BOOK_EVENT = pygame.USEREVENT + 2

    pygame.time.set_timer(THROW_BOOK_EVENT, 3000)  # 3000 milliseconds = 3 seconds
    pygame.time.set_timer(REMOVE_BOOK_EVENT, 3000)  # 3000 milliseconds = 3 seconds

    # In the main game loop:
    while running:
        # In your main game loop:
        current_time = time.time()

        # Update and draw the books
        for book, throw_time in professor.books:
            book.update()
            book.draw(screen)

        # Check for collisions between the student and the books
        for book, throw_time in professor.books:
            if pygame.Rect(student.pos[0], student.pos[1], student.width, student.height).colliderect(pygame.Rect(book.pos[0], book.pos[1], book.width, book.height)):
                student.lives -= book.damage
                professor.books.remove((book, throw_time))
                hurt_sound.play()

            if student.lives <= 0:
                explosion_sound.play()
                import end
                end.end(scoreboard.score)
                running = False

        # Update and draw the books
        for book, throw_time in professor.books:
            # book.update()
            book.draw(screen)

        # Draw the student's lives
        lives_text = font.render(f"Lives: {student.lives}", True, (50, 50, 50))
        screen.blit(lives_text, (10, 10))

        # Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    student.move(0, -chair_height)
                    move_sound.play()
                elif event.key == pygame.K_DOWN:
                    student.move(0, chair_height)
                    move_sound.play()
                elif event.key == pygame.K_LEFT:
                    student.move(-chair_width, 0)
                    move_sound.play()
                elif event.key == pygame.K_RIGHT:
                    student.move(chair_width, 0)
                    move_sound.play()
            elif event.type == THROW_BOOK_EVENT:
                # Generate a random position within the grid of chairs
                random_col = random.randint(0, cols - 1)
                random_row = random.randint(0, rows - 1)
                random_pos = (random_col * chair_width, random_row * chair_height)
                professor.throw_book(random_pos, scoreboard.score)
                throw_book_sound.play()
            elif event.type == REMOVE_BOOK_EVENT:
                # Remove the book when the timer event is triggered
                if professor.books:
                    professor.books.pop(0)
                    scoreboard.increment_score(1)

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("bisque4")

        # Draw the chairs
        draw_chairs(screen, rows, cols, chair_width, chair_height, chair_image)

        # Draw the student
        student.draw(screen)

        # Draw the professor
        professor.draw(screen)

        # Draw the scoreboard
        scoreboard.draw(screen)

        # Draw the professor's message
        if professor.message:
            message_rect = professor.message.get_rect()
            screen_center = (screen.get_width() // 2,  professor.pos[1] + 50)
            message_pos = (screen_center[0] - message_rect.width // 2, screen_center[1] - message_rect.height // 2)
            screen.blit(professor.message, message_pos)

        pygame.display.flip()
        pygame.display.set_caption("LectureTrauma")
        draw_health_bar(screen, (325, 0), student.lives, student.max_lives)
        pygame.display.update()
        clock.tick(60)

    save_scoreboard(scoreboard.score)
    pygame.quit()

    print("Game Over!")

if __name__ == "__main__":
    main()