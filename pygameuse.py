import pygame
import math
import random
from pygame import mixer
pygame.init()
pygame.font.init()
mixer.music.load("background.wav")
mixer.music.play(-1)
score_value=0
text=pygame.font.Font("freesansbold.ttf",32)
text_x=10;text_y=10
def show_score(x,y):
    score=text.render("Score : " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("SPACE INVADERS")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
back=pygame.image.load("back.jpg")
playerimg=pygame.image.load("space-invaders.png")
playx=370
playy=480
playchange=0
def player():
    screen.blit(playerimg,(playx,playy))

alien=[]
alienx=[]
alieny=[]
alienx_change=[]
alieny_change=[]
num_of_aliens=6
for i in range(num_of_aliens):
    alien.append(pygame.image.load("alien.png"))
    alienx.append(random.randint(0,734))
    alieny.append(random.randint(50,150))
    alienx_change.append(0.65)
    alieny_change.append(30)
def enemy(alien,x,y):
    screen.blit(alien,(x,y))
bullet=pygame.image.load("bullet.png")
bulletx=0
bullety=480
bulletx_change=0
bullety_change=2
bullet_state="ready"
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fired"
    screen.blit(bullet,(x+16,y+15))
def isCollide(alienx,alieny,bulletx,bullety):
    distance=math.sqrt((alienx-bulletx)**2+(alieny-bullety)**2)
    if distance<27:
        return True
    return False
gamo_over_font=pygame.font.Font("Blanchope Free.ttf",64)
def game_over_text():
    over_score=gamo_over_font.render("GAMEOVER",True,(0,0,0))
    screen.blit(over_score,(230,250))
r=True
while r:
    screen.fill((50,50,50))
    screen.blit(back,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            r=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playchange=-1.5
            elif event.key==pygame.K_RIGHT:
                playchange=1.5
            elif event.key==pygame.K_SPACE and bullet_state =="ready":
                bulletx=playx
                laser=mixer.Sound("laser.wav")
                laser.play()
                fire_bullet(bulletx,bullety)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playchange=0
    playx=playx+playchange
    if playx<0:
        playx=0
    if playx>736:
        playx=736
    for i in range(num_of_aliens):
        if alieny[i]>300:
            for j in range(num_of_aliens):
                alieny[j]=2000
            game_over_text()
            break
        alienx[i]+=alienx_change[i]
        if alienx[i]<0:
            alienx_change[i]=0.65
            alieny[i]+=alieny_change[i]
        elif alienx[i]>736:
            alienx_change[i]=-0.65       
            alieny[i]+=alieny_change[i]
        collide=isCollide(alienx[i],alieny[i],bulletx,bullety)
        if collide:
            bullety=480
            bullet_state="ready"
            score_value+=1
            alienx[i]=random.randint(0,734)
            alieny[i]=random.randint(50,150)
            explo_sound=mixer.Sound("explosion.wav")
            explo_sound.play()
        enemy(alien[i],alienx[i],alieny[i])
    if bullety<=0:
        bullety=480
        bullet_state="ready"
    if bullet_state=='fired':
        fire_bullet(bulletx,bullety)
        bullety-=bullety_change
    player()
    show_score(text_x,text_y)
    pygame.display.update() 