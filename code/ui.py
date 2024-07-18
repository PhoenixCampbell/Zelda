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

        # conv. weapon dic
        self.weaponGraphic = []
        for weapon in weaponData.values():
            path = weapon["graphic"]
            weapon = pygame.image.load(path).convert_alpha()
            self.weaponGraphic.append(weapon)

    def showBar(self, current, maxAmount, bgRect, colour):
        # drawbg
        pygame.draw.rect(self.displaySurface, UI_BG_COLOUR, bgRect)

        # convertion: stat to pixel
        ratio = current / maxAmount
        currentWidth = bgRect.width * ratio
        currentRect = bgRect.copy()
        currentRect.width = currentWidth

        # draw bar
        pygame.draw.rect(self.displaySurface, colour, currentRect)
        pygame.draw.rect(self.displaySurface, UI_BORDER_COLOUR, bgRect, 3)

    def showExp(self, exp):
        textSurf = self.font.render(str(int(exp)), False, TEXT_COLOUR)
        x = self.displaySurface.get_size()[0] - 20
        y = self.displaySurface.get_size()[1] - 20
        textRect = textSurf.get_rect(bottomright=(x, y))

        pygame.draw.rect(self.displaySurface, UI_BG_COLOUR, textRect.inflate(20, 20))
        self.displaySurface.blit(textSurf, textRect)
        pygame.draw.rect(
            self.displaySurface, UI_BORDER_COLOUR, textRect.inflate(20, 20), 3
        )

    def selectionBox(self, left, top, hasSwitched):
        bgRect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.displaySurface, UI_BG_COLOUR, bgRect)
        if hasSwitched:
            pygame.draw.rect(self.displaySurface, UI_BORDER_COLOUR_ACTIVE, bgRect, 3)
        else:
            pygame.draw.rect(self.displaySurface, UI_BORDER_COLOUR, bgRect, 3)
        return bgRect

    def weaponOverlay(self, weaponIndex, hasSwitched):
        bgRect = self.selectionBox(10, 630, hasSwitched)
        weaponSurf = self.weaponGraphic[weaponIndex]
        weaponRect = weaponSurf.get_rect(center=bgRect.center)
        self.displaySurface.blit(weaponSurf, weaponRect)

    def display(self, player):
        self.showBar(
            player.health, player.stats["health"], self.healthBarRect, HEALTH_COLOUR
        )
        self.showBar(
            player.energy, player.stats["energy"], self.energyBarRect, ENERGY_COLOUR
        )
        self.showExp(player.exp)
        self.weaponOverlay(player.weaponIndex, not player.canSwitchWeapon)
        # self.selectionBox(80, 635)
