import pygame

class button:
    def __init__(self, screen, text, position, action):
        self.screen = screen
        self.text = text
        self.position = position
        self.action = action
        self.font = pygame.font.Font(None, 40)
        self.rect = None

    def draw(self):
        # Draw the button
        button_text = self.font.render(self.text, True, (255, 255, 255))
        button_rect = button_text.get_rect(center=self.position)
        self.rect = button_rect
        pygame.draw.rect(self.screen, (0, 0, 255), button_rect.inflate(30, 30))
        self.screen.blit(button_text, button_rect)

    def click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.action()
