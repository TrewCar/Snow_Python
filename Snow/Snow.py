import pygame
import random


w = 1920
h = 1080

FPS = 60
d = 255,255,255
Background = 0,0,0
pygame.init()

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Space")
clock = pygame.time.Clock()

Pl = 1

class Snow(pygame.sprite.Sprite):
    def __init__(self):
        pos = random.randrange(0,w)
        pos1 = random.randrange(0,h)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((Pl, Pl))
        self.image.fill(d)
        self.rect = self.image.get_rect()
        self.rect.center = (pos,pos1)        
    def sss(self):
        if self.rect.y > h+Pl:
            self.rect.y = 0-Pl
        elif self.rect.y < 0-Pl:
            self.rect.y = h+Pl
        if self.rect.x > w+Pl:
            self.rect.x = 0-Pl
        elif self.rect.x < 0-Pl:
            self.rect.x = w+Pl
    def move(self,pixels):
        s = random.randrange(0,1)
        if s ==0:
            self.rect.x -= pixels  -5  
        else:
            self.rect.x += pixels -5  
        self.rect.y += pixels * pixels/10 

clock = pygame.time.Clock()


def fffg(i):
    array[i].move(random.randrange(1,10))
    array[i].sss()
    if i < SizeArry-1:
        fffg(i+1)

all_sprites = pygame.sprite.Group()
SizeArry = 800
array = []

i=0    
while i<SizeArry:   
    snow = Snow() 
    array.append(snow)
    i+=1
all_sprites.add(array)



running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update
    screen.fill(Background)
    all_sprites.draw(screen)
    fffg(0)
    pygame.display.flip()
pygame.quit()
