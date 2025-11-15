import pygame
import sys
import math

pygame.init()
#character appearence
class StickMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.direction = -1  #-1=right, 1=left

        #Body parameter
        size.head_radiu = 30
        size.body_length = 50
        size.hands_length = 40
        size.legs_length = 60

        #movement animation
        self.walking = false
        self.walking_01 = 0
        self.walking_speed = 0.5
