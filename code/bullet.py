import pygame
class Bullet:
    def __init__(self):
        self.pic = pygame.image.load("../images/bullet.png")
        self.createNewBullet()
        self.missedShot = 0
    def getFired(self,gun):
        self.fired = True
        self.position = [gun.position[0]-20,gun.position[1]+10]
        print("Bullet: " + str(self.position))
        print("Bullet Fired")
    def fly(self):
        self.position[0] -= 10
        print("Bullet: " + str(self.position))
    def reload(self):
        self.createNewBullet()
        print("Bullet: " + str(self.position))
        print("Bullet out of window")
        self.missedShot += 1
    def reset(self):
        self.missedShot = 0
        self.createNewBullet()
        print("Bullet: " + str(self.position))
    def createNewBullet(self):
        self.startPosition = [-100,-100]
        self.position = self.startPosition
        self.fired = False
