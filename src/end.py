import pygame
import sys
from saveScore import save_scoreboard
import subprocess

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
FONT_SIZE = 32
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 40

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a font
font = pygame.font.Font(None, FONT_SIZE)

# Define button rectangles
try_again_button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
quit_button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 + 50, BUTTON_WIDTH, BUTTON_HEIGHT)

def draw_end_view(score):
    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Create a game over text
    game_over_text = font.render("Game Over!", True, (255, 255, 255))
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

    # Draw the game over text
    screen.blit(game_over_text, game_over_rect)

    # Draw the try again button
    pygame.draw.rect(screen, (0, 255, 0), try_again_button)  # Green button
    try_again_text = font.render("Try Again", True, (0, 0, 0))
    screen.blit(try_again_text, (try_again_button.x + 10, try_again_button.y + 10))

    # Draw the quit button
    pygame.draw.rect(screen, (255, 0, 0), quit_button)  # Red button
    quit_text = font.render("Quit", True, (0, 0, 0))
    screen.blit(quit_text, (quit_button.x + 30, quit_button.y + 10))

    # Update the display
    pygame.display.flip()

    # Save the score
    save_scoreboard(score)

def main(score):
    draw_end_view(score)

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if try_again_button.collidepoint(mouse_pos):
                    pygame.display.quit()
                    subprocess.call(["python", "src/main.py"])
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    score = 0  # Replace this with the actual score
    main(score)