import pygame
import constant as con


class Token(pygame.sprite.Sprite):
    def __init__(self, image, px, py):
        super().__init__()
        self.image = pygame.transform.scale(image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.center = px, py


class Player1Token(Token):
    def __init__(self, px, py):
        super().__init__(con.IMAGES['RED'], px, py)


class Player2Token(Token):
    def __init__(self, px, py):
        super().__init__(con.IMAGES['BLACK'], px, py)
