#Imports
import random, sys
import pygame as pg
from pygame import font
pg.init()

#Variables
score=0
red=(255,0,0)
green=(0,255,0)
blue=(0,228,255)
yellow=(255,128,0)
white=(255,255,255)
screen=pg.display.set_mode((600,600))
fails=0
clock=pg.time.Clock()
running=True

bowl_img=pg.image.load('Ball_Game_Files/bowl.png')
apple_img=pg.image.load('Ball_Game_Files/apple.png')
backdrop_img=pg.image.load('Ball_Game_Files/backdrop.png')
orange_img=pg.image.load('Ball_Game_Files/orange.png')
tomato_img=pg.image.load('Ball_Game_Files/tomato.png')
lemon_img=pg.image.load('Ball_Game_Files/lemon.png')
avocado_img=pg.image.load('Ball_Game_Files/avocado.png')
pepper_img=pg.image.load('Ball_Game_Files/pepper.png')
squash_img=pg.image.load('Ball_Game_Files/squash.png')
mushroom_img=pg.image.load('Ball_Game_Files/mushroom.png')
watermelon_img=pg.image.load('Ball_Game_Files/watermelon.png')
bullet_img=pg.image.load('Ball_Game_Files/bullet.png')
watermelon_img=pg.image.load('Ball_Game_Files/watermelon.png')

fail_sound=pg.mixer.Sound('Ball_Game_Files/miss_sound.wav')
win_sound=pg.mixer.Sound('Ball_Game_Files/catch_sound.wav')

font=pg.font.Font(None,90)


