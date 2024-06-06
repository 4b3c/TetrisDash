import pygame
import time
import board
import shape
pygame.init()


window = pygame.display.set_mode((1100, 800))
pause = 0.2

game_board = board.Board()
last_time = time.time()


while True:
	window.fill((20, 30, 40))
	game_board.update(window)
	pygame.display.flip()

	if (time.time() - last_time) > pause:
		game_board.move_y(1)
		last_time = time.time()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			game_board.rotate(1)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			game_board.rotate(-1)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			game_board.move_x(1)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			game_board.move_x(-1)