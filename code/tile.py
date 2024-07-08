import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(
        self, pos, groups, spriteType, surface=pygame.Surface((TILESIZE, TILESIZE))
    ):
        super().__init__(groups)
        self.spriteType = spriteType
        self.image = surface
        if spriteType == "object":
            # offset
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
