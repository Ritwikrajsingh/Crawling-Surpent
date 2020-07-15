import pygame
import time
import random
clock = pygame.time.Clock()
pygame.init()
LENGTH = 720
HEIGHT = 480
res= pygame.display.set_mode((LENGTH,HEIGHT))
clock = pygame.time.Clock()
pygamee.display.set_caption("Surpent's Crawl")
base = 10
radius = base//2
def snake(base,snake_list):
	for x in snake_list:
		pygame.draw.rect(res,(0,255,0),(x[0],x[1],base,base))
length = LENGTH//base
height = HEIGHT//base
snake_list = []
length_of_snake = 1
def food(foodx,foody):
	pygame.draw.circle(res,(255,0,0),(foodx,foody),radius)
def the_game():
	length_of_snake = 1
	run = True
	restart = False
	x1 = random.choice(range(length*10))
	y1 = random.choice(range(height*10))	
	foodx = random.choice(range(length*10))
	foody = random.choice(range(height*10))
	x1_ch = 1
	y1_ch = 0
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP] and y1_ch==0:
			y1_ch -= 1
			x1_ch = 0
		elif keys[pygame.K_DOWN] and y1_ch==0:
			y1_ch += 1
			x1_ch = 0
		elif keys[pygame.K_RIGHT] and x1_ch==0:
			x1_ch += 1
			y1_ch = 0
		elif keys[pygame.K_LEFT] and x1_ch==0:
			x1_ch-= 1
			y1_ch = 0
		x1 += x1_ch
		y1 += y1_ch
		snake_head = []
		snake_head.append(x1)
		snake_head.append(y1)
		snake_list.append(snake_head)
		if len(snake_list)>length_of_snake:
			del snake_list[0]
		if snake_list[0]==snake_list[::-1]:
			return True
			quit()
		if x1==foodx and y1==foody:
			foodx=random.choice(range(length*10))
			foody=random.choice(range(height*10))
			length_of_snake+=base
		res.fill((0,0,0))
		food(foodx,foody)
		snake(base,snake_list)		
		if x1>=LENGTH or x1<0 or y1>=HEIGHT or y1<0:
			snake(base,snake_list)
		pygame.display.update()
		pygame.time.delay(2)
the_game()
if the_game() == True:
	the_game()