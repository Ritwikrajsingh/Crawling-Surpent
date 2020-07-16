#IMPORTING

import pygame
import random

#BASIC SETUP

pygame.init()

length_of_canvas = 1080
height_of_canvas = 720

clock = pygame.time.Clock()

res = pygame.display.set_mode((length_of_canvas,height_of_canvas))
pygame.display.set_caption("Surpent's Crawl")
pygame.display.set_icon(pygame.image.load('icon.png'))
'''Icon made by https://www.flaticon.com/authors/google'''
unit = 10
FPS = 35

#FUNCTIONS

#SNAKE
def snake(unit,snake_list):
	for x in snake_list:
		pygame.draw.rect(res,(0,0,255),(x[0]*unit,x[1]*unit,unit,unit))
length = length_of_canvas//unit
height = height_of_canvas//unit

#FOOD
def food(foodx,foody):
	pygame.draw.rect(res,(255,0,0),(foodx*unit,foody*unit,unit,unit))

#SCORE
def Score(score):
		font = pygame.font.SysFont('arial', 20)
		text = font.render('Score : ' + str(score),1,(0,255,0))
		res.blit(text,(unit//2,unit//2)) 

#MAIN_GAME		
def the_game():

	#default_values

	score = 0
	snake_list = []
	length_of_snake = 1

	x1 = random.choice(range(length))
	y1 = random.choice(range(height))	

	foodx = random.choice(range(length))
	foody = random.choice(range(height))

	x1_ch = 1
	y1_ch = 0
	
	run = True

	while run:
		
		#userControls

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		keys = pygame.key.get_pressed()
		if (keys[pygame.K_UP] or keys[pygame.K_w]) and y1_ch==0:
			y1_ch -= 1
			x1_ch = 0
		elif ( keys[pygame.K_DOWN] or keys[pygame.K_s]) and y1_ch==0:
			y1_ch += 1
			x1_ch = 0
		elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x1_ch==0:
			x1_ch += 1
			y1_ch = 0
		elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x1_ch==0:
			x1_ch-= 1
			y1_ch = 0
		if keys[pygame.K_LSHIFT]:
			length_of_snake+=1
			score+=1


		#properties of snake

		x1 += x1_ch
		y1 += y1_ch
		snake_head = [x1,y1]
		snake_list.append(snake_head)
			#removal of traces
		if len(snake_list)>length_of_snake:
			del snake_list[0]

		#drawingObjects
		res.fill((0,0,0))
		food(foodx,foody)
		snake(unit,snake_list)

		#eationg Food

		if x1==foodx and y1==foody:
			foodx=random.choice(range(length))
			foody=random.choice(range(height))
			length_of_snake+=1
			score+=1

		#death of Snake

		if x1>=length or x1<0 or y1>=height or y1<0:
			return True
		
		for i in snake_list[:-1]:
			if i == snake_head:
				return True 

		#drawing score

		Score(score)
		pygame.display.update()

		#framerates

		clock.tick(FPS)

#RUNNING GAME

the_game()

#RESTART ON DEATH

while the_game():
	pass
