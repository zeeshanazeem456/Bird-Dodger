import pygame
from button import button
from settings import settings
from leaderboard import Leaderboard

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.name = ""
        self.flag_leaderboard = False
        self.font = pygame.font.SysFont("comicsans",30)
        self.Settings = settings()
        self.running = True
        self.Top_scores = list()
        self.leaderboard = Leaderboard()
        self.start_button = button(self.screen, "Start Game", (self.screen.get_width() // 2, self.screen.get_height() // 2 - 50), self.start_game)
        self.quit_button = button(self.screen, "Quit", (self.screen.get_width() // 2, self.screen.get_height() // 2 + 100), self.quit_game)
        self.leaderboard_button = button(self.screen, "Leaderboard", (self.screen.get_width() // 2, self.screen.get_height() // 2 + 20), self.quit_game)

    def start_game(self):
        self.name = self.prompt_name()
        if self.name.strip() == "":
            return
        self.running = False  # Exit the main menu and start the game

    def quit_game(self):
        pygame.quit()
        quit()

    def draw(self):
        self.image_bg = pygame.image.load("menuImage.png")
        self.image_bg = pygame.transform.scale(self.image_bg, (800, 590))
        title_text = self.font.render("Bird Dodger", True, (255, 5, 255))  
        self.bg_rect = self.image_bg.get_rect()
        self.screen.blit(self.image_bg, self.bg_rect)
        self.screen.blit(title_text, (self.screen.get_width() // 2 - title_text.get_width() // 2, 100))

        self.start_button.draw()
        self.leaderboard_button.draw()
        self.quit_button.draw()
        if self.flag_leaderboard == True:
            self.draw_leaderboard_screen(self.screen,self.Top_scores)
        pygame.display.update()

    def run(self):
         while self.running:
            self.draw()
            self.handle_events()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.rect.collidepoint(event.pos):
                    self.start_game()
                elif self.quit_button.rect.collidepoint(event.pos):
                    self.quit_game()
                elif self.leaderboard_button.rect.collidepoint(event.pos):
                     self.Top_scores= self.leaderboard.get_leaderboard()
                     print("\n🏆 Sorted Leaderboard 🏆")
                     for i, (self.name, score) in enumerate(self.Top_scores, start=1):
                         print(f"{i}. {self.name} - {score}" ) 
                     self.flag_leaderboard = True 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.flag_leaderboard = False
                    

    def prompt_name(self):
        self.name = ""  
        font = pygame.font.SysFont('Arial', 36)
        input_box = pygame.Rect(100, 300, 600, 50) 
        color = pygame.Color('lightskyblue3')
        active = True 

        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and self.name.strip() != "":
                        return self.name.strip() 
                    elif event.key == pygame.K_BACKSPACE:
                        self.name = self.name[:-1] 
                    elif event.unicode.isprintable() and len(self.name) < 90:
                        self.name += event.unicode 

            
            self.screen.fill((135, 206, 235)) 
            full_text = "Enter Your Name: " + self.name
            max_width = input_box.width - 10

            while font.size(full_text)[0] > max_width:
                self.name = self.name[:-1]
                full_text = "Enter Your Name: " + self.name

            text_surface = font.render(full_text, True, (30, 30, 30))
            self.screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))  
            pygame.draw.rect(self.screen, color, input_box, 2) 
            pygame.display.flip()  

    def update_leaderboard(self,name,score):
        self.leaderboard.add_entry(name, score)

    def get_name(self):
        return self.name
    
    def draw_leaderboard_screen(self,screen, score_board):
        screen.fill((135, 206, 235))  # Clear screen with black
        font = pygame.font.SysFont(None, 48)
        small_font = pygame.font.SysFont(None, 36)

        title = font.render("<== Leaderboard ==>", True, (0,0,0))
        screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 50))

        entries = self.leaderboard.get_leaderboard()
        for i, (name, score) in enumerate(entries[:10]):  # Show top 10
            text = small_font.render(f"{i+1}. {name} - {score}", True, (0,0,0))
            screen.blit(text, (100, 120 + i * 40))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
                self.flag_leaderboard = False
        pygame.display.flip() 