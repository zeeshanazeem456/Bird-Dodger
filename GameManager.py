import pygame 
import time
import random
from settings import settings
from plane import Plane

class GameManager:
    def __init__(self):
        self.Settings = settings()
        self.WIN = pygame.display.set_mode((self.Settings.WIDTH,self.Settings.HEIGHT))
        pygame.display.set_caption("Space Dodger")
        self.plane = Plane(self.WIN)
        self.plane_still = True
        self.clock = pygame.time.Clock()

    def run(self):
        self.clock.tick(60)
        self.Event_Handling()

    def Event_Handling(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
            
            keys = pygame.key.get_pressed()
            self.plane_still = True
            if keys[pygame.K_LEFT]:
                self.plane_still = False
                self.plane.move_left()
            if keys[pygame.K_RIGHT]:
                self.plane.move_right()
                self.plane_still = False
            if self.plane_still:
                self.plane.change_image(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\plane_sprites\plane_straight.png")
                 
            #To display sky blue background
            self.position()

    def position(self):
            self.WIN.fill((135, 206, 235)) 
            self.render_game()

    def render_game(self):
        self.plane.draw_plane()
        pygame.display.update()

def main():
    pygame.init()  
    game = GameManager()
    game.run()
    pygame.quit()

if __name__ == "__main__":  
    main()