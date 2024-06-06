
shapes = [
	[[(2, 2), (3, 2), (2, 3), (3, 3)]],

	[[(2, 2), (3, 2), (1, 3), (2, 3)],
	 [(2, 1), (2, 2), (3, 2), (3, 3)]],

	[[(1, 2), (2, 2), (2, 3), (3, 3)],
	 [(3, 1), (2, 2), (3, 2), (2, 3)]],

	[[(1, 1), (2, 1), (3, 1), (4, 1)],
	 [(2, 0), (2, 1), (2, 2), (2, 3)]],

	[[(1, 1), (1, 2), (2, 2), (3, 2)],
	 [(2, 1), (3, 1), (2, 2), (2, 3)],
	 [(1, 2), (2, 2), (3, 2), (3, 3)],
	 [(2, 1), (2, 2), (1, 3), (2, 3)]],

	[[(3, 1), (1, 2), (2, 2), (3, 2)],
	 [(2, 1), (2, 2), (2, 3), (3, 3)],
	 [(1, 2), (2, 2), (3, 2), (1, 3)],
	 [(1, 1), (2, 1), (2, 2), (2, 3)]],

	[[(2, 1), (1, 2), (2, 2), (3, 2)],
	 [(2, 1), (2, 2), (3, 2), (2, 3)],
	 [(1, 2), (2, 2), (3, 2), (2, 3)],
	 [(2, 1), (1, 2), (2, 2), (2, 3)]]
]

shape_colors = [
	(255, 255, 0), 
	(0, 255, 0), 
	(255, 0, 0), 
	(0, 255, 255), 
	(255, 165, 0), 
	(0, 0, 255), 
	(128, 0, 128)
]


class Shape:

	def __init__(self, shape_num) -> None:
		self.shape_num = shape_num
		self.orientation = 0
		self.pos = [2, 0]
		self.shape = shapes[self.shape_num]
		self.color = shape_colors[self.shape_num]

	# Figues out hw far to move a piece back if it is extended past the edge of the board
	def outside_grid(self, x_or_y, edge) -> int:
		moveback = 0
		for square in self.shape[self.orientation]:
			abs_pos = square[x_or_y] + self.pos[x_or_y]
			moveback = 0 - abs_pos if abs_pos < 0 and (0 - abs_pos) > moveback else moveback
			moveback = edge - abs_pos if abs_pos > edge and (edge - abs_pos) < moveback  else moveback
		return moveback


	def rotate(self, direction) -> None:
		self.orientation = (self.orientation + direction) % len(self.shape)
		self.pos[0] += self.outside_grid(0, 9)
		self.pos[1] += self.outside_grid(1, 19)


	def scoot(self, direction) -> None:
		self.pos[0] += direction
		self.pos[0] += self.outside_grid(0, 9)


	def drop(self) -> None:
		self.pos[1] += 1
		self.pos[1] += self.outside_grid(1, 19)


	def draw(self, board, surf) -> None:
		for square in self.shape[self.orientation]:
			board.draw_square(surf, self.color, (square[0] + self.pos[0], square[1] + self.pos[1]))

