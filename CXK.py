import pygame

class CXK(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/CXK_1.png").convert_alpha()
        self.image2 = pygame.image.load("images/CXK_2.png").convert_alpha()
        self.image3 = pygame.image.load("images/CXK_3.png").convert_alpha()
        self.image4 = pygame.image.load("images/CXK_4.png").convert_alpha()
        self.image5 = pygame.image.load("images/CXK_5.png").convert_alpha()
        self.image6 = pygame.image.load("images/CXK_6.png").convert_alpha()
        self.image7 = pygame.image.load("images/CXK_7.png").convert_alpha()
        self.image8 = pygame.image.load("images/CXK_8.png").convert_alpha()
        self.image9 = pygame.image.load("images/CXK_9.png").convert_alpha()
        self.image10 = pygame.image.load("images/CXK_10.png").convert_alpha()
        self.image11 = pygame.image.load("images/CXK_11.png").convert_alpha()
        self.image12 = pygame.image.load("images/CXK_12.png").convert_alpha()
        self.image13 = pygame.image.load("images/CXK_13.png").convert_alpha()
        self.image14 = pygame.image.load("images/CXK_14.png").convert_alpha()
        self.image15 = pygame.image.load("images/CXK_15.png").convert_alpha()
        self.image16 = pygame.image.load("images/CXK_16.png").convert_alpha()
        self.image17 = pygame.image.load("images/CXK_17.png").convert_alpha()
        self.image18 = pygame.image.load("images/CXK_18.png").convert_alpha()

        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/CXK_down_1.png").convert_alpha(),\
            pygame.image.load("images/CXK_down_2.png").convert_alpha(),\
            pygame.image.load("images/CXK_down_3.png").convert_alpha(),\
            pygame.image.load("images/CXK_down_4.png").convert_alpha()])

        self.rect = self.image1.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.rect.left,self.rect.top = (self.width - self.rect.width) /2,self.height - self.rect.height - 60
        self.speed = 10
        self.active = True
        self.invincible = False
        self.mask = pygame.mask.from_surface(self.image1)

    def moveUP(self):
        if self.rect.top>0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDOWN(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLEFT(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRIGHT(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        self.rect.left,self.rect.top = (self.width - self.rect.width) /2,self.height - self.rect.height - 60
        self.active = True
        self.invincible = True





