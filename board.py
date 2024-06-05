import pygame

grid_color = (100, 100, 100)
grid_size = 30
grid_width = 10
grid_height = 20
grid_pos = (100, 100)


def draw_grid(surf):
	for i in range(grid_pos[0], grid_pos[0] + 1 + (grid_width * grid_size), grid_size):
		pygame.draw.line(surf, grid_color, (i, grid_pos[1]), (i, grid_pos[1] + (grid_height * grid_size)))

	for i in range(grid_pos[1], (grid_height * grid_size) + grid_pos[1] + 1, grid_size):
		pygame.draw.line(surf, grid_color, (grid_pos[0], i), (grid_pos[0] + (grid_width * grid_size), i))

def draw_square(surf, color, pos):
	x = grid_pos[0] + (grid_size * pos[0]) + 1
	y = grid_pos[1] + (grid_size * pos[1]) + 1
	
	pygame.draw.rect(surf, color, (x, y, grid_size - 1, grid_size - 1))
