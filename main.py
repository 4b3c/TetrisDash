import pygame
import time
import board
import shape
pygame.init()


window = pygame.display.set_mode((1100, 900))
pause = 0.8

new_shape = shape.Shape()
last_time = time.time()


while True:
	window.fill((0, 0, 0))
	board.draw_grid(window)
	new_shape.draw(window)
	pygame.display.flip()

	if (time.time() - last_time) > pause:
		new_shape.drop()
		last_time = time.time()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			new_shape.rotate(1)