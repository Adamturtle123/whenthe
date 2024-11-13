import pygame
import os
class Animations:
    def __init__(self):
        self.action = ""
        self.frame = 0
        self.current_frame = 0
        self.animation_frames = []#(3)
        self.frames_database = {}#(2)
        self.animation_database = {} #(1)
        
        #{"walk": walk_0, walk_1...}(1)
        #{"walk_0": walk.png, "walk_1": walk2.png}(2)
        #[walk_0, walk_0, walk_1](3) #we will repeat the animation name multiple time to represent how long we want to play it
        
    def load_animation(self, path, duration=[1,1]):
        animation_name = path.split("/")[-1] #walk, run...
        
        n = 0
        for frame in duration:
            
            animation_frame_id = animation_name + "_" + str(n) #walk_0, walk_1
            #self.animation_database[animation_name] = animation_frame_id
            img_loc = path + "/" + animation_frame_id + ".png"
            img = pygame.image.load(img_loc)
            img.set_colorkey((255,255,255))
            self.frames_database[animation_frame_id] = img.copy()
            n += 1
            for i in range(frame):
                self.animation_frames.append(animation_frame_id)
        
        return self.animation_frames    
    
    
    def auto_load(self, path):
        name = os.listdir(path)
        for key in name:
            
            self.animation_database[key] = anime.load_animation(path + "/" + key, [1,1])
        
        return self.animation_database       
        
anime = Animations()

#print(anime.auto_load("assets/player"))

#anime.animation_database["walk"] = anime.load_animation( "assets/player/walk", [1,1,1,1])


#print(anime.animation_database)

#anime.frame += 1
#pygame.display.blit(anime.frames_database[anime.animation_database["walk"][anime.frame]])



    
    