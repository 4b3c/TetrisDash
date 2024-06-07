
# Contains coordinates for each shape for each rotation/orientation they can be in
shapes = [
	[[(2, 2), (3, 2), (2, 3), (3, 3)]], # O

	[[(2, 2), (3, 2), (1, 3), (2, 3)],
	 [(2, 1), (2, 2), (3, 2), (3, 3)]], # S

	[[(1, 2), (2, 2), (2, 3), (3, 3)],
	 [(3, 1), (2, 2), (3, 2), (2, 3)]], # Z

	[[(1, 1), (2, 1), (3, 1), (4, 1)],
	 [(2, 0), (2, 1), (2, 2), (2, 3)]], # I

	[[(1, 1), (1, 2), (2, 2), (3, 2)],
	 [(2, 1), (3, 1), (2, 2), (2, 3)],
	 [(1, 2), (2, 2), (3, 2), (3, 3)],
	 [(2, 1), (2, 2), (1, 3), (2, 3)]], # J

	[[(3, 1), (1, 2), (2, 2), (3, 2)],
	 [(2, 1), (2, 2), (2, 3), (3, 3)],
	 [(1, 2), (2, 2), (3, 2), (1, 3)],
	 [(1, 1), (2, 1), (2, 2), (2, 3)]], # L

	[[(2, 1), (1, 2), (2, 2), (3, 2)],
	 [(2, 1), (2, 2), (3, 2), (2, 3)],
	 [(1, 2), (2, 2), (3, 2), (2, 3)],
	 [(2, 1), (1, 2), (2, 2), (2, 3)]] # T
]

# Corresponding colors
shape_colors = [
	(230, 190, 0), # O
	(10, 180, 60), # S
	(210, 0, 0), # Z
	(0, 180, 200), # I
	(180, 110, 0), # J
	(0, 90, 190), # L
	(170, 0, 200) # T
]


class Shape:

	def __init__(self, shape_num: int) -> None:
		self.shape_num = shape_num # Number representing the index in the shapes list that is this shape
		self.orientation = 0 # The index of the rotation
		self.shape = shapes[self.shape_num]
		self.color = shape_colors[self.shape_num]

	# Iterates through the different rotations of each shape by incrementing the orientation variable
	def rotate(self, direction: int):
		self.orientation = (self.orientation + direction) % len(self.shape)

	# Gets all the coordinates for the cells in the shape in its current rotation/orientation
	def squares(self):
		return self.shape[self.orientation]

