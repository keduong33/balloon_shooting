import pygame
from settings import width, height
'''
Gun size: 60 x 40 (w x h)
'''
class Gun:
    def __init__(self):
        self.createNewGun()
    def moveUp(self, position):
        if self.position[1] - 10 > 0:
            self.position[1] -= 10
        print("Gun: " + str(self.position))
    def moveDown(self, position):
        if self.position[1] + 10 < height - 40:
            self.position[1] +=10
        print("Gun: " + str(self.position))
    def createNewGun(self):
        self.startPosition = [540,200]
        self.position = self.startPosition
        self.pic = pygame.image.load("../images/gun.png")
    def reset(self):
        self.createNewGun()
        
