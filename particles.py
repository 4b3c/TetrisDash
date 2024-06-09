import pygame
import random
import time

class Particle:

	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color
		self.size = random.randint(4, 12)
		self.lifetime = random.randint(200, 800)
		self.velocity = [random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)]


	def update(self):
		self.x += self.velocity[0]
		self.y += self.velocity[1]
		self.lifetime -= 1


	def draw(self, screen):
		if self.lifetime > 0:
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))


class ParticleSystem:

	def __init__(self, screen) -> None:
		self.screen = screen
		self.particles = []

	def add_particles(self, x, y, num, color):
		for _ in range(num):
			self.particles.append(Particle(x, y, color))

	def update_particles(self):
		for particle in self.particles:
			particle.update()
			if particle.lifetime <= 0:
				self.particles.remove(particle)

	def draw_particles(self):
		self.update_particles()
		for particle in self.particles:
			particle.draw(self.screen)

	def play_until_done(self, board):
		while len(self.particles) != 0:
			self.screen.fill((20, 30, 40))
			board.draw_grid(self.screen)
			self.update_particles()
			self.draw_particles()
			pygame.display.flip()
			time.sleep(0.004)
