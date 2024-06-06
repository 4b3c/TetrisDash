import pygame

height = 20
width = 10

class Board:

	def __init__(self) -> None:
		self.color = (160, 160, 160)
		self.size = 30
		self.pos = (100, 100)

	def draw_grid(self, surf):
		for i in range(self.pos[0], self.pos[0] + 1 + (width * self.size), self.size):
			pygame.draw.line(surf, self.color, (i, self.pos[1]), (i, self.pos[1] + (height * self.size)))

		for i in range(self.pos[1], (height * self.size) + self.pos[1] + 1, self.size):
			pygame.draw.line(surf, self.color, (self.pos[0], i), (self.pos[0] + (width * self.size), i))

	def draw_square(self, surf, color, pos):
		x = self.pos[0] + (self.size * pos[0]) + 1
		y = self.pos[1] + (self.size * pos[1]) + 1
		
		pygame.draw.rect(surf, color, (x, y, self.size - 1, self.size - 1))
