import pygame
import sys
from pygame.locals import *
from random import *
class Ball(pygame.sprite.Sprite):
    def __init__(self,image,position,speed,bg_size):
        # pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.speed = speed
        self.width,self.height = bg_size[0],bg_size[1]
        self.radius = self.rect.width / 2
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.right < 0:
            self.rect.left = self.width
        elif self.rect.left > self.width:
            self.rect.right = 0
        elif self.rect.bottom <0:
            self.rect.top = self.height
        elif self.rect.top > self.height:
            self.rect.bottom = 0
def main():
    pygame.init()
    ball_image = "gray_ball.png"
    bg_image = "background.png"

    running = True
    bg_size = width,height = 1024,681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Play the ball")
    background = pygame.image.load(bg_image).convert_alpha()
    balls = []
    group = pygame.sprite.Group()

    for i in range(5):
        position = randint(0,width-100),randint(0,height-100)
        speed = [randint(-10,10),randint(-10,10)]
        ball = Ball(ball_image,position,speed,bg_size)
        # while pygame.sprite.spritecollide(ball,group,False):
        while pygame.sprite.spritecollide(ball,group,False,pygame.sprite.collide_circle):
            ball.rect.left,ball.rect.top = randint(0,width-100),randint(0,height-100)
        balls.append(ball)
        group.add(ball)

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.blit(background,(0,0))

        for each in balls:
            each.move()
            screen.blit(each.image,each.rect)

        for each in group:
            group.remove(each)
            if pygame.sprite.spritecollide(each,group,False,pygame.sprite.collide_circle):
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1]
            group.add(each)
        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()