import pygame
from entities.draw_things import draw_rect

WHITE = (255,255,255)
GRAY = (129, 131, 132,200)
DARK_GRAY = (58, 58, 60, 200)
DARK_DARK_GRAY = (30, 30, 32,200)
YELLOW = (181,159,59,200)
GREEN = (83,141,78,200)
BLACK = (0,0,0,0)
bc_font = pygame.font.SysFont(None, 24)

class boardcast:
    def __init__(self, name, font = bc_font,  color = BLACK): #name = text
        self.text = name
        self.transparent_count = 200
        self.timeout = 2500
        if(len(color) == 4):
            color = color[:3]
        self.color  = color
        self.font = font
        self.is_bc = True
        self.y = 20
    def show(self, screen, dt):
        if self.is_bc == True:
            w,h = screen.get_size()
            if(self.timeout<=500):
                self.transparent_count = max(0,self.transparent_count - dt*0.4)
            self.timeout -= dt
            text_surface = self.font.render(self.text, True, WHITE)
            rect = text_surface.get_rect()
            rect.x, rect.y = w/2-rect.w/2,self.y
            draw_rect(screen, (*self.color,self.transparent_count), (rect.x-2,rect.y-1,rect.w + 4, rect.h + 2), r = 3)
            screen.blit(text_surface, rect)

