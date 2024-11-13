import pygame

class AI():
    def __init__(self, entity): #target=entity that has ai
        self.entity = entity
        self.directions = [0,0]
    
    def follow_target(self, target):#target here is the player or the thing the entity ai will follow
        
        if target.hitbox.x > self.entity.hitbox.x: #The entity ai is on the left of the player
            self.directions[0] = 2
            #print('move right')
        
        elif target.hitbox.x < self.entity.hitbox.x: #The entity ai is on the right of the player
            self.directions[0] = -2
            #print('move left')
            
        
        self.entity.movement[0] = self.directions[0]
        
        if self.entity.collusion_type["right"] or self.entity.collusion_type["left"]:
            self.entity.y_momentum = -6
            #print("touched wall")
        
        
        
        
        #self.movement[0] = self.directions[0]
        #self.movement[1] = self.directions[1]
        
        #print(self.movement)
        