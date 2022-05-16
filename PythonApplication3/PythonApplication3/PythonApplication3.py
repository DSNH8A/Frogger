# mosulok import�l�sa
import pygame
import random
from pygame import time
from pygame.locals import *
from random import randrange
from operator import itemgetter
  
# pygame ind�t�sa
pygame.init()

# lej�tsz�fel�let adatainak megad�sa �s be�ll�t�sa 

screen = pygame.display.set_mode((128, 128))
WIDTH, HEIGTH = 900,900
window = pygame.display.set_mode((WIDTH, HEIGTH))
  
# alkalmaz�s nev�nek megad�sa
pygame.display.set_caption('Frogger')
  
# �ra be�ll�t�sa

clock = pygame.time.Clock()

# spritok megad�sa
# h�tt�r megad�sa
Player = pygame.image.load('Player.png')
        
car = pygame.image.load('Car1.png')
car2 = pygame.image.load('Car2.png')
car3 = pygame.image.load('Car3.png')
background = pygame.image.load('BackGround.png')
leaf = pygame.image.load('Leaf.png')
flower = pygame.image.load('Flower.png')

# visszasz�ml�l� 
counter, text = 20, '20'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

# score sz�ml�l� be�ll�t�sa a PLayer y koordin�t�i alapj�n
y =  (HEIGTH * 0.95)
current_time = y
score = (f"Score: {current_time}")

#objektumok adatai
x = (WIDTH * 0.45) 
# p�lya hat�rai nehogy a Player kimenjen a fel�letr�l
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

  
# v�gtelen ciklus
run = True
while run:
  
    # �ra be�ll�t�sa 60 FPS-re
    clock.tick(60)
   
    # objektumok elhelyez�se 
  
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
  
    # esem�nyek ellen�rz�se 

    for event in pygame.event.get():

        current_time = pygame.time.get_ticks()
        #score jelz� 0-ra �ll�t�sa
        Score = (y - 855) * -1
        current_time = y
        #score bet�t�pis be�ll�t�sa �s ki�r�sa
        font2 = pygame.font.SysFont('Consolas', 30)
        score = (f"Score: {Score}")

        print(x_pos_car3)
        

        # a run bool ha True �rt�ket veszi fel a program kil�p
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit
            #visszasz�ml�l�s -1/m�sodperccel 
            #ha lej�r game over kil�p a program
        if event.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'Game Over!'
            if counter < 0:
                run = False
                print(score)
            
        # aut�k ind�t�sa
        
        x_pos_car += car_speed
        x_pos_car2 += car2_speed
        x_pos_car3 -= car3_speed
        x_pos_car4 -= car4_speed
        # aut�k �jraind�t�sa miut�n el�rt�k a p�lya sz�leit

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

    # Player mozg�sa
    # ESC billenty�re val� kil�p�s

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
    # PLayer p�ly�n tart�sa
    if x >= WIDTH * 0.94:
        x = x_pos_max
    if x <= WIDTH * -0.01:
        x = x_neg_max
    if y <= HEIGTH * 0.02:
        y = y_neg_max
    if y >= HEIGTH * 0.95:
        y = y_pos_max
    #maximum y �rt�k el�r�sekor a program le�ll
    if y_pos_flower == y:
        run = False
    #score ki�r�sa 
        print(score)

        #k�perny� friss�t�s
  
    pygame.display.update()

