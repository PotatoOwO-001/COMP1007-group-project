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
WHITE = (255, 255, 255)

#character appearence
class StickMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.direction = 1  #1=right, -1=left

        #Body parameter
        size.head_radius = 30
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
        self.x = max(size.head_radius), min(WIDTH - size.body_l)

        def draw(self, surface):
            # Head 
            pygame.draw.circle(surface, BLACK, (self.x, self.y - self.body_length - self.head_radius), self.head_radius)
            
            # Body 
            body_top = (self.x, self.y - self.body_length)
            body_bottom = (self.x, self.y)
            pygame.draw.line(surface, BLACK, body_top, body_bottom, 3)
        
            # Movement calculation of hand's animation
            if self.walking:
                # Hands opposite to legs during walking
                left_hand_angle = math.pi/9 + math.sin(self.walk_phase) * 0.5
                right_hand_angle = math.pi/9 - math.sin(self.walk_phase) * 0.5
            else:
                left_arm_angle = math.pi/9
                right_arm_angle = math.pi/9
        
        # Arm direction adjustment
        if self.direction == 1:  
            # Facing right
            left_arm_end = (self.x - math.cos(left_arm_angle) * self.arm_length, self.y - self.body_length + math.sin(left_arm_angle) * self.arm_length )
            right_arm_end = (self.x + math.cos(right_arm_angle) * self.arm_length, self.y - self.body_length + math.sin(right_arm_angle) * self.arm_length)
        else:  
            # Facing left
            left_arm_end = (self.x - math.cos(left_arm_angle) * self.arm_length, self.y - self.body_length + math.sin(left_arm_angle) * self.arm_length)
            right_arm_end = (self.x + math.cos(right_arm_angle) * self.arm_length, self.y - self.body_length + math.sin(right_arm_angle) * self.arm_length)
        
        # Hands displaying
        pygame.draw.line(surface, BLACK, body_top, left_hand_end, 2)
        pygame.draw.line(surface, BLACK, body_top, right_hand_end, 2)
        
        # Movement calculation of leg's animation
        if self.walking:
            left_leg_angle = math.pi/6 + math.sin(self.walk_phase) * 0.3
            right_leg_angle = math.pi/6 - math.sin(self.walk_phase) * 0.3
        else:
            left_leg_angle = math.pi/6
            right_leg_angle = math.pi/6
        
        # Adjust legs based on direction
        if self.direction == 1:  
            # Facing right
            left_leg_end = (self.x - math.cos(left_leg_angle) * self.leg_length, self.y + math.sin(left_leg_angle) * self.leg_length)
            right_leg_end = (self.x + math.cos(right_leg_angle) * self.leg_length, self.y + math.sin(right_leg_angle) * self.leg_length)
        else:  
            # Facing left
            left_leg_end = (self.x - math.cos(left_leg_angle) * self.leg_length, self.y + math.sin(left_leg_angle) * self.leg_length)
            right_leg_end = (self.x + math.cos(right_leg_angle) * self.leg_length, self.y + math.sin(right_leg_angle) * self.leg_length)
        
        # Legs displaying
        pygame.draw.line(surface, BLACK, body_bottom, left_leg_end, 3)
        pygame.draw.line(surface, BLACK, body_bottom, right_leg_end, 3)

# Stick man showcase
stick_man = StickMan(WIDTH // 2, HEIGHT // 2 + 100)

# Game looping
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Key pressing
    keys = pygame.key.get_pressed()
    
    # Movement controls
    if keys[pygame.K_a]:
        stick_man.move_left()
    elif: keys[pygame.K_d]:
        stick_man.move_right()
    else:
        stick_man.stop()
    
    # Stick man refreshment
    stick_man.update()
    
    # Background clearing
    screen.fill(WHITE)
    
    # Base ground line
    pygame.draw.rect(screen, (200, 200, 200), (0, HEIGHT - 50, WIDTH, 50))
    
    # Draw stick man
    stick_man.draw(screen)
    
    # Display refreshment
    pygame.display.flip()
    
    # Frame rate caption
    clock.tick(60)

pygame.quit()
sys.exit()
