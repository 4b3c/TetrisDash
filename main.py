import pygame
import time
import board
pygame.init()


window = pygame.display.set_mode((1100, 800))
pause = 0.2

game_board = board.Board()
last_time = time.time()
last_time_key_pressed = time.time()
pressed_keys = {
	pygame.K_w: False,
	pygame.K_a: False,
	pygame.K_s: False,
	pygame.K_d: False,
	pygame.K_UP: False,
	pygame.K_LEFT: False,
	pygame.K_DOWN: False,
	pygame.K_RIGHT: False,
	pygame.K_SPACE: False
}

while True:
	window.fill((20, 30, 40))
	game_board.update(window)
	pygame.display.flip()

	if (time.time() - last_time) > pause:
		game_board.move_y(1)
		if game_board.game_over:
			game_board = board.Board()
		last_time = time.time()

	if (time.time() - last_time_key_pressed) > 0.03:
		pressed_keys = {
			pygame.K_w: False,
			pygame.K_a: False,
			pygame.K_s: False,
			pygame.K_d: False,
			pygame.K_UP: False,
			pygame.K_LEFT: False,
			pygame.K_DOWN: False,
			pygame.K_RIGHT: False,
			pygame.K_SPACE: False
		}
		last_time_key_pressed = time.time()

	print(pressed_keys[pygame.K_SPACE])
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_SPACE] and not pressed_keys[pygame.K_SPACE]:
		if game_board.valid_pos():
			game_board.move_y(1)
			pressed_keys[pygame.K_SPACE] = True

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_w):
			game_board.rotate(1)
		elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
			game_board.move_x(1)
		elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
			game_board.move_x(-1)