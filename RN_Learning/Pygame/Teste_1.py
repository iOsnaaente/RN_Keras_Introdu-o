from random import randint
import numpy as np 
import pygame
import math 

def sum(A,B):
    MATRIX = A.copy()
    for i in range(len(A)):
       MATRIX[i] = A[i] + B[i]
    return MATRIX


WHITE = [255,255,255]
GRAY  = [150,150,150]
BLACK = [  0,  0,  0]


display_length, display_width = 800, 500 

naturalForce = 1 #gravity simulated 
fAmort = 0.75

class Pontos:

    img = pygame.transform.scale(pygame.image.load('./fog.jpg'), [35,35])
    size = [20,20]
    pos = [0,0]
    vel = [0,0]
    vela = [0,0]
    acl = [0,0]
    
    def __init__(self, length, width, pos = [0,0]):
        self.pos = [display_length/2, display_width/2]
        self.vel = [0,0]
        self.acl = [0,0]

    def drawPoint(self):
        pygame.draw.rect(main_screen, GRAY, [self.pos[0], self.pos[1], self.size[0], self.size[1]], 0)
        #main_screen.blit(self.img, self.pos)

    def addVel(self, vel = [0,0]):
        self.vela = self.vel
        self.vel = sum(self.vel, vel)

    def addAcl(self, acl = [0,0]):
        self.acl = sum(self.acl, acl)

    def applyForces(self, draw = False):
        if self.pos[0] + self.vel[0] > display_length or self.pos[0] + self.vel[0] < 0:
            self.vel[0] = int(self.vel[0] * -fAmort)

        if self.pos[1] + self.vel[1] > display_width or self.pos[1] + self.vel[1] < 0:
            self.vel[1] = int(self.vel[1] * -fAmort)

        self.pos = sum(self.pos, self.vel)

        self.vela = self.vel  
        self.vel = sum(self.vel, self.acl) 

        self.acl = [0, naturalForce]

        if draw:
            self.drawPoint()


class Goal:
    #time2arrive
    pos = [0,0]
    raio = 35
    num = 0

    def __init__(self):
        self.pos = [randint(0,display_length), randint(0,display_width)]
        self.raio = 15
        self.draw()

    def newGoal(self):
        self.num = self.num + 1
        self.pos = [randint(0,display_length), randint(0,display_width)]
        self.draw()

    def draw(self):
        pygame.draw.circle(main_screen, BLACK, self.pos, self.raio, 0)



pygame.init()

pygame.display.set_caption("Modelo básico de funcionamento para Pygame")

main_screen = pygame.display.set_mode([display_length, display_width])
Clock = pygame.time.Clock()


teste = Pontos(0,0)
goal = Goal()

teste.addAcl([10,50])


while 1:

    main_screen.fill(WHITE)

    x_acl = y_acl = 0

    for event in pygame.event.get():
    	if event.type == pygame.KEYDOWN:
    		if event.key == pygame.K_ESCAPE:
    			pygame.quit()

    		if event.key == pygame.K_LEFT:
    			x_acl = -2
    		elif event.key == pygame.K_RIGHT:
    			x_acl = 2

    		if event.key == pygame.K_UP:
    			y_acl = -2
    		elif event.key == pygame.K_DOWN:
    			y_acl = 2

    teste.addAcl([x_acl,y_acl])

    print(x_acl, y_acl, end='\n')
    print(teste.acl, end='\n')
    print(teste.vel, end='\n')
    

    teste.applyForces(True)
    goal.draw()

    pygame.display.update()
    Clock.tick(20)