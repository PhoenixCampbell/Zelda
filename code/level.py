import pygame
from pygame.sprite import AbstractGroup
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from weapon import Weapon
from ui import UI


class Level:
    def __init__(self):

        self.displaySurface = pygame.display.get_surface()

        # sprite group setup
        self.visibleSprites = YSortCameraGroup()
        self.obstacleSprites = pygame.sprite.Group()

        # attack sprite
        self.currentAttack = None

        # sprite setup
        self.create_map()

        # user interface setup
        self.ui = UI()

    def create_map(self):
        layouts = {
            "boundary": importCSVLayout("./map/map_FloorBlocks.csv"),
            "grass": importCSVLayout("./map/map_Grass.csv"),
            "object": importCSVLayout("./map/map_LargeObjects.csv"),
        }
        graphics = {
            "grass": importFolder("./graphics/Grass"),
            "objects": importFolder("./graphics/objects"),
        }

        for style, layout in layouts.items():
            for rowIndex, row in enumerate(layout):
                for colIndex, col in enumerate(row):
                    if col != "-1":
                        x = colIndex * TILESIZE
                        y = rowIndex * TILESIZE
                        if style == "boundary":
                            Tile(
                                (x, y),
                                [self.obstacleSprites],
                                "invisible",
                            )
                        if style == "grass":
                            randomGrassImage = choice(graphics["grass"])
                            Tile(
                                (x, y),
                                [self.visibleSprites, self.obstacleSprites],
                                "grass",
                                randomGrassImage,
                            )
                        if style == "object":
                            surf = graphics["objects"][int(col)]
                            Tile(
                                (x, y),
                                [self.visibleSprites, self.obstacleSprites],
                                "object",
                                surf,
                            )
        self.player = Player(
            (2000, 1430),
            [self.visibleSprites],
            self.obstacleSprites,
            self.createAttack,
            self.destroyAttack,
            self.createMagic,
        )

    def createAttack(self):
        self.currentAttack = Weapon(self.player, [self.visibleSprites])

    def createMagic(self, style, strength, cost):
        print(style)
        print(strength)
        print(cost)

    def destroyAttack(self):
        if self.currentAttack:
            self.currentAttack.kill()
        self.currentAttack = None

    def run(self):
        # update and draw the game
        self.visibleSprites.customDraw(self.player)
        self.visibleSprites.update()
        self.ui.display(self.player)
        #!debug(self.player.direction) debug for player direction
        #!debug(self.player.status) check for different idle/attack types


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # gen setup
        super().__init__()
        self.displaySurface = pygame.display.get_surface()
        self.halfWidth = self.displaySurface.get_size()[0] // 2
        self.halfHeight = self.displaySurface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floorSurf = pygame.image.load("./graphics/tilemap/ground.png").convert()
        self.floorRect = self.floorSurf.get_rect(topleft=(0, 0))

    def customDraw(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.halfWidth
        self.offset.y = player.rect.centery - self.halfHeight

        # drawing the floor
        floorOffsetPos = self.floorRect.topleft - self.offset
        self.displaySurface.blit(self.floorSurf, floorOffsetPos)

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offsetPos = sprite.rect.topleft - self.offset
            self.displaySurface.blit(sprite.image, offsetPos)
