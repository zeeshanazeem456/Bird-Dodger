import pygame

class settings:
    def __init__(self):
        self.HEIGHT = 600
        self.WIDTH = 800

        #plane settings
        self.plane_speed = 6

        #Text settings
        self.text_size = 30
        self.text_font = "comicsans"

        #Bird Settings
        self.bird_velocity = 1
        self.bird_count = 0
        self.bird_add_increment = 3000

        #leaderboard Settings
        self.leaderboard_file = "leaderboard.txt"
        self.max_entries = 10
        self.name = ""
        

