from typing import Iterable, Union
import pygame
from pygame.sprite import AbstractGroup
from settings import *
from tile import Tile
from player import Player
from debug import debug


class Level:
    def __init__(self):
        # sprite group setup
        self.visibleSprites = YSortCameraGroup()
        self.obstacleSprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for rowIndex, row in enumerate(worldMap):
            for colIndex, col in enumerate(row):
                x = colIndex * TILESIZE
                y = rowIndex * TILESIZE
                if col == "x":
                    Tile((x, y), [self.visibleSprites, self.obstacleSprites])
                if col == "p":
                    self.player = Player(
                        (x, y), [self.visibleSprites], self.obstacleSprites
                    )

    def run(self):
        # update and draw the game
        self.visibleSprites.customDraw(self.player)
        self.visibleSprites.update()
        #!debug(self.player.direction) debug for player direction


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # gen setup
        super().__init__()
        self.displaySurface = pygame.display.get_surface()
        self.halfWidth = self.displaySurface.get_size()[0] // 2
        self.halfHeight = self.displaySurface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def customDraw(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.halfWidth
        self.offset.y = player.rect.centery - self.halfHeight

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offsetPos = sprite.rect.topleft - self.offset
            self.displaySurface.blit(sprite.image, offsetPos)
