import pygame
import random

import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class background_works:
    def __init__(self, img_path,W,H):
        #for the image work
        self.img = pygame.image.load(resource_path(img_path))
        self.img = pygame.transform.scale(self.img, (W, H))
        self.width = W
        self.height = H
        
        #snow flakes work
        NUM_SNOWFLAKES = 100
        self.snowflakes = []

        for i in range(NUM_SNOWFLAKES):
            x = random.randrange(0, W)
            y = random.randrange(0, H)
            radius = random.randint(2, 5)
            speed = random.uniform(0.06, 0.18)
            self.snowflakes.append([x, y, radius, speed])


    def draw(self, screen,dt):
        #draw the image
        screen.blit(self.img, (0, 0))

        for flake in self.snowflakes:
            x, y, r, speed = flake

            y += speed*dt  # Fall down
            x += random.uniform(-0.03, 0.03)*dt  # Slight "wind" effect

            # If snowflake moves off screen → reset to the top
            if y > self.height:
                y = random.randrange(-30, -5)
                x = random.randrange(0, self.width)

            flake[0], flake[1] = x, y

            pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), r)
