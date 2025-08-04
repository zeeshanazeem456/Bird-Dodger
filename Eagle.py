import pygame
import random

from settings import settings

class bird:
    def __init__(self,WIN,X):
        self.screen = WIN
        self.Settings = settings()
        self.Frames = [
            pygame.image.load(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\bird\bird_0.png"),
            pygame.image.load(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\bird\bird_1.png"),
            pygame.image.load(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\bird\bird_2.png"),
            pygame.image.load(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\bird\bird_3.png"),
            pygame.image.load(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\bird\bird_4.png"),
            pygame.image.load(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\bird\bird_5.png"),
            pygame.image.load(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\bird\bird_6.png"),
            pygame.image.load(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\bird\bird_7.png"),
            pygame.image.load(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\bird\bird_8.png"),
            pygame.image.load(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\bird\bird_9.png"),
        ]
        self.current_frame = 0 
        self.image = self.Frames[self.current_frame]
        self.rect = self.image.get_rect()
        x = random.randint(0,self.Settings.WIDTH)
        self.rect.center = (x,0)
        self.width = self.image.get_height()
        self.rect.x = X
        self.last_update = pygame.time.get_ticks()  # time when last frame changed
        self.frame_delay = 50  # milliseconds between frames; increase for slower animation
        self. bird_add_increment = 2000
        self.bird_count = 0
        self.bird_velo = random.randint(1,3)


    def draw(self):
        self.screen.blit(self.image, self.rect)

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.Frames)
            self.image = self.Frames[self.current_frame]
            self.last_update = now

    def update(self):
        self.rect.y += self.bird_velo #self.Settings.bird_velocity
        self.animate()