#Classes
class Player(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.width=200
		self.height=100
		self.image=pg.transform.scale(bowl_img,(int(self.width),int(self.height)))
		self.rect=self.image.get_rect()
		self.speed=5
	def update(self):
		self.image=pg.transform.scale(bowl_img,(int(self.width),int(self.height)))

class food(pg.sprite.Sprite):
	def __init__(self,image):
		pg.sprite.Sprite.__init__(self)
		self.width=50
		self.height=50
		self.pic=image
		self.image=pg.transform.scale(self.pic,(int(self.width),int(self.height)
		))
		self.rect=self.image.get_rect()
		self.speed=0
	def update(self):
		self.image=pg.transform.scale(self.pic,(int(self.width),int(self.height)))

class Ground(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image=pg.Surface((600,100))
		self.rect=self.image.get_rect()
		self.rect.bottomleft=(0,600)

#Objects and Groups
bowl=Player()
apple=food(apple_img)
orange=food(orange_img)
tomato=food(tomato_img)
lemon=food(lemon_img)
avocado=food(avocado_img)
pepper=food(pepper_img)
squash=food(squash_img)
mushroom=food(mushroom_img)
melon=food(watermelon_img)
bullet=food(bullet_img)
ground=Ground()

all_sprites=pg.sprite.Group()
all_sprites.add(melon)
all_sprites.add(mushroom)
all_sprites.add(squash)
all_sprites.add(pepper)
all_sprites.add(avocado)
all_sprites.add(lemon)
all_sprites.add(tomato)
all_sprites.add(orange)
all_sprites.add(apple)
all_sprites.add(bullet)
all_sprites.add(bowl)
all_sprites.add(bullet)

bowl.rect.bottom=525
bowl.rect.centerx=300
apple.rect.bottomleft=(random.randint(0,550),int(-15*apple.speed))
orange.rect.right=0
tomato.rect.right=0
lemon.rect.right=0
avocado.rect.right=0
pepper.rect.right=0
squash.rect.left=600
squash.width=100
squash.height=100
mushroom.rect.right=0
melon.width+=50
melon.height+=50
melon.rect.left=600
bullet.rect.topright=(0,0)

apple.speed=5

print('''Rules:
Rules:
	1. Use the arrow keys to move the bowl left and right to catch/avoid objects.
	2. The apple falls faster over time.
	3. After the score reaches 530, the apple's speed reaches its max and will not increase anymore.
	4. After the score reaches 1000, the apple starts to get smaller.
Food Glossary:
	Apple - if caught, score increases by five. If it falls to the ground, "missed apples" increases by 1.
	Orange - Increases the player's speed by 0.5.
	Tomato - increases bowl size by 6.
	Lemon - if caught, nothing happens. However, if it falls to the ground, "missed apples" increases by 2.
	Avocado - if "missed apples" is greater than zero, 0.5 apples are replenished. If there are no missed apples, the score goes up by five.
	Pepper - If caught, "missed apples" increases by two.
	Squash - If caught, the player's speed decreases by four.
	Mushroom - If caught, the bowl's size decreased by twenty.
	Glowing Orb Thing - If you catch it, nothing happens. If you miss it, nothing happens. Just think of it as a distraction.
	Watermelon - If caught, the size of the apple increases, and the the sizes of the peppers and squash decrease.''')

#Main Loop(s)
while True:
	while running==True:
		clock.tick(24)
		if int(fails)>=10:
			running=False
			name=input()
			print(str(name)+' got a score of '+str(score))
		#Events
		for event in pg.event.get():
			if event.type==pg.QUIT:
				sys.exit()
			if event.type==pg.KEYDOWN:
				if event.key==pg.K_SPACE:
					running=None
		keys=pg.key.get_pressed()
		if keys[pg.K_RIGHT]:
			bowl.rect.centerx+=bowl.speed
		if keys[pg.K_LEFT]:
			bowl.rect.centerx-=bowl.speed
		#Apple - collect to gain points
		if apple.rect.colliderect(bowl.rect):
			pg.mixer.Sound.play(win_sound)
			apple.rect.bottomleft=(random.randint(0,575),int(-20*apple.speed))
			score+=5
			if apple.speed<=16:
				apple.speed+=0.1
			if score>1000:
				apple.width-=0.1
				apple.height-=0.1
		if apple.rect.colliderect(ground.rect):
			pg.mixer.Sound.play(fail_sound)
			apple.rect.bottomleft=(random.randint(0,575),int(-20*apple.speed))
			fails+=1
			if apple.speed<=16:
				apple.speed+=0.5
			if score>1000:
				apple.width-=0.25
				apple.height-=0.25
		apple.rect.bottom+=int(apple.speed)

		#Orange - makes you faster
		if score>100:
			orange.speed=5
			orange.rect.bottom+=orange.speed
		if orange.rect.colliderect(bowl.rect):
			pg.mixer.Sound.play(win_sound)
			orange.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-3600,0)))
			bowl.speed+=0.5
		if orange.rect.colliderect(ground.rect):
			orange.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-3600,0)))
		if score==100:
			orange.rect.topleft=(int(random.randint(0,550)),int(random.randint(-3600,0)))

		#Tomato - replenishes missing apples
		if score>250:
			tomato.speed=5
			tomato.rect.bottom+=tomato.speed
		if tomato.rect.colliderect(bowl.rect):
			pg.mixer.Sound.play(win_sound)
			tomato.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-3600,0)))
			bowl.width+=6
			bowl.rect.left-=3
		if tomato.rect.colliderect(ground.rect):
			tomato.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-3600,0)))
		if score==250:
			tomato.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-3600,0)))

		#Lemon makes the apple slower
		if score>325:
			lemon.speed=5
			lemon.rect.bottom+=lemon.speed
		if lemon.rect.colliderect(bowl.rect):
			pg.mixer.Sound.play(win_sound)
			lemon.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,-1500)))
		if lemon.rect.colliderect(ground.rect):
			pg.mixer.Sound.play(fail_sound)
			lemon.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,-1500)))
			fails+=2
		if score==325:
			lemon.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,-1500)))
		
		#Avocado - replenishes missing apples (more than tomatoes)
		if score>475:
			avocado.speed=5
			avocado.rect.bottom+=avocado.speed
		if avocado.rect.colliderect(bowl.rect):
			pg.mixer.Sound.play(win_sound)
			avocado.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,-1800)))
			if fails>0:
				fails-=0.5
			if fails==0:
				score+=5
		if avocado.rect.colliderect(ground.rect):
			avocado.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,-1800)))
		if score==475:
			avocado.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,-1800)))
		
		#Pepper - depletes missing apples
		if score>600:
			pepper.speed=5
			pepper.rect.bottom+=pepper.speed
		if pepper.rect.colliderect(bowl.rect):
			pg.mixer.Sound.play(fail_sound)
			pepper.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,-1200)))
			pepper.width+=10
			pepper.height+=10
			fails+=2
		if pepper.rect.colliderect(ground.rect):
			pepper.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,-1200)))
			pepper.width+=10
			pepper.height+=10
		if score==600:
			pepper.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,-1200)))
		
		#Squash - makes you slower
		if score>800:
			squash.speed=5
			squash.rect.bottom+=squash.speed
		if squash.rect.colliderect(bowl.rect):
			pg.mixer.Sound.play(fail_sound)
			squash.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,0)))
			bowl.speed-=4
			squash.width+=10
			squash.height+=10
		if squash.rect.colliderect(ground.rect):
			squash.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,0)))
			squash.width+=10
			squash.height+=10
		if score==800:
			squash.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,0)))
		
		#Mushroom - restores four missed apples
		if score>900:
			mushroom.speed=5
			mushroom.rect.bottom+=mushroom.speed
		if mushroom.rect.colliderect(bowl.rect):
			pg.mixer.Sound.play(fail_sound)
			mushroom.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,-1200)))
			bowl.width-=20
			bowl.rect.right+=10
		if mushroom.rect.colliderect(ground.rect):
			mushroom.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,-1200)))
		if score==900:
			mushroom.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,-1200)))
		
		#Bullet - strengthens your laser
		if score>1000:
			bullet.speed=5
			bullet.rect.bottom+=bullet.speed
		if bullet.rect.colliderect(bowl.rect):
			bullet.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-1500,0)))
		if bullet.rect.colliderect(ground.rect):
			bullet.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-1500,0)))
		if score==1000:
			bullet.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-1500,0)))
		
		#Melon - makes the apple bigger, the pepper and squash smaller
		if score>1000:
			melon.speed=5
			melon.rect.bottom+=melon.speed
		if melon.rect.colliderect(bowl.rect):
			pg.mixer.Sound.play(win_sound)
			melon.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,-1200)))
			apple.width+=5
			apple.height+=5
			pepper.width-=5
			pepper.height-=5
			squash.width-=5
			squash.height-=5
		if melon.rect.colliderect(ground.rect):
			melon.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,-1200)))
		if score==1000:
			melon.rect.bottomleft=(int(random.randint(0,550)),int(random.randint(-6000,-1200)))
		#Drawing and Updates
		screen.blit(pg.transform.scale(backdrop_img,(600,600)),(0,0))
		all_sprites.draw(screen)
		all_sprites.update()
		screen.blit(font.render("Caught: "+(str(score)),True,red),(0,0))
		screen.blit(font.render("Missed: "+(str(int(fails))),True,red),(0,60))
		pg.display.update()
	while running==None:
		font2=pg.font.Font(None,150)
		text=font2.render("Paused",True,red)
		textRect=text.get_rect()
		textRect.center=(300,300)
		screen.fill(blue)
		screen.blit(text,textRect)
		for event in pg.event.get():
			if event.type==pg.QUIT:
				sys.exit()
			if event.type==pg.KEYDOWN:
				if event.key==pg.K_SPACE:
					running=True
		pg.display.update()
	while running==False:
		font2=pg.font.Font(None,150)
		text=font2.render("Game Over!",True,red)
		textRect=text.get_rect()
		textRect.center=(300,300)
		screen.fill(blue)
		screen.blit(text,textRect)
		for event in pg.event.get():
			if event.type==pg.QUIT:
				sys.exit()
			if event.type==pg.KEYDOWN:
				if event.key==pg.K_SPACE:
					apple.speed=5
					bowl.speed=5
					orange.rect.right=0
					tomato.rect.right=0
					lemon.rect.right=0
					avocado.rect.right=0
					pepper.rect.right=0
					squash.rect.right=0
					mushroom.rect.right=0
					score=0
					fails=0
					bullet.rect.right=0
					bowl.width=200
					tomato.width=50
					tomato.height=50
					squash.width=50
					squash.height=50
					running=True
		pg.display.update()