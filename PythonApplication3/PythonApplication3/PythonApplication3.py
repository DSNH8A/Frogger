# Importing pygame module
import pygame
import random
from pygame import time
from pygame.locals import *
from random import randrange
from operator import itemgetter
  
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

  
# create the display surface object
# of specific dimension.
#window = pygame.display.set_mode((1920, 1080))
screen = pygame.display.set_mode((128, 128))
WIDTH, HEIGTH = 900,900
window = pygame.display.set_mode((WIDTH, HEIGTH))
  
# Add caption in the window
pygame.display.set_caption('Frogger')
  
# Initializing the clock
# Clocks are used to track and
# control the frame-rate of a game
clock = pygame.time.Clock()
class Player:
	def __init__(self, image, x, y, width_of_player, heigth_of_player, speed):
		self.image = image
		self.x = x
		self.y = y
		self.width_of_player = width_of_player
		self.width_of_player = heigth_of_player
		self.speed = speed

class Car:
	def __init__(self, image, x_pos_car, y_pos_car, width_of_car, heigth_of_car, car_speed):
		self.image = image
		self.x_pos_car = x_pos_car
		self.y_pos_car = y_pos_car
		self.width_of_car = width_of_car
		self.heigth_of_car = heigth_of_car
		self.car_speed = car_speed
	def car_movement(self):
		 x_pos_car += car_speed

class Car1(Car):
	def __init__(self, image, x_pos_car, y_pos_car, width_of_car, heigth_of_car, car_speed):
		super(). __init__(image, x_pos_car, y_pos_car, width_of_car, heigth_of_car, car_speed)
class Car2(Car):
	def __init__(self, image, x_pos_car, y_pos_car, width_of_car, heigth_of_car, car_speed):
		super(). __init__(image, x_pos_car, y_pos_car, width_of_car, heigth_of_car, car_speed)
class Car3(Car):
	def __init__(self, image, x_pos_car, y_pos_car, width_of_car, heigth_of_car, car_speed):
		super(). __init__(image, x_pos_car, y_pos_car, width_of_car, heigth_of_car, car_speed)
class Car4(Car):
	def __init__(self, image, x_pos_car, y_pos_car, width_of_car, heigth_of_car, car_speed):
		super(). __init__(image, x_pos_car, y_pos_car, width_of_car, heigth_of_car, car_speed)

# objektumok példányosytása
car1 = Car1(pygame.image.load('Car1.png'), -150, 280, 100, 80, randrange(12, 20))
car2 = Car2(pygame.image.load('Car2.png'), -150, 370, 100, 80, randrange(15, 20))
car3 = Car3(pygame.image.load('Car3.png'), -150, 460, 100, 80, randrange(10, 15))
car4 = Car4(pygame.image.load('Car2.png'), -150, 550, 100, 80, randrange(12, 15))
  
# Add player sprite
Player = [pygame.image.load('Player.png'),
         pygame.image.load('Player2.png'),
         pygame.image.load('Player3.png')]
car = pygame.image.load('Car1.png')
car2 = pygame.image.load('Car2.png')
car3 = pygame.image.load('Car3.png')
background = pygame.image.load('BackGround.png')
leaf = pygame.image.load('Leaf.png')
flower = pygame.image.load('Flower.png')


counter, text = 20, '20'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)
y =  (HEIGTH * 0.95)
current_time = y


high_score, text = 20, '20'.rjust(3)
font = pygame.font.SysFont('Consolas', 30)

score = (f"Score: {current_time}")
 #Store the initial
# coordinates of the player in
# two variables i.e. x and y.
x = (WIDTH * 0.45) 

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

x_pos_car3 = -150
y_pos_car3 = 460

x_pos_car4 = -150
y_pos_car4 = 550
speed = 5

x_pos_leaf = 200
y_pos_leaf = 400

x_pos_flower = 405
y_pos_flower = 18


  
# Creating an Infinite loop
run = True
while run:
  
    # Set the frame rates to 60 fps
    clock.tick(60)
   
  
    # Display the player sprite at x
    # and y coordinates
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
    screen.blit(font.render(str(high_score), True, (0, 0, 0)), (100, 300))


    
    window.blit(Player[0], (x, y))

    
    #window.blit(image, (x, y))
    #print(x, y)
  
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        current_time = pygame.time.get_ticks()
        #print(y)
        Score = (y - 855) * -1
        current_time = y
        font2 = pygame.font.SysFont('Consolas', 30)
        score = (f"Score: {Score}")

        score_board = []
        score_board.append(Score)
        print(score_board[0])
        
        # Closing the window and program if the
        # type of the event is QUIT
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit
        if event.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'Game Over!'
            if counter < 0:
                run = False
                print(score)
            
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = True
            elif event.key == pygame.K_LEFT:
                direction = False
        car_movement()
        x_pos_car2 += car2_speed
        x_pos_car3 += car3_speed
        x_pos_car4 += car4_speed
        if x_pos_car >= WIDTH:
            x_pos_car = -100
            y_pos_car = randrange(280, 370)
        if x_pos_car2 >= WIDTH:
            pygame.time.wait(2)
            x_pos_car2 = -100
            y_pos_car2 = randrange(370, 460)
        if x_pos_car3 >= WIDTH:
            x_pos_car3 = -100
            y_pos_car3 = randrange(460, 550)
        if x_pos_car4 >= WIDTH:
            x_pos_car4 = -100
            y_pos_car4 = randrange(550, 570)
        
           
       

    key_pressed_is =  pygame.key.get_pressed()

    # Changing the coordinates
    # of the player
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
    if x >= WIDTH * 0.94:
        x = x_pos_max
    if x <= WIDTH * -0.01:
        x = x_neg_max
    if y <= HEIGTH * 0.02:
        y = y_neg_max
    if y >= HEIGTH * 0.95:
        y = y_pos_max
    if y_pos_flower == y:
        run = False
        score += str(1000)
        score_board.append(score)
        print(score)


  
    pygame.display.update()

