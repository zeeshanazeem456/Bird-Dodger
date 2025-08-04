import pygame
from settings import settings
pygame.font.init()

class Text:
    def __init__(self,WIN):
        self.screen = WIN
        self.Settings = settings()
        self.FONT = pygame.font.SysFont("comicsans",30)
        
    def update(self,elapsed_time):
        self.time_text = self.FONT.render(f"Time: {round(elapsed_time)}s",1,"red")
        self.screen.blit(self.time_text,(10,10))