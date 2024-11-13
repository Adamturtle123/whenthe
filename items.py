from entity import Entity
from projectile import Projectile
import math
import pygame
import json
from timers import Timer
class Item(Entity):
    def __init__(self, x,y,width,height,path, item_name):
        super().__init__(x, y, width, height, path)
        self.item_name = item_name
        self.stats = self.load_stats("stats")
        self.icon = pygame.image.load(f"{path}")
        self.icon = pygame.transform.scale(self.icon, (self.icon.get_width()/2, self.icon.get_height()/2))
        self.icon.set_colorkey("White")
        self.angle = 0
        self.fire_rate = 0
        self.magazine = 7500
        
        
        #{'items': {'melee': {'pickaxe': {'dmg': 2, 'speed': 2, 'durability': 2}}, 'consumables': {'Mango': {'heal': 2}}}}
    #----check for each item if the item is melee class then blah blah
    #----for now make basic following ability + swing (don't forget we will make class for each main item inshallah that contains all the properties)
    #Swing (done sorta we gonna fix it)
    def item_func(self,item, mx, my, projs, scroll):
        btn_pressed = pygame.mouse.get_pressed()
        for item_class in self.stats["items"]:
            #print(self.stats["items"]["melee"])
            if item.item_name in self.stats["items"]["range"]:
                if btn_pressed[0] and self.magazine > 0:#Adding bullets to projectiles list when we hold mouse button
                    s  = Timer().wait(3)
                    if s == False:
                        
                        projs[self.item_name].append(Projectile(item.hitbox.x + 10, item.hitbox.y + 10 ,2,5, "rifle", self.angle*-1 , "assets/items/bullet.png"))
                        self.magazine -= 1
                        self.fire_rate += 1
                        Timer().reset()
                    
                    
                    
                    
                self.angle = item.get_direction(mx,my, scroll)
                
                return int(self.angle)*-1
            
                
            #if item.item_name in self.stats["items"]["consumables"]:
                #print("Pina")
                
    def load_stats(self,path):
        with open(f'{path}.json', 'r') as f:
            data = json.load(f)
            
        return data
    
    def get_distance_to_player(self, player):
        return math.sqrt(abs((player.hitbox.x - self.hitbox.x)) ^ 2 + abs((player.hitbox.y+20 - self.hitbox.y)) ^ 2)
        
    def pickup(self, player):
        
        key_pressed = pygame.key.get_pressed()
        
        
        distance = self.get_distance_to_player(player)
        if distance > 3:
            
            self.reach = False
        #print(int(distance))
        else:
            if int(distance) <= 3 and key_pressed[pygame.K_e]:
                
                self.reach = True
            #print("picked up")
        
        return self.reach

                    

    def hold_item(self, selected_item, target, display, scroll): #it was selected_item.rotated_image changed to image
        img_copy = pygame.transform.rotate(selected_item.image, (selected_item.angle))
        selected_item.hitbox.x = target.hitbox.x
        selected_item.hitbox.y = target.hitbox.y
        display.blit(img_copy, ((selected_item.hitbox.x + 10 - scroll[0]) - int(img_copy.get_width()/2) , (selected_item.hitbox.y + 10 - scroll[1]) - int(img_copy.get_height()/2)))
    
    #def hold_item(self, selected_item, target, display, scroll):
    # Rotate the gun by applying the correct angle
       # img_copy = pygame.transform.rotate(selected_item.image, -selected_item.angle)

    # Update gun position to match the player's position (use fine-tuned offsets)
        #gun_offset_x = 10  # Adjust this if necessary
        #gun_offset_y = 10  # Adjust this if necessary
        #selected_item.hitbox.x = target.hitbox.x
        #selected_item.hitbox.y = target.hitbox.y

    # Get the rect for the rotated image, centered at the gun's intended location
        #img_rect = img_copy.get_rect(center=(selected_item.hitbox.x + gun_offset_x - scroll[0], 
                                         #selected_item.hitbox.y + gun_offset_y - scroll[1]))

    # Debugging information to see what's happening
        #print(f"Gun Center: {selected_item.hitbox.x + gun_offset_x}, {selected_item.hitbox.y + gun_offset_y}")
        #print(f"Rotated Image Rect: {img_rect.topleft}")
        #print(f"Gun Angle (Degrees): {selected_item.angle}")

    # Blit the rotated image at the new position based on the adjusted rect
        #
        # display.blit(img_copy, img_rect.topleft)  
        
    
    





        
        
        
        
    
    