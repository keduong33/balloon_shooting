import pygame
import gun
import keyboard
import balloon
from pygame import K_UP, K_DOWN, K_SPACE
from settings import width, height, screen
'''
    This is the main file for the game
    Run this file to play the game
    Gun size: 60 x 40 (w x h)
'''
class Bullet:
    def __init__(self):
        self.startPosition = [-100,-100]
        self.position = self.startPosition
        self.fired = False
        
#initialisation
pygame.init()

gun = gun.Gun()
bullet = Bullet()
balloon = balloon.Balloon()
playerKeyboard = keyboard.Keyboard()
white = [255,255,255]
clock = pygame.time.Clock()
bulletPic = pygame.image.load("../images/bullet.png")

while True:
    clock.tick(30)
    screen.fill(white)
    screen.blit(gun.pic, gun.position)
    screen.blit(bulletPic, bullet.position)
    screen.blit(balloon.pic, balloon.position)
    pygame.display.flip()
    
    playerKeyboard.manage(gun,bullet)
    balloon.move()

