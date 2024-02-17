from csv import reader
from os import walk
import pygame


def importCSVLayout(path):
    terrainMap = []
    with open(path) as levelMap:
        layout = reader(levelMap, delimiter=",")
        for row in layout:
            terrainMap.append(list(row))
        return terrainMap


def importFolder(path):
    surfaceList = []

    for _, __, imgFiles in walk(path):
        for image in imgFiles:
            fullPath = path + "/" + image
            imageSurf = pygame.image.load(fullPath).convert_alpha()
            surfaceList.append(imageSurf)
        return surfaceList
