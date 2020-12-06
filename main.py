import pygame

from vector_field import *
from vector import *
from render_pendulum import *
from transform import *

res = 20

pygame.init()

screen_size = [1500, 900]
screen_w, screen_h = screen_size

screen = pygame.display.set_mode(screen_size)

def field_func(pos: Vector) -> Vector:
    x, y = transform(pos, screen_size).array;

    # infection_rate = 0.02
    # removal_rate = 0.1
    # dx = -infection_rate*x*y
    # dy = infection_rate*x*y - removal_rate*y

    # dx = 0.2 * x - 0.01 * y**0.5 * x
    # dy = 0.0025 * x**0.5 * y - 0.05 * y

    dx = y
    dy = -0.2 * y - 2 * math.sin(x)

    return Vector([dx, dy]).div(res).scale(5.0)


vector_field = Vector_Field(screen, screen_size, field_func)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x, y = pos
            vector_field.add_particle(Particle(screen_size, pos=[x, screen_h - y], special=True))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                vector_field.remove_particle()

    screen.fill((0, 0, 0))

    vector_field.show()
    for _ in range(res):
        vector_field.update()
    
    particle = vector_field.particles[0]
    if particle.special:
        angle = transform(particle.pos, screen_size).x
        render_pendulum(
            screen,
            screen_size,
            angle,
            ball=particle.color
        )

    pygame.display.flip()

pygame.quit()
