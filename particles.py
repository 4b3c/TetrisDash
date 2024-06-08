import pygame
import random

pygame.init()

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(4, 12)
        self.color = random.choice([(255, 255, 255), (255, 215, 0), (255, 69, 0), (0, 125, 125)])
        self.lifetime = random.randint(200, 800)
        self.velocity = [random.uniform(-0.15, 0.15), random.uniform(-0.15, 0.15)]

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.lifetime -= 1

    def draw(self, screen):
        if self.lifetime > 0:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.radius, self.radius)) 
            # pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


particles = []

def create_particles(pos):
    # for _ in range(20):  # Adjust the number of particles as needed
    particles.append(Particle(pos[0], pos[1]))

def update_particles():
    for particle in particles[:]:
        particle.update()
        if particle.lifetime <= 0:
            particles.remove(particle)

def draw_particles(screen):
    for particle in particles:
        particle.draw(screen)

screen = pygame.display.set_mode((1100, 800))

# In your main game loop:
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    if pygame.mouse.get_pressed()[0]:
        create_particles(pygame.mouse.get_pos())
    
    update_particles()
    screen.fill((0, 0, 0))  # Clear screen with black
    draw_particles(screen)
    
    pygame.display.flip()
