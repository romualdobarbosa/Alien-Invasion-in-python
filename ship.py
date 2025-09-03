import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #self.settings = ai_game.settings
        self.image = pygame.image.load('C:\\Python Alien Invasion\\images\\ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        #self.rect.centerx = self.screen.get_rect().centerx
        #self.rect.bottom = self.screen.get_rect().bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)