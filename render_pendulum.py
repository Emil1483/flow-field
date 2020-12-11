import pygame
import math

from color_utils import *

def render_pendulum(screen, size, angle, alpha=1.0, ball=(25, 121, 169)):
    '''
    Renders a pendulum at the bottom right of the screen,
    given a current angle.
    '''
    stick = (237, 184, 121)

    stick = color_with_alpha(stick, alpha)
    ball = color_with_alpha(ball, alpha)

    ball_size = 20
    r = 200

    w, h = size
    center = (
        round(w - r - ball_size),
        round(h - r - ball_size)
    )

    center_x, center_y = center
    angle = angle + math.pi / 2
    end = (
        round(center_x + math.cos(angle) * r),
        round(center_y + math.sin(angle) * r)
    )

    pygame.draw.line(screen, stick, center, end, 5)
    pygame.draw.circle(screen, ball, end, ball_size)
