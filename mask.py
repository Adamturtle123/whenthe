import pygame


class Mask:
    def __init__(self, x, y, image):
        self.alpha = 255
        self.x = x
        self.y = y
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        
    
    def photofy_mask(self):
        image = self.mask.to_surface(unsetcolor=(0,0,0,0), setcolor=(255,255,255,255))
        return image
    
    def render_mask(self,display, scroll, img):
        display.blit(img, (self.x - scroll[0] ,self.y - scroll[1]))
    
    
    
    
        