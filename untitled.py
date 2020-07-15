import pygame
import random
FPS = 30
pygame.init()
LENGTH = 1080
HEIGHT = 720
clock = pygame.time.Clock()
res = pygame.display.set_mode((LENGTH,HEIGHT))
pygame.display.set_caption("Surpent's Crawl")
base = 10

def snake(base,snake_list):
	for x in snake_list:
		pygame.draw.rect(res,(0,0,255),(x[0]*base,x[1]*base,base,base))
length = LENGTH//base
height = HEIGHT//base


def food(foodx,foody):
	pygame.draw.rect(res,(255,0,0),(foodx*base,foody*base,base,base))
def Score(score):
		font = pygame.font.SysFont('arial', 20)
		text = font.render('Score : ' + str(score),1,(0,255,0))
		res.blit(text,(base//2,base//2))
		pygame.display.update()
def the_game():
	snake_list = []
	length_of_snake = 1
	run = True
	restart = False
	x1 = random.choice(range(length))
	y1 = random.choice(range(height))	
	foodx = random.choice(range(length))
	foody = random.choice(range(height))
	x1_ch = 1
	y1_ch = 0
	length_of_snake = 1
	score = 0
	while run:
		
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
		elif (keys[pygame.K_RIGHT] or keys[pygame.K_s]) and x1_ch==0:
			x1_ch += 1
			y1_ch = 0
		elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x1_ch==0:
			x1_ch-= 1
			y1_ch = 0
		if keys[pygame.K_LSHIFT]:
			length_of_snake+=1
			score+=1
		x1 += x1_ch
		y1 += y1_ch
		snake_head = [x1,y1]
		snake_list.append(snake_head)
		if len(snake_list)>length_of_snake:
			del snake_list[0]
		if snake_list[0]==snake_list[::-1]:
			return True
			quit()
		if x1==foodx and y1==foody:
			foodx=random.choice(range(length))
			foody=random.choice(range(height))
			length_of_snake+=1
			score+=1
		res.fill((0,0,0))
		food(foodx,foody)
		snake(base,snake_list)		
		if x1>=length or x1<0 or y1>=height or y1<0:
			return True
		Score(score)
		pygame.display.update()
		clock.tick(FPS)
		for i in snake_list[:-1]:
			if i == snake_head:
				return True 
the_game()
while the_game():
	pass
