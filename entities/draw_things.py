import pygame
import sys

pygame.font.init()

WHITE = (255,255,255)
GRAY = (129, 131, 132,200)
keyboard = [
    ["Q","W","E","R","T","Y","U","I","O","P"],
    ["A","S","D","F","G","H","J","K","L"],
    "ENTER",
    ["Z","X","C","V","B","N","M"],
    "DELETE"
]



def draw_rect(screen,color, rect, d = 0,r = 0):
    x,y,w,h = rect
    alpha_surface = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.rect(alpha_surface,color,(0,0,w,h),width = d, border_radius = r)
    screen.blit(alpha_surface, (x, y))

def draw_a_character_inside_a_box(screen,text,rect,color,font = pygame.font.SysFont(None, 48)):
    rect = pygame.Rect(rect)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)  
    draw_rect(screen, color, rect)
    screen.blit(text_surface, text_rect)

class button:
    def __init__(self, rect, name,font = pygame.font.SysFont(None, 48)):
        self.rect = pygame.Rect(rect)
        self.name = name
        self.color = GRAY
        self.font = font
    def draw(self,screen):
        draw_a_character_inside_a_box(screen, self.name,self.rect,self.color,self.font)
    def is_mouse_on(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

kb_dict = {}

def create_kb(screen):
    w,w2,h,d,d2 = 44,65,58,6,8
    width,height = screen.get_size()
    x = width/2-5*w-4.5*d
    y = height-200
    for i in keyboard[0]:
        kb_dict[i] = button((x,y,w,h),i)
        x+= w + d
    y += h+d2
    x = width/2-4.5*w-4*d
    for i in keyboard[1]:
        kb_dict[i] = button((x,y,w,h),i)
        x+= w + d
    y += h+d2
    x = width/2-3.5*w - 4*d - w2
    kb_dict[keyboard[2]] = button((x,y,w2,h),keyboard[2],font = pygame.font.SysFont(None, 24))
    x+=w2+d
    for i in keyboard[3]:
        kb_dict[i] = button((x,y,w,h),i)
        x+= w + d
    kb_dict[keyboard[4]] = button((x,y,w2,h),keyboard[4],font = pygame.font.SysFont(None, 20))


def draw_kb(screen):#kb_color = 0 =>kb_color[text], -1 => dark kb_color[text], 1=> yellow, 2=> green
    for i in kb_dict:
        kb_dict[i].draw(screen)


def draw_maingame(screen,character_box_color,character):
    screen_width, screen_height = screen.get_size()
    size = 59
    distance = 6
    y=10
    for i in range(6):
        x = screen_width/2 - size*5/2 - distance*2
        for j in range(5):
            if(len(character[i])<=j):
                ch = ""
            else:
                ch = character[i][j]
            draw_a_character_inside_a_box(screen,ch,(x,y,size,size),character_box_color[i][j])
            x+=size+distance
        y+=distance+size
