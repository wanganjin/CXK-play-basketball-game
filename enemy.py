import pygame
from random import *

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/small_basketball.png").convert_alpha()

        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/small_basketball_down_1.png").convert_alpha(),\
            pygame.image.load("images/small_basketball_down_2.png").convert_alpha(),\
            pygame.image.load("images/small_basketball_down_3.png").convert_alpha()])

        self.rect = self.image.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.speed = 2
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left,self.rect.top =randint(0,self.width - self.rect.width),randint(-5*self.height,0)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset

    def reset(self):
        self.active = True
        self.rect.left,self.rect.top =randint(0,self.width - self.rect.width),randint(-5*self.height,0)

class MidEnemy(pygame.sprite.Sprite):

    energy = 8

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/mid_basketball.png").convert_alpha()

        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/mid_basketball_down_1.png").convert_alpha(),\
            pygame.image.load("images/mid_basketball_down_2.png").convert_alpha(),\
            pygame.image.load("images/mid_basketball_down_3.png").convert_alpha()])

        self.rect = self.image.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.speed = 1
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left,self.rect.top =randint(0,self.width - self.rect.width),randint(-10*self.height,-self.height)
        self.energy = MidEnemy.energy

    def move(self):
        if self.rect.top < self.height+5:
            self.rect.top += self.speed
        else:
            self.reset

    def reset(self):
        self.active = True
        self.energy = MidEnemy.energy
        self.rect.left,self.rect.top =randint(0,self.width - self.rect.width),randint(-10*self.height,-self.height)

class BigEnemy(pygame.sprite.Sprite):

    energy = 20

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/big_basketball_1.png").convert_alpha()
        self.image2 = pygame.image.load("images/big_basketball_2.png").convert_alpha()
        self.image3 = pygame.image.load("images/big_basketball_3.png").convert_alpha()
        self.image4 = pygame.image.load("images/big_basketball_4.png").convert_alpha()
        self.image5 = pygame.image.load("images/big_basketball_5.png").convert_alpha()
        self.image6 = pygame.image.load("images/big_basketball_6.png").convert_alpha()
        self.image7 = pygame.image.load("images/big_basketball_7.png").convert_alpha()
        self.image8 = pygame.image.load("images/big_basketball_8.png").convert_alpha()
        self.image9 = pygame.image.load("images/big_basketball_9.png").convert_alpha()
        self.image10 = pygame.image.load("images/big_basketball_10.png").convert_alpha()
        self.image11 = pygame.image.load("images/big_basketball_11.png").convert_alpha()
        self.image12 = pygame.image.load("images/big_basketball_12.png").convert_alpha()
        self.image13 = pygame.image.load("images/big_basketball_13.png").convert_alpha()
        self.image14 = pygame.image.load("images/big_basketball_14.png").convert_alpha()
        self.image15 = pygame.image.load("images/big_basketball_15.png").convert_alpha()
        self.image16 = pygame.image.load("images/big_basketball_16.png").convert_alpha()
        self.image17 = pygame.image.load("images/big_basketball_17.png").convert_alpha()
        self.image18 = pygame.image.load("images/big_basketball_18.png").convert_alpha()
        self.image19 = pygame.image.load("images/big_basketball_19.png").convert_alpha()

        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/big_basketball_down_1.png").convert_alpha(),\
            pygame.image.load("images/big_basketball_down_2.png").convert_alpha(),\
            pygame.image.load("images/big_basketball_down_3.png").convert_alpha()])

        self.rect = self.image1.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.speed = 1
        self.active = True
        self.mask = pygame.mask.from_surface(self.image1)
        self.rect.left,self.rect.top =randint(0,self.width - self.rect.width),randint(-15*self.height,-5*self.height)
        self.energy = BigEnemy.energy

    def move(self):
        if self.rect.top < self.height+5:
            self.rect.top += self.speed
        else:
            self.reset

    def reset(self):
        self.active = True
        self.energy = BigEnemy.energy
        self.rect.left,self.rect.top =randint(0,self.width - self.rect.width),randint(-15*self.height,-5*self.height)

