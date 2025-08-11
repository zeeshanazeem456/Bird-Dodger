import pygame
import random
import os
from settings import settings

class bird:
    def __init__(self, WIN, X):
        self.screen = WIN
        self.Settings = settings()
        base_path = os.path.join("bird")
        self.Frames = [
            pygame.image.load(os.path.join(base_path, f"bird_{i}.png"))
            for i in range(10)
        ]

        self.current_frame = 0
        self.image = self.Frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (X, 0)
        self.width = self.image.get_height()
        self.last_update = pygame.time.get_ticks()
        self.frame_delay = 50
        self.bird_velo = random.randint(1, 3)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.Frames)
            self.image = self.Frames[self.current_frame]
            self.last_update = now

    def update(self):
        self.rect.y += self.bird_velo
        self.animate()
