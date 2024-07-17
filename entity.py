import pygame
import math
class Entity:
    def __init__(self, x, y, width, height, path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.image.load(f"{path}").convert()
        self.image.set_colorkey("White")
        self.movement = [0,0]#the movement of player vector speed
        self.y_momentum = 0#speed verticle
        self.air_timer = 0#sees how much time spent in air (for jumping purposes)
        self.jump_force = -6
        self.slot_index = 0
        self.slot_select = 0
        self.speed = 5
        self.jumps = 0
        self.collusion_type = {"top":False, "bottom":False, "right":False, "left":False}
        
        
    def collusion_test(self, tiles):#these are the tiles list that has all the tile rect data
        self.hit_list = []
        for tile in tiles:
            if self.hitbox.colliderect(tile):
                self.hit_list.append(tile)
        return self.hit_list
    
    def update(self, scroll, screen):#renders the entity
        screen.blit(self.image, (self.hitbox.x-scroll[0], self.hitbox.y-scroll[1]))
        #pygame.draw.rect(screen, (255,0,0), (self.hitbox.x-scroll[0], self.hitbox.y-scroll[1], self.hitbox.width, self.hitbox.height), 2)
    
    
    def move(self, tiles): #Collusion and moving the player
        self.collusion_type = {"top":False, "bottom":False, "right":False, "left":False} #this is the collusion reletive to the entity
        self.hitbox.x += self.movement[0]
        hit_list = self.collusion_test(tiles)
        for tile in hit_list:
            if self.movement[0] > 0:
                self.hitbox.right = tile.left
                self.collusion_type["right"] = True

            elif self.movement[0] < 0:
                self.hitbox.left = tile.right
                self.collusion_type["left"] = True
        
        
        self.hitbox.y += self.movement[1]
        hit_list = self.collusion_test(tiles)
        for tile in hit_list:
            if self.movement[1] > 0:
                
                self.hitbox.bottom = tile.top
                self.collusion_type["bottom"] = True

            elif self.movement[1] < 0:
                self.hitbox.top = tile.bottom
                self.collusion_type["top"] = True
        
        return self.collusion_type, self.hitbox
    
    def gravity(self, col_type):#makes the entity fall basically
        self.y_momentum += 0.4
        if self.y_momentum > 5:
            self.y_momentum = 5
        
            
        self.movement[1] = self.y_momentum
        if col_type["bottom"]:
            #self.y_momentum = 0
            self.air_timer = 0
            self.jumps = 0
            
            
            
        else:
            self.air_timer += 1
            #*(180/math.pi)*-1-90
    def get_direction(self,tx,ty, scroll):#Get the angle where the entity is headed to through x,y of mouse
        rel_X = tx-(int(self.hitbox.x - scroll[0] + 10  -int(self.image.get_width()/2)))
        rel_Y = ty-(int(self.hitbox.y - scroll[1] + 10 -int(self.image.get_height()/2)))
        
        #print([self.hitbox.x, self.hitbox.y])
        #-int(self.image.get_width()/2))
        self.angle = (math.atan2(rel_Y, rel_X+0.0001))

        return math.degrees(self.angle) 



        
        
