# Frogger
# mosulok importálása
import pygame
import random
from pygame import time
from pygame.locals import *
from random import randrange
from operator import itemgetter
  
# pygame indítása
pygame.init()

# lejátszófelület adatainak megadása és beállítása 

screen = pygame.display.set_mode((128, 128))
WIDTH, HEIGTH = 900,900
window = pygame.display.set_mode((WIDTH, HEIGTH))
  
# alkalmazás nevének megadása
pygame.display.set_caption('Frogger')
  
# óra beállítása

clock = pygame.time.Clock()

# spritok megadása
# háttér megadása
Player = pygame.image.load('Player.png')
        
car = pygame.image.load('Car1.png')
car2 = pygame.image.load('Car2.png')
car3 = pygame.image.load('Car3.png')
background = pygame.image.load('BackGround.png')
leaf = pygame.image.load('Leaf.png')
flower = pygame.image.load('Flower.png')

# visszaszámláló 
counter, text = 20, '20'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

# score számláló beállítása a PLayer y koordinátái alapján
y =  (HEIGTH * 0.95)
current_time = y
score = (f"Score: {current_time}")

#objektumok adatai
x = (WIDTH * 0.45) 
# pálya határai nehogy a Player kimenjen a felületről
x_pos_max = WIDTH * 0.94
x_neg_max = WIDTH * -0.01
y_pos_max = HEIGTH * 0.95 
y_neg_max = HEIGTH * 0.02

width_of_Player = 66
heigth_of_Player = 50


width_of_car = 100
heigth_of_car = 80

width_of_car2 = 100
heigth_of_car2 = 80

width_of_car3 = 100
heigth_of_car3 = 80

width_of_car4 = 100
heigth_of_car4 = 80


x_pos_car = -150
y_pos_car = 280
car_speed = randrange(12, 20)
car2_speed = randrange(15, 20)
car3_speed = randrange(10, 15)
car4_speed = randrange(12, 15)

x_pos_car2 = -150
y_pos_car2 = 370

x_pos_car3 = 800
y_pos_car3 = 460

x_pos_car4 = 600
y_pos_car4 = 550
speed = 5

x_pos_leaf = 200
y_pos_leaf = 400

x_pos_flower = 405
y_pos_flower = 18

  
# végtelen ciklus
run = True
while run:
  
    # óra beállítása 60 FPS-re
    clock.tick(60)
   
    # objektumok elhelyezése 
  
    window.blit(background, (0.5, 8))
    window.blit(car, (x_pos_car, y_pos_car))
    window.blit(car2,(x_pos_car2, y_pos_car2))
    window.blit(car3,(x_pos_car3, y_pos_car3))
    window.blit(car3,(x_pos_car4, y_pos_car4))
    window.blit(leaf, (405,163))
    window.blit(leaf, (405,63))
    window.blit(flower, (x_pos_flower, y_pos_flower))
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    screen.blit(font.render(score, True, (0, 0, 0)), (100, 200))
    window.blit(Player, (x, y))
  
    # események ellenőrzése 

    for event in pygame.event.get():

        current_time = pygame.time.get_ticks()
        #score jelző 0-ra állítása
        Score = (y - 855) * -1
        current_time = y
        #score betűtípis beállítása és kiírása
        font2 = pygame.font.SysFont('Consolas', 30)
        score = (f"Score: {Score}")

        print(x_pos_car3)
        

        # a run bool ha True értéket veszi fel a program kilép
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit
            #visszaszámlálás -1/másodperccel 
            #ha lejár game over kilép a program
        if event.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'Game Over!'
            if counter < 0:
                run = False
                print(score)
            
        # autók indítása
        
        x_pos_car += car_speed
        x_pos_car2 += car2_speed
        x_pos_car3 -= car3_speed
        x_pos_car4 -= car4_speed
        # autók újraindítása miután elérték a pálya széleit

        if x_pos_car >= WIDTH:
            x_pos_car = -100
            y_pos_car = randrange(280, 370)
        if x_pos_car2 >= WIDTH:
            pygame.time.wait(2)
            x_pos_car2 = -100
            y_pos_car2 = randrange(370, 460)
        if x_pos_car3 <= x_neg_max:
            x_pos_car3 = 900
            y_pos_car3 = randrange(460, 550)
        if x_pos_car4 <= x_neg_max:
            x_pos_car4 = 900
            y_pos_car4 = randrange(550, 570)
        
           
       

    key_pressed_is =  pygame.key.get_pressed()

    # Player mozgása
    # ESC billentyűre való kilépés

    if key_pressed_is[K_LEFT]:
        x -= speed
    if key_pressed_is[K_RIGHT]:
        x += speed
    if key_pressed_is[K_UP]:
        y -= speed
    if key_pressed_is[K_DOWN]:
        y += speed
    if key_pressed_is[K_ESCAPE]:
        run = False
        print(score)
    # PLayer pályán tartása
    if x >= WIDTH * 0.94:
        x = x_pos_max
    if x <= WIDTH * -0.01:
        x = x_neg_max
    if y <= HEIGTH * 0.02:
        y = y_neg_max
    if y >= HEIGTH * 0.95:
        y = y_pos_max
    #maximum y érték elérésekor a program leáll
    if y_pos_flower == y:
        run = False
    #score kiírása 
        print(score)

        #képernyő frissítés
  
    pygame.display.update()

