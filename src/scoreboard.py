# scoreboard.py
import pygame


class Scoreboard:
    def __init__(self, x, y, font):
        self.score = 0
        self.x = x
        self.y = y
        self.font = font

    def increment_score(self, amount):
        self.score += amount

    def reset_score(self):
        self.score = 0

    def draw(self, screen):
        score_text = self.font.render(
            f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (self.x, self.y))

    def get_score(self):
        return self.score