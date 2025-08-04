import pygame
from settings import settings

class Plane:
    def __init__(self,WIN):
        self.Settings = settings()
        self.screen = WIN
        self.image = pygame.image.load(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\plane_sprites\plane_straight.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200,self.Settings.HEIGHT - self.rect.height/2)
        self.x = self.rect.x

    def change_image(self,new_image_path):
        self.image = pygame.image.load(new_image_path) 
        new_rect = self.image.get_rect()
        self.rect.width = new_rect.width
        self.rect.height = new_rect.height

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.Settings.plane_speed
        self.change_image(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\plane_sprites\plane_left_1.png")

    def move_right(self):
        #self.rect.center = (self.x,self.Settings.HEIGHT - self.rect.height/2)
        if self.rect.x < self.Settings.WIDTH - self.rect.width:
            self.rect.x += self.Settings.plane_speed
        self.change_image(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\plane_sprites\plane_right_1.png")

    def draw_plane(self):
        self.screen.blit(self.image, self.rect)