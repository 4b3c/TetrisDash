import random
import board

O = [[(2, 2), (3, 2), (2, 3), (3, 3)]]

S = [[(2, 2), (3, 2), (1, 3), (2, 3)],
     [(2, 1), (2, 2), (3, 2), (3, 3)]]

Z = [[(1, 2), (2, 2), (2, 3), (3, 3)],
	 [(3, 1), (2, 2), (3, 2), (2, 3)]]

I = [[(1, 1), (2, 1), (3, 1), (4, 1)],
	 [(2, 0), (2, 1), (2, 2), (2, 3)]]

J = [[(1, 1), (1, 2), (2, 2), (3, 2)],
	 [(2, 1), (3, 1), (2, 2), (2, 3)],
	 [(1, 2), (2, 2), (3, 2), (3, 3)],
	 [(2, 1), (2, 2), (1, 3), (2, 3)]]

L = [[(3, 1), (1, 2), (2, 2), (3, 2)],
	 [(2, 1), (2, 2), (2, 3), (3, 3)],
	 [(1, 2), (2, 2), (3, 2), (1, 3)],
	 [(1, 1), (2, 1), (2, 2), (2, 3)]]

T = [[(2, 1), (1, 2), (2, 2), (3, 2)],
	 [(2, 1), (2, 2), (3, 2), (2, 3)],
	 [(1, 2), (2, 2), (3, 2), (2, 3)],
	 [(2, 1), (1, 2), (2, 2), (2, 3)]]


shapes = [O, S, Z, I, J, L, T]
shape_colors = [(255, 255, 0), (0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


class Shape:

	def __init__(self) -> None:
		self.falling = True
		self.orientation = 0
		self.pos = [2, 0]
		self.shape_num = random.randint(0, 6)
		self.shape = shapes[self.shape_num]
		self.color = shape_colors[self.shape_num]
		print(self.color)


	def rotate(self, direction) -> None:
		self.orientation = (self.orientation + direction) % len(self.shape)

	def drop(self) -> None:
		if self.falling:
			self.pos[1] += 1


	def draw(self, surf) -> None:
		for square in self.shape[self.orientation]:
			board.draw_square(surf, self.color, (square[0] + self.pos[0], square[1] + self.pos[1]))

