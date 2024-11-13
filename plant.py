import pygame
from items import Item
class Plant(Item):
    def __init__(self,x,y,width,height,path, item_name, growth_rate):
        super().__init__(x, y, width, height, path, item_name)
        self.phase = 0
        self.growth_rate = growth_rate
        self.is_planted = False
        
    
    def get_planted(self):
        pass