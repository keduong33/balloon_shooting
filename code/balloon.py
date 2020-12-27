import pygame
import random
from settings import width, height
'''
    Class for the balloon object
    Balloon size: 40 x 40
'''
class Balloon:
    def __init__(self):
        self.position = [0,200]
        self.pic = pygame.image.load("../images/balloon.png")
    def move(self):
        randomMove = random.random()
        direction = 1
##        delay = 0
##        repeatCount = 0
##        repeat = random.randint(10,100)
##        randomMove = random.random()
##        while repeatCount < repeat:
##            #delay
##            while delay < 1000000:
##                delay += 1
##            if  randomMove < 0.3 and self.position[1] + 6.67 < height - 40:
##                self.position[1] += 6.67
##                print("Balloon: " + str(self.position))
##            elif randomMove > 0.7 and self.position[1] - 6.67 > 0:
##                self.position[1] -= 6.67
##                print("Balloon: " + str(self.position))
##            repeatCount += 1
        if  randomMove < 0.35 or randomMove > 0.85:
            direction *= -1
        if direction > 0 and self.position[1] + 15*direction < height - 40:
            self.position[1] += 15* direction
            print("Balloon: " + str(self.position))
        elif direction < 0 and self.position[1] + 15*direction > 0:
            self.position[1] += 15 * direction
            print("Balloon: " + str(self.position))
            
