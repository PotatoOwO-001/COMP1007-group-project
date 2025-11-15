import pygame
import sys
import math

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moveable Stick Man - A (Left) D (Right)")

# Colors
BLACK = (0, 0, 0)

#character appearence
class StickMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.direction = 1  #1=right, -1=left

        #Body parameter
        size.head_radiu = 30
        size.body_length = 50
        size.hands_length = 40
        size.legs_length = 60

        #movement animation
        self.walking = false
        self.walking_patteren = 0
        self.walking_speed = 0.5
        
        #keyboard_movement_control
        def right_handside_movement(self):
            self.x +=self.speed
            self.facing_direction= 1
            self.walking = true
        
        def left_handside_movement(self):
            self.x -=self.speed
            self.facing_direction = -1
            self.walking = true
            
        def stop(self):
            self.walking= false
            
        #movement posture refreshment   
        def update(self):
            self.walking_patteren += self.walking_speed

        
            
        
            

# Boundary limitation
size.x = width-size.head_radiu
            
