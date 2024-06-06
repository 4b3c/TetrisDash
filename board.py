import pygame
import random
from shape import Shape

height = 20
width = 10
shapes = [0, 1, 2, 3, 4, 5, 6]

class Board:

	def __init__(self) -> None:
		self.color = (160, 160, 160)
		self.size = 30
		self.pos = (100, 100)
		self.shapes = []
		self.spawn_piece()
		self.full_cells = {}

	# Creates a new piece at the top of the grid
	def spawn_piece(self):
		if len(self.shapes) == 0:
			self.shapes = shapes.copy()
			random.shuffle(self.shapes)
		self.piece = Shape(self.shapes.pop(0))
		self.piece_pos = [2, 0]

	# Fills in a square in the grid by coordinate
	def draw_square(self, surf, color, pos):
		x = self.pos[0] + (self.size * pos[0]) + 1
		y = self.pos[1] + (self.size * pos[1]) + 1
		
		pygame.draw.rect(surf, color, (x, y, self.size - 1, self.size - 1))

	# Draws lines representing the grid of the board
	def draw_grid(self, surf):
		for i in range(self.pos[0], self.pos[0] + 1 + (width * self.size), self.size):
			pygame.draw.line(surf, self.color, (i, self.pos[1]), (i, self.pos[1] + (height * self.size)))

		for i in range(self.pos[1], (height * self.size) + self.pos[1] + 1, self.size):
			pygame.draw.line(surf, self.color, (self.pos[0], i), (self.pos[0] + (width * self.size), i))

	# Uses the function for filling a single cell to draw the shape of the moving piece
	def draw_piece(self, surf):
		for coord in self.piece.squares():
			self.draw_square(surf, self.piece.color, (coord[0] + self.piece_pos[0], coord[1] + self.piece_pos[1]))

	# Figues out how far to move a piece back if it is not in a valid position
	def valid_pos(self, x_or_y, edge) -> int:
		moveback = 0
		for coord in self.piece.squares():
			abs_pos = coord[x_or_y] + self.piece_pos[x_or_y]
			if abs_pos < 0 and (0 - abs_pos) > moveback:
				moveback = 0 - abs_pos
			elif abs_pos > edge and (edge - abs_pos) < moveback:
				moveback = edge - abs_pos
			elif coord in self.full_cells:
				moveback = -1

		return moveback
	
	def move_x(self, dx):
		self.piece_pos[0] += dx
		self.piece_pos[0] += self.valid_pos(0, 9)

	def move_y(self, dy):
		self.piece_pos[1] += dy
		moveback = self.valid_pos(1, 19)
		if moveback != 0:
			self.piece_pos[1] += moveback

	def rotate(self, direction) -> None:
		self.piece.rotate(direction)
		self.piece_pos[0] += self.valid_pos(0, 9)
		self.piece_pos[1] += self.valid_pos(1, 19)

	def update(self, surf):
		self.draw_grid(surf)
		self.draw_piece(surf)

	