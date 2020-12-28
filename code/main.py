import pygame
import tkinter
from tkinter import messagebox
import pygetwindow as gw
#handmade libraries
import gun, eventHandler, balloon, bullet
from settings import screen
'''
    This is the main file for the game
    Run this file to play the game
'''
def main():
    direction = 1
    while True:
        clock.tick(30)
        screen.fill(white)
        screen.blit(gun.pic, gun.position)
        screen.blit(bullet.pic, bullet.position)
        screen.blit(balloon.pic, balloon.position)
        pygame.display.flip()
        event.manage(gun,bullet)
        direction = balloon.move(direction)
        if balloon.getHitBy(bullet):
            print(bullet.missedShot)
            missedShot = bullet.missedShot
            replay = receiveInput(missedShot)
            if replay == 'yes':
                win = gw.getWindowsWithTitle('Balloon Shooting')[0]
                win.activate()
                restart()
            else:
                pygame.quit() 
                exit(0)

def restart():
    bullet.reset()
    balloon.reset()
    gun.reset()
    print("Restarted the game")
    main()

def receiveInput(missedShot):
    parent = tkinter.Tk()
    parent.overrideredirect(1)
    parent.withdraw()
    notification = 'You missed {ms} shots.\nWanna play again?'.format(ms = missedShot)
    replay = messagebox.askquestion("The balloon is hit", notification) # Yes / No
    print(replay)
    return replay

#initialisation
pygame.init()
gun = gun.Gun()
bullet = bullet.Bullet()
balloon = balloon.Balloon()
event = eventHandler.event()
white = [255,255,255]
clock = pygame.time.Clock()
title = 'Balloon Shooting'
pygame.display.set_caption(title)
icon = pygame.image.load("../images/smileyFace.jpg")
pygame.display.set_icon(icon)
main()
