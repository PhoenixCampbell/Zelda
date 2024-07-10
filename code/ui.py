import pygame
from settings import *


class UI:
    def __init__(self):
        # gen
        self.displaySurface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # bar style
        self.healthBarRect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energyBarRect = pygame.Rect(10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)

    def showBar(self, current, maxAmount, bgRect, colour):
        # drawbg
        pygame.draw.rect(self.displaySurface, UI_BG_COLOUR, bgRect)

        # draw bar

    def display(self, player):
        self.showBar(
            player.health, player.stats["health"], self.healthBarRect, HEALTH_COLOUR
        )
        self.showBar(
            player.energy, player.stats["energy"], self.energyBarRect, ENERGY_COLOUR
        )
