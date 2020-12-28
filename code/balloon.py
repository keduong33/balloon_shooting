import pygame
import random
from settings import width, height
'''
    Class for the balloon object
    Balloon size: 40 x 40
'''
class Balloon:
    def __init__(self):
        self.createNewBalloon()
    def move(self, direction):
        randomMove = random.randint(0,100)
        
        if randomMove >= 30:
            if randomMove <= 40:
                direction = direction * -1
            if direction > 0 and self.position[1] + 6.67*direction < height - 40:
                self.position[1] += 6.67* direction
                print("Balloon: " + str(self.position))
            elif direction < 0 and self.position[1] + 6.67*direction > 0:
                self.position[1] += 6.67 * direction
                print("Balloon: " + str(self.position))
        return direction
    def getHitBy(self,bullet):
        if (int(self.position[0]) - bullet.position[0] == 0) and (self.bottomHit(bullet) or self.topHit(bullet)):
            print(self.position, bullet.position)
            return True
        return False
    def bottomHit(self,bullet):
        return abs(int(self.position[1]) - bullet.position[1]) <= 30 and self.position[1] <= bullet.position[1]
    def topHit(self, bullet):
        return abs(int(self.position[1]) - bullet.position[1]) <= 15 and self.position[1] > bullet.position[1]
    def reset(self):
        self.createNewBalloon()
    def createNewBalloon(self):
        self.startPosition = [0,200]
        self.position = self.startPosition
        self.pic = pygame.image.load("../images/balloon.png")   
            
            
