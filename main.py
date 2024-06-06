import pygame
import time
import board
import shape
pygame.init()


window = pygame.display.set_mode((1100, 800))
pause = 0.2

game_board = board.Board()
new_shape = shape.Shape(4)
last_time = time.time()


while True:
	window.fill((20, 30, 40))
	game_board.draw_grid(window)
	new_shape.draw(game_board, window)
	pygame.display.flip()

	if (time.time() - last_time) > pause:
		new_shape.drop()
		last_time = time.time()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			new_shape.rotate(1)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			new_shape.rotate(-1)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			new_shape.scoot(1)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			new_shape.scoot(-1)