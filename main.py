import pygame

from vector_field import *
from vector import *
from render_pendulum import *
from transform import *
from global_values import *

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode(screen_size)

music = pygame.mixer.music.load('shallow.mp3')
pygame.mixer.music.play(-1)

def field_func(pos: Vector) -> Vector:
    '''
    This is the function that defines the vector field.
    Each position of the screen is associated with what
    this function returns.

    The function should return the gradient of a state
    field.
    '''
    x, y = transform(pos).array;

    # infection_rate = 0.02
    # removal_rate = 0.1
    # dx = -infection_rate*x*y
    # dy = infection_rate*x*y - removal_rate*y

    # dx = 0.2 * x - 0.01 * y**0.5 * x
    # dy = 0.0025 * x**0.5 * y - 0.05 * y

    dx = y
    dy = -0.2 * y - 2 * math.sin(x)

    return Vector([dx, dy]).div(res).scale(5.0)


vector_field = Vector_Field(screen, field_func)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            # Add a special particle
            # TODO: play sound effect
            pos = pygame.mouse.get_pos()
            x, y = pos
            vector_field.add_particle(Particle(pos=[x, screen_h - y], special=True))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                # Remove the special particle
                # TODO: play sound effect
                vector_field.remove_particle()

    screen.fill((0, 0, 0))

    # Show and update the fector field
    vector_field.show()
    for _ in range(res):
        vector_field.update()
    
    particle = vector_field.particles[0]
    if particle.special:
        # Only show a pendulum if the first particle is special
        # The particle's x position represents the pendulum's angle
        angle = transform(particle.pos).x
        render_pendulum(
            screen,
            angle,
            ball=particle.color
        )

    pygame.display.flip()

pygame.quit()
