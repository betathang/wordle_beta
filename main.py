import pygame
import sys
from entities.boardcast import boardcast
from entities.draw_things import *
from wordfreq import top_n_list
from entities.background import background_works
import random

pygame.init()

screen_width = 518
screen_height = 600

#icon = pygame.image.load("icon.png")
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("WOORRRRDDDDLLLLLLEEEE")



background_main = background_works("entities/entity2/3.jpg",screen_width,screen_height)

box_height = 58
box_width = 44
box_distance = 6

WHITE = (255,255,255)
GRAY = (129, 131, 132,200)
DARK_GRAY = (58, 58, 60, 200)
YELLOW = (181,159,59,200)
GREEN = (83,141,78,200)
BLACK = (0,0,0)

clock = pygame.time.Clock()

word = []
for i in range(0,6):
    word.append("")

all_words = top_n_list("en", 500000)
valid_words_list = [w.upper() for w in all_words if len(w) == 5]
valid_words_set = set(valid_words_list)

line = 0
keyboard_input_idk = {}
kb_color = {}
dt = 0 
for i in range(ord("a"), ord('z') + 1):
    kb_color[(chr(i)).upper()] = GRAY
kb_color["ENTER"] = GRAY
kb_color["BACKSPACE"] = GRAY
#used_key = 0 =>gray, -1 => dark gray, 1=> yellow, 2=> green

character_box_color = [[GRAY for _ in range(5)] for _ in range(6)]



running = True
reason_of_stop_running = None

answer = random.choice(valid_words_list)

bc = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
            reason_of_stop_running = 0
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key).upper()
            if pygame.K_a <= event.key <= pygame.K_z and len(word[line])<5:
                word[line] = word[line] + key_name.upper()
            elif event.key == pygame.K_BACKSPACE:
                word[line] = word[line][:-1]
            elif event.key == pygame.K_RETURN:
                if len(word[line])<5:
                    for i in bc:
                        i.y += 30
                    bc = [boardcast("5 characters word ONLY")] + bc
                elif word[line] not in valid_words_set:
                    for i in bc:
                        i.y += 30
                    bc = [boardcast("TF is this word?")] + bc
                else:
                    tmp = list(answer)
                    for i in range(5):
                        if(word[line][i]==answer[i]):
                            tmp.remove(answer[i])
                            character_box_color[line][i] = GREEN
                            kb_color[word[line][i]] = GREEN
                    for i in range(5):
                        if word[line][i]!=answer[i]:
                            if word[line][i] in tmp:
                                tmp.remove(word[line][i])
                                character_box_color[line][i] = YELLOW
                                if(kb_color[word[line][i]] == GRAY):
                                    kb_color[word[line][i]] = YELLOW
                            else:
                                character_box_color[line][i] = DARK_GRAY
                                if(kb_color[word[line][i]]==GRAY):
                                    kb_color[word[line][i]] = DARK_GRAY
                    
                    if(word[line] == answer):
                        running = False
                        reason_of_stop_running = 2
                        break
                    line += 1
                    if(line == 6):
                        running = False
                        reason_of_stop_running = 1
 


                

    #BACKGROUND WORK
    background_main.draw(screen,dt)

    draw_kb(screen,kb_color)
    draw_maingame(screen,character_box_color,word)

    for i in range(len(bc)):
        bc[i].show(screen, dt)
    if(len(bc)>0 and bc[-1].timeout<0):
        bc.pop()
    dt = clock.tick()
    #print(1000/dt)
    #print(dt)
    pygame.display.flip()
#cd D:/for learning ofc/pyham/wordle/main.py

if(reason_of_stop_running == 1 or reason_of_stop_running == 2):
    running = True
    timeout = 3000
    if reason_of_stop_running == 1:
        bc= [boardcast("YOU STUPID LUSER")] + bc
        bc[0].timeout = 5000
        bc[0].y +=20
        bc= [boardcast("The correct word is " + answer)] + bc
        bc[0].timeout = 5000
    elif reason_of_stop_running == 2:
        bc= [boardcast("Orz")] + bc
        bc[0].timeout = 5000
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                running = False

        background_main.draw(screen,dt)
        draw_kb(screen,kb_color)
        draw_maingame(screen,character_box_color,word)


        for i in range(len(bc)):
            bc[i].show(screen, dt)
        if(len(bc)>0 and bc[-1].timeout<0):
            bc.pop()

        dt = clock.tick()
        timeout -= dt
        if(timeout < 0):
            running = False
        
        pygame.display.flip()
    

pygame.quit()
sys.exit()
