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

    def update_lose(self):
        self.lose_text = self.FONT.render("You Lost!",1,"red")
        self.screen.blit(self.lose_text,(self.Settings.WIDTH/2 - self.lose_text.get_width()/2,self.Settings.HEIGHT/2 - self.lose_text.get_height()))