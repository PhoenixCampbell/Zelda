import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug


class Level:
	def __init__(self):

		# get the display surface 
		self.displaySurface = pygame.display.get_surface()

		# sprite group setup
		self.visibleSprites = pygame.sprite.Group()
		self.obstacleSprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	def create_map(self):
		for rowIndex,row in enumerate(worldMap):
			for colIndex, col in enumerate(row):
				x = colIndex * TILESIZE
				y = rowIndex * TILESIZE
				if col == 'x':
					Tile((x,y),[self.visibleSprites,self.obstacleSprites])
				if col == 'p':
					self.player = Player((x,y),[self.visibleSprites])

	def run(self):
		# update and draw the game
		self.visibleSprites.draw(self.displaySurface)
		self.visibleSprites.update()
		debug(self.player.direction)