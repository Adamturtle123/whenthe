import pygame

class Inventory():
    def __init__(self):
        self.slot_index = 0
        self.slot_selector = 1
        self.inventory_slots = [[],[],[],[],[]]
        
        self.inventory = {
        }
        
    def handle_inventory(self, world, player, items, display, scroll):
        
        for item in items:
            #text = font.render(str(int(item.get_distance_to_player(player))), True, (0,0,0), (255,255,255))
            
            col_type, item.hitbox = item.move(world.tile_rect) 
            item.update(scroll, display)
            item.gravity(col_type)
        
            reach = item.pickup(player)
            #display.blit(text, (item.hitbox.x-scroll[0]+10, item.hitbox.y-scroll[1]))
            if reach and len(self.inventory_slots[self.slot_index]) < 1:
                self.slot_index += 1
                if item.item_name not in self.inventory:
                    self.inventory[item.item_name] = []
                    #print("creating new subject")
                    
                self.inventory[item.item_name].append(item)
                items.remove(item)
                self.inventory_slots[self.slot_index-1].append(item)
                
                if self.slot_index >= len(self.inventory_slots):
                    self.slot_index = 0
    
    def make_slots(self, display,x,y):
        index = 0
        pygame.draw.rect(display, (255,0,0), (x+self.slot_selector*16, y, 16,16))
        if self.slot_selector > len(self.inventory_slots):
            self.slot_selector = 1
        elif self.slot_selector == 0:
            self.slot_selector = len(self.inventory_slots)
        for row in self.inventory_slots:
            
            index += 1
            pygame.draw.rect(display, (0,255,0), (x+index*16, y, 16,16), 1)
            for item in row:
                display.blit(item.icon, (x+index*16, y))
    
    def select_item(self):
        selected_item = self.inventory_slots[self.slot_selector-1]
        if selected_item:
            return selected_item[0]
         