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
		self.full_cells = {}
		self.game_over = False
		self.score = 0
		self.spawn_piece()

	# Creates a new piece at the top of the grid
	def spawn_piece(self):
		if len(self.shapes) == 0:
			self.shapes = shapes.copy()
			random.shuffle(self.shapes)
		self.piece = Shape(self.shapes.pop(0))
		self.piece_pos = [2, 0]
		if not self.valid_pos():
			self.game_over = True
		self.score += 10

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

		for coord in self.full_cells:
			self.draw_square(surf, self.full_cells[coord], coord)

	# Uses the function for filling a single cell to draw the shape of the moving piece
	def draw_piece(self, surf):
		for coord in self.piece.squares():
			self.draw_square(surf, self.piece.color, (coord[0] + self.piece_pos[0], coord[1] + self.piece_pos[1]))

	# Determines if a pice is in a valid position
	def valid_pos(self) -> bool:
		for coord in self.piece.squares():
			abs_x = coord[0] + self.piece_pos[0]
			abs_y = coord[1] + self.piece_pos[1]
			if abs_x < 0 or abs_x > 9: return False
			elif abs_y > 19: return False
			elif (abs_x, abs_y) in self.full_cells: return False
		return True
	
	def move_x(self, dx) -> None:
		self.piece_pos[0] += dx
		if not self.valid_pos():
			self.piece_pos[0] -= dx

	def move_y(self, dy) -> bool:
		self.piece_pos[1] += dy
		if self.valid_pos():
			return False
		self.piece_pos[1] -= dy
		for coord in self.piece.squares():
			self.full_cells[(coord[0] + self.piece_pos[0], coord[1] + self.piece_pos[1])] = self.piece.color
			self.clear_lines()
		self.spawn_piece()
		return True

	def rotate(self, direction) -> None:
		self.piece.rotate(direction)
		if not self.valid_pos():
			self.piece.rotate(-direction)

	def update(self, surf) -> None:
		self.draw_grid(surf)
		self.draw_piece(surf)

	def clear_line(self, i) -> bool:
		for j in range(width):
			if (j, i) not in self.full_cells:
				return False
		for j in range(width):
			self.full_cells.pop((j, i))

		for k in range(i, 0, -1):
			for j in range(width):
				if (j, k - 1) in self.full_cells:
					self.full_cells[(j, k)] = self.full_cells[(j, k - 1)]
					self.full_cells.pop((j, k - 1))


	def clear_lines(self) -> None:
		score_multiplier = 1
		for i in range(height):
			if self.clear_line(i):
				self.score += 100 * score_multiplier
				score_multiplier += 1