import pygame 
import time
import random
from settings import settings

class GameManager:
    def __init__(self):
        self.Settings = settings()
        self.WIN = pygame.display.set_mode((self.Settings.WIDTH,self.Settings.HEIGHT))
        pygame.display.set_caption("Space Dodger")

    def run(self):
        self.Event_Handling()

    def Event_Handling(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
            
            #To display sky blue background
            self.WIN.fill((135, 206, 235)) 
            self.render_game()

    def render_game(self):
        pygame.display.update()

def main():
    pygame.init()  
    game = GameManager()
    game.run()
    pygame.quit()

if __name__ == "__main__":  
    main()