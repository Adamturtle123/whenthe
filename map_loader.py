import pygame
import os
import json
pygame.init()
#Oh alright I will download that workspace then
#I gotta go eat
class Map():
    def __init__(self, tile_database, tile_list):
        self.tile_database = tile_database
        self.tile_list = tile_list
        self.collidables = []
        self.tile_rect = []
        self.rects = {}
        self.get_tiles()
        self.rects_data = self.get_col()
        
    
    def get_tiles(self):
        for tile in self.tile_list:
            
            img = pygame.image.load('assets/tiles/' + tile).convert()
            img.set_colorkey((255,255,255))
            self.tile_database[tile] = img.copy()
        
        return self.tile_database
        
        

    def get_col(self,):
        with open('data.json', 'r') as f:
            data = json.load(f)
            meta_data = data["collidables"] #{'tree.png:[]}
            
            for tile in self.tile_database:
                
                
                for col in meta_data:
                    if tile == col:
                        self.collidables.append(tile)
            
            for name in self.collidables:
                self.rects[name] = pygame.Rect(meta_data[name][0], meta_data[name][1], meta_data[name][2], meta_data[name][3])
        
        return self.rects
        
        
        
    
    
                    
    
    
    
    def load_map(self, path):
        with open(f'{path}.json', 'r') as f:
            data = json.load(f)
            tile_map = data['map']
    
        return tile_map


    def tiles(self,world_data, display, scroll, shops, entity):
        self.tile_rect = []
    #layers    
        for i, layer in sorted(enumerate(world_data), reverse=True):
        #tiles
            for j, tile in sorted(enumerate(world_data[layer]), reverse=True):
                
                loc = tile.split(':')
                tile_data = world_data[layer][tile]
            
                if tile_data[4] == "shop.png":
                    shops.append(entity(int(loc[0]), int(loc[1]), 23, 31, "assets/tiles/shop.png"))
                
                display.blit(self.tile_database[tile_data[4]], (int(loc[0])-int(scroll[0]), int(loc[1])-int(scroll[1])))
                
                if tile_data[4] in self.collidables:
                    self.tile_rect.append(pygame.Rect(int(loc[0]) + self.rects[tile_data[4]].x, 
                                                      int(loc[1]) + self.rects[tile_data[4]].y ,
                                                      self.rects_data[tile_data[4]].width, self.rects_data[tile_data[4]].height))
                
#rects_data = [posx, posy, w, h]           
                       
                    
#uhh still working on that I will be doing it now

#I am gonna make save settings now
