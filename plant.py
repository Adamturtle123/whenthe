import pygame
from items import Item
class Plant(Item):
    def __init__(self,x,y,width,height,path, item_name):
        super().__init__(x, y, width, height, path, item_name)
        
        
        self.phases = {}