import pygame 
import time
import random
from settings import settings
from plane import Plane
from text import Text
from Eagle import bird
from button import button

pygame.init()
pygame.mixer.init()

class GameManager:
    def __init__(self):
        self.Settings = settings()
        self.WIN = pygame.display.set_mode((self.Settings.WIDTH,self.Settings.HEIGHT))
        pygame.display.set_caption("Space Dodger")
        self.plane = Plane(self.WIN)
        self.plane_still = True
        self.clock = pygame.time.Clock()
        self.start_time = time.time()
        self.text = Text(self.WIN)
        self.birds = []
        self.hit_count = 0
        self.score = 0
        self.plane_sound = pygame.mixer.Sound(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\sounds\plane_sound.mp3")
        self.plane_sound.play(-1)
        self.plane_sound.set_volume(0.4) 
        self.Bird_sound = pygame.mixer.Sound(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\sounds\birds.wav")
        self.Bird_sound.play(-1)
        self.time_cap = 0
        self.flag_time = 2
        #self.Button = button()
        self.crash_sound = pygame.mixer.Sound(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\sounds\crash_sound.mp3")

    def run(self):
        dt = self.clock.tick(60)
        self.Settings.bird_count += dt
        if self.Settings.bird_count > self.Settings.bird_add_increment:
            for _ in range(3):
                bird_x = random.randint(0,self.Settings.WIDTH - self.bird.width)
                self.Bird = bird(self.WIN,bird_x)
                self.birds.append(self.bird)

            self.Settings.bird_add_increment = max(200,self.bird_add_increment-50)
            self.Settings.bird_count = 0

        self.Event_Handling()

    def Event_Handling(self):
        self.running = True
        while self.running:
            if self.hit_count > 3:
                break
            self.clock.tick(60)  # Moved from run()
            self.elapsed_time = time.time() - self.start_time
            self.time_cap = int(self.elapsed_time)
            self.Settings.bird_count += 60  # Approximation since tick(60)
            if self.time_cap > self.flag_time:
                self.flag_time += 4
                self.score += 25

            if self.Settings.bird_count > self.Settings.bird_add_increment:
                for _ in range(1):
                    bird_x = random.randint(0, self.Settings.WIDTH - 64)  # 64 = bird width estimate
                    new_bird = bird(self.WIN, bird_x)
                    self.birds.append(new_bird)
                self.Settings.bird_count = 0

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
                self.plane_still = False
                self.plane.move_right()
            if self.plane_still:
                self.plane.change_image(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\plane_sprites\plane_straight.png")

            self.position()

    def position(self):
            self.WIN.fill((135, 206, 235)) 
            for bird_x in self.birds[:]:
                bird_x.update()
            self.render_game()

    def render_game(self):
        self.plane.draw_plane()
        for bird_x in self.birds[:]:
            bird_x.draw()
            if bird_x.rect.y > self.Settings.HEIGHT:
                self.birds.remove(bird_x)
            elif bird_x.rect.y >= self.plane.rect.y and bird_x.rect.colliderect(self.plane):
                self.birds.remove(bird_x)
                self.hit_count +=1
                self.crash_sound.play()
                break
        if self.hit_count > 3:
            self.text.update_lose()

        for bird_x in self.birds[:]:
            bird_x.draw()

        self.text.update(self.elapsed_time)
        self.text.update_score(self.score)
        pygame.display.update()
        if self.hit_count > 3:
            pygame.time.delay(4000)


def main():
    pygame.init()  
    game = GameManager()
    game.run()
    pygame.quit()

if __name__ == "__main__":  
    main()