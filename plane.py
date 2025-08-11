import pygame
from settings import settings
class Plane:
    def __init__(self, WIN):
        self.Settings = settings()
        self.screen = WIN
        self.image = pygame.image.load("plane_sprites\plane_straight.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, self.Settings.HEIGHT - self.rect.height / 2)

        self.hitbox_body = pygame.Rect(0, 0, self.rect.width // 3, self.rect.height * 0.7)    
        self.hitbox_wings = pygame.Rect(0, 0, self.rect.width * 0.9, self.rect.height // 4)
        self.hit_flag = False    
        self.update_hitboxes()

    def update_hitboxes(self):
        self.hitbox_body.center = self.rect.center
        self.hitbox_wings.center = self.rect.center 

    def change_image(self, new_image_path):
        old_center = self.rect.center
        self.image = pygame.image.load(new_image_path)
        self.rect = self.image.get_rect()
        self.rect.center = old_center
        self.update_hitboxes()

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.Settings.plane_speed
        self.change_image("plane_sprites/plane_left_1.png")
        self.update_hitboxes()

    def move_right(self):
        if self.rect.x < self.Settings.WIDTH - self.rect.width:
            self.rect.x += self.Settings.plane_speed
        self.change_image("plane_sprites/plane_right_1.png")
        self.update_hitboxes()

    def draw_plane(self):
        self.screen.blit(self.image, self.rect)
        if self.hit_flag:
            pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox_body, 2) 
            pygame.draw.rect(self.screen, (255,0, 0), self.hitbox_wings, 2)   
