import pygame
import constant as con


class Player:
    spark_images = [pygame.transform.scale(con.IMAGES[name], (90, 90)) for name in con.IMAGES if "SPARK" in name]

    def __init__(self, token):
        self.token = token
        self.tokens = pygame.sprite.Group()
        self.points = 0
        self.rect = self.token.rect
        self.rect.center = (con.WIDTH/2, con.TOKEN_SIZE * 1.5)
        self.spark_image = self.__class__.spark_images[0]
        self._spark_count = 0

    def draw(self, surface):
        surface.blit(self.token.image, self.rect)
        surface.blit(self.spark_image, self.rect)

    def set_rect_center(self, x, y):
        self.rect.center = x, y

    def update(self):
        self._animate()

    def _animate(self):
        self.spark_image = self.__class__.spark_images[self._spark_count // 4]
        self._spark_count = (self._spark_count + 1) % (4 * len(self.__class__.spark_images))
