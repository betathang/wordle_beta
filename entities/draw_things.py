import pygame
import sys

pygame.font.init()

WHITE = (255,255,255)
keyboard = [
    ["Q","W","E","R","T","Y","U","I","O","P"],
    ["A","S","D","F","G","H","J","K","L"],
    "ENTER",
    ["Z","X","C","V","B","N","M"],
    "⌫"
]

font = pygame.font.SysFont(None, 48) # letter

def draw_rect(screen,color, rect, d = 0,r = 0):
    x,y,w,h = rect
    alpha_surface = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.rect(alpha_surface,color,(0,0,w,h),width = d, border_radius = r)
    screen.blit(alpha_surface, (x, y))

def draw_a_character_inside_a_box(screen,text,x,y,w,h,color):
    rect = pygame.Rect(x, y, w, h)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)  
    draw_rect(screen, color, rect)
    screen.blit(text_surface, text_rect)

def draw_kb(screen,kb_color):#kb_color = 0 =>kb_color[text], -1 => dark kb_color[text], 1=> yellow, 2=> green

    rect_height = 58
    rect_width = 44
    rect_distance = 6
    screen_width, screen_height = screen.get_size()


    #draw the keyboard
    #first collum
    y =screen_height-200
    x = screen_width/2 - 5*rect_width - 4.5*rect_distance
    for i in range(0,10):
        draw_a_character_inside_a_box(screen, keyboard[0][i],x,y,rect_width,rect_height,kb_color[keyboard[0][i]])
        x += rect_width + rect_distance

    #second collum
    y+= rect_height + rect_distance/6*8
    x = screen_width/2 - 4.5*rect_width - 4*rect_distance

    for i in range(0,9):
        draw_a_character_inside_a_box(screen, keyboard[1][i],x,y,rect_width,rect_height,kb_color[keyboard[1][i]])
        
        x += rect_width + rect_distance
    y+= rect_height + rect_distance/6*8
    x = screen_width/2 - 3.5*rect_width - 4*rect_distance-65

    #thirt collum
    #enter
    rect = pygame.Rect(x, y, 65, rect_height)
    x += 65 + rect_distance
    text = keyboard[2]
    draw_rect(screen, kb_color[text], rect)
    text_surface = pygame.font.SysFont(None, 24).render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)  
    screen.blit(text_surface, text_rect)


    for i in range(0,7):
        draw_a_character_inside_a_box(screen, keyboard[3][i],x,y,rect_width,rect_height,kb_color[keyboard[3][i]])

        x += rect_width + rect_distance
    
    #backspace rect
    rect = pygame.Rect(x, y, 65, rect_height)
    draw_rect(screen, kb_color["BACKSPACE"], rect)
    x += 65 + rect_distance
    text = keyboard[4]
    text_surface = text_surface = pygame.font.SysFont("Segoe UI Symbol", 28).render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    text_rect.y-=2  #not true
    screen.blit(text_surface, text_rect)


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
            draw_a_character_inside_a_box(screen,ch,x,y,size,size,character_box_color[i][j])
            x+=size+distance
        y+=distance+size
