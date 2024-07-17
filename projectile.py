import math
import pygame
from entity import Entity
class Projectile(Entity):
    
    def __init__(self,x,y,width,height, proj_name, angle ,path):
        super().__init__(x, y, width, height, path)
        self.proj_name = proj_name
        self.proj_angle = 0
        self.speed = 5
        self.angle = angle
        #self.x_dir = math.cos(self.proj_angle)*self.speed
        #self.y_dir = math.sin(self.proj_angle)*self.speed
    
    
    def render_projectile(self, display, scroll):#Renders the projectile based on it's trajectory
        image_copy = pygame.transform.rotate(self.image, self.angle*-1)
        display.blit(image_copy, (self.hitbox.x - scroll[0], self.hitbox.y - scroll[1]))
    
    def move_proj(self, proj_angle):
        x_dir = math.cos(proj_angle)*self.speed
        y_dir = math.sin(proj_angle)*self.speed
        self.movement[0] += x_dir
        self.movement[1] += y_dir 
        