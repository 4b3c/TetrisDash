import pygame
import time
from board import Board
from user_input import UserInput
from particles import ParticleSystem
pygame.init()


window = pygame.display.set_mode((1100, 800))
pause = 0.6

input_handler = UserInput()
particlesystem = ParticleSystem(window)
game_board = Board(particlesystem)

last_time = time.time()


while True:
	window.fill((20, 30, 40))
	game_board.update(window)
	particlesystem.draw_particles()
	pygame.display.flip()

	if (time.time() - last_time) > pause:
		game_board.move_y(1)
		if game_board.game_over:
			game_board = Board()
		last_time = time.time()

	input_handler.update(pygame.key.get_pressed())
	if input_handler.state("up"):
		game_board.rotate(1)
	elif input_handler.state("left"):
		game_board.move_x(-1)
	elif input_handler.state("down"):
		game_board.move_y(1)
	elif input_handler.state("right"):
		game_board.move_x(1)
	elif input_handler.state("drop"):
		while not game_board.move_y(1):
			pass


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()