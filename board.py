import pygame
import random
from shape import Shape

# Constants for the game board
height = 20
width = 10
shapes = [0, 1, 2, 3, 4, 5, 6]

class Board:

	def __init__(self) -> None:
		self.color = (160, 160, 160)
		self.size = 30 # Pixel width of each grid cell
		self.pos = (100, 100) # Position of the board on the screen 
		self.shapes = [] # Bag of shape options (so 1 pieces doesn't appear more than 2 times in a row)
		self.full_cells = {} # Dictionary to track filled cells and their colors
		self.game_over = False
		self.score = 0
		self.spawn_piece() # Spawns the first piece

	# Creates a new piece at the top of the grid
	def spawn_piece(self) -> None:
		if len(self.shapes) == 0:
			self.shapes = shapes.copy()
			random.shuffle(self.shapes) # Shuffles the 'bag' of shape options
		self.piece = Shape(self.shapes.pop(0))
		self.piece_pos = [2, 0]
		if not self.valid_pos():
			self.game_over = True # If the initial piece is invalid then the game is over
		self.score += 10

	# Fills in a square in the grid by coordinate
	def draw_square(self, surf: pygame.Surface, color: tuple, pos: tuple) -> None:
		x = self.pos[0] + (self.size * pos[0]) + 1
		y = self.pos[1] + (self.size * pos[1]) + 1
		pygame.draw.rect(surf, color, (x, y, self.size - 1, self.size - 1))

	# Draws lines representing the grid of the board
	def draw_grid(self, surf: pygame.Surface) -> None:
		for i in range(self.pos[0], self.pos[0] + 1 + (width * self.size), self.size):
			pygame.draw.line(surf, self.color, (i, self.pos[1]), (i, self.pos[1] + (height * self.size)))
		for i in range(self.pos[1], (height * self.size) + self.pos[1] + 1, self.size):
			pygame.draw.line(surf, self.color, (self.pos[0], i), (self.pos[0] + (width * self.size), i))
		for coord in self.full_cells:
			self.draw_square(surf, self.full_cells[coord], coord)

	# Uses the function for filling a single cell to draw the moving piece
	def draw_piece(self, surf: pygame.Surface) -> None:
		for coord in self.piece.squares():
			self.draw_square(surf, self.piece.color, (coord[0] + self.piece_pos[0], coord[1] + self.piece_pos[1]))

	# Determines if a piece is in a valid position
	def valid_pos(self) -> bool:
		for coord in self.piece.squares():
			abs_x = coord[0] + self.piece_pos[0]
			abs_y = coord[1] + self.piece_pos[1]
			if abs_x < 0 or abs_x > 9: return False # Piece is outside the left or right of the grid
			elif abs_y > 19: return False # Piece is lower than the bottom of te grid
			elif (abs_x, abs_y) in self.full_cells: return False # Piece is colliding with a filled cell
		return True
	
	# Moves the piece horizontally
	def move_x(self, dx: int) -> None:
		self.piece_pos[0] += dx
		if not self.valid_pos():
			self.piece_pos[0] -= dx # If the move resulted in an invalid position, move the piece back

	# Moves the piece vertically, returns whether or not the piece has stopped, and a new one has been spawned
	def move_y(self, dy: int) -> bool:
		self.piece_pos[1] += dy
		if self.valid_pos():
			return False
		# Everything below here means the piece has collided with the bottom of the grid or a filled cell
		self.piece_pos[1] -= dy
		for coord in self.piece.squares():
			# Add the piece's cells to the full cells dict
			self.full_cells[(coord[0] + self.piece_pos[0], coord[1] + self.piece_pos[1])] = self.piece.color
			self.clear_lines() # Once the piece stops we also check if any lines can be cleared
		self.spawn_piece() # And spawn a new piece
		return True
	
	# Rotates the piece and makes sure its a valid position (1 for clockwise, -1 for counter-clockwise)
	def rotate(self, direction: int) -> None:
		self.piece.rotate(direction)
		if not self.valid_pos():
			self.piece.rotate(-direction) # Undo the rotation if it moved it into an invalid position

	# Draws the grid and the current piece
	def update(self, surf: pygame.Surface) -> None:
		self.draw_grid(surf)
		self.draw_piece(surf)

	# Clears a line in the grid and moves the above pieces one down, returns whether a row was cleared or not (for score)
	def clear_line(self, row: int) -> bool:
		for col in range(width):
			if (col, row) not in self.full_cells:
				return False # Exit if any pieces in the row are not filled
				
		for col in range(width):
			self.full_cells.pop((col, row)) # Remove each cell from the row

		for k in range(row, 0, -1):
			for col in range(width):
				if (col, k - 1) in self.full_cells:
					self.full_cells[(col, k)] = self.full_cells[(col, k - 1)] # Shift all cells above the removed row, down
					self.full_cells.pop((col, k - 1))

		return True

	# Clears all full lines and increases score for all the lines cleared
	def clear_lines(self) -> None:
		score_multiplier = 1
		for row in range(height):
			if self.clear_line(row):
				self.score += 100 * score_multiplier
				score_multiplier += 1