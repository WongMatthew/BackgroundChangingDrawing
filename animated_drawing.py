# animated_drawing.py
# Author: Matt Wong

import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GRASS_GREEN = (142, 198, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600

pygame.init()

# ----- SCREEN PROPERTIES
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Animated Drawing")

# ----- VARIABLES
done = False
clock = pygame.time.Clock()

grass = pygame.Rect(0, 440, WIDTH, (HEIGHT - 440))

background = pygame.Color(SKY_BLUE[0], SKY_BLUE[1], SKY_BLUE[2])
yellow = pygame.Color(YELLOW[0], YELLOW[1], YELLOW[2])
background_h, background_s, background_l, background_a = background.hsla
background_vector = 0.5

list_of_stars = []
number_of_stars = 100
twinkle_factor = 20

for i in range(number_of_stars):
    list_of_stars.append(
        [
            random.randrange(0, WIDTH),
            random.randrange(0, HEIGHT),
            random.randrange(50, 255),
            random.choice([True, False])
        ]
    )

# ----- MAIN LOOP
while not done:
    # -- Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # ----- LOGIC
    # Dark to Light to Dark
    if background.hsla[2] + background_vector >= background_l:
        background_vector = -background_vector
    elif background.hsla[2] + background_vector < 0:
        background_vector = -background_vector

    background.hsla = (
        background_h,
        background_s,
        background.hsla[2] + background_vector,
        background_a,
    )

    # ----- DRAW
    screen.fill(background)

    for i in range(len(list_of_stars)):
        print(list_of_stars[i][2])
        pygame.draw.circle(
            screen,
            yellow,
            (list_of_stars[i][0], list_of_stars[i][1]),
            2,
        )

        # star_brightness = list_of_stars[i][2]
        
        # if star_brightness + twinkle_factor > 255 or star_brightness + twinkle_factor < 25:
        #     list_of_stars[i][3] = not list_of_stars[i][3]

        # dimming = list_of_stars[i][3]

        # if dimming:
        #     list_of_stars[i][2] += twinkle_factor
        # else:
        #     list_of_stars[i][2] -= twinkle_factor
        


    pygame.draw.rect(screen, GRASS_GREEN, grass)

    
    # ----- UPDATE
    pygame.display.flip()
    clock.tick(60)


pygame.quit()