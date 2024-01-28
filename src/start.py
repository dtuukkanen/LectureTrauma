import subprocess
import pygame
import sys
from saveScore import get_high_score

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
FONT_SIZE = 32

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a font
font = pygame.font.Font(None, FONT_SIZE)

# Initialize start_button_rect
start_button_rect = None

def draw_start_view():
    global start_button_rect
    # Clear the screen
    screen.fill((0, 0, 0))

    # Load the logo image
    logo = pygame.image.load('assets/logo.png')

    # Draw the logo at the top center of the screen
    logo_rect = logo.get_rect(center=(WIDTH / 2, 50))
    screen.blit(logo, logo_rect)

    # Draw the start button
    start_button_text = font.render("Start Game", True, (255, 255, 255))
    start_button_rect = start_button_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    pygame.draw.rect(screen, (255, 0, 0), start_button_rect)
    screen.blit(start_button_text, start_button_rect)

    # Draw the high score
    high_score = get_high_score()
    high_score_text = font.render(f"Highest Score: {high_score}", True, (255, 255, 255))
    screen.blit(high_score_text, (10, 10))

    # Flip the display
    pygame.display.flip()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button_rect.collidepoint(mouse_pos):
                    pygame.display.quit()
                    subprocess.call(["python3", "src/main.py"])

        draw_start_view()

if __name__ == "__main__":
    main()