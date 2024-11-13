import pygame
import os
import json
pygame.init()

WIDTH, HEIGHT = 800, 600
version = '1.0.1'

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tile editor v " + version)


tiles_set = os.listdir('assets/tiles')
tile_database = {}
for tile in tiles_set:
    img = pygame.image.load('assets/tiles/' + tile).convert()
    img.set_colorkey((255,255,255))
    tile_database[tile] = img.copy()

selected_tile = "dirt.png"

font = pygame.font.Font('assets/retrofont.ttf', 25)

tiles_size = 20

scroll = [0,0]

snap = True

offsets = {"grass.png" : {"tile_offset" : [0, -3]},
            "grass l.png" : {"tile_offset" : [-4, -3]},
            "grass r.png" : {"tile_offset" : [-4, -3]},
            "dirt.png" : {"tile_offset" : [0,0]},
            "edge l.png" : {"tile_offset" : [-2, 0]},
            "edge r.png" : {"tile_offset" : [-2, 0]},
            "shop.png": {"tile_offset": [-3, -11]}}
# dict = {"grass.png: {tile_offest: [x, y]}"}
# dict[selected_tile] --> {tile_offest: [x,y]}
# offset = dict[selected_tile]["tile_offest"] ---> [x,y]
#x + offset[0], y + offset[1]

class Tiles:
    def __init__(self, x, y, width, height, img):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img
        self.tile_rect = pygame.Rect(x, y, width, height)
    
    def update_rect(self, scroll):
        self.tile_rect = pygame.Rect(self.x-scroll[0], self.y-scroll[1], self.width, self.height)
        return self.tile_rect
        
#{"layer1":{'loc':25,'loc':50}, "layer2"[], "layer3":[]}
    
layers = {}
def gen_layers(layer_index):
    
    
    for i in range(layer_index):
        
        layers['layer_'+str(layer_index)] = {}
    
    return layers
    
#layers = [[Tiles(50, 50, tiles_size, tiles_size, dirt),Tiles(50, 50, tiles_size, tiles_size, dirt)], [Tiles(50, 50, tiles_size, tiles_size, grass)], [Tiles(50, 50, tiles_size, tiles_size, dirt)]]

layer_value = 1 #Hardcoded layer value this has to be changed
select_value = 1 #Hardcoded selection value this has to be changed

def create_grid():
    for i in range((HEIGHT*2)//tiles_size):
        pygame.draw.line(display, "White", (0, (i*tiles_size) - scroll[1]), (800, (i*tiles_size) - scroll[1]))
        if i == 0:
            pygame.draw.line(display, "Red", (0, (i*tiles_size) - scroll[1]), (800, (i*tiles_size) - scroll[1]))
    
    for i in range((WIDTH*2)//tiles_size):
        pygame.draw.line(display, "White", ((i*tiles_size) - scroll[0], 0), ((i*tiles_size) - scroll[0], 600))
        if i == 0:
            pygame.draw.line(display, "Red", ((i*tiles_size) - scroll[0], 0), ((i*tiles_size) - scroll[0], 600))

def camera(scroll):
    key_press = pygame.key.get_pressed()
    
    if key_press[pygame.K_w]:
        scroll[1] -= 2
    
    if key_press[pygame.K_s]:
        scroll[1] += 2
    
    if key_press[pygame.K_d]:
        scroll[0] += 2
    
    if key_press[pygame.K_a]:
        scroll[0] -= 2
        

def select_layer(layers, index):
    selected = layers[index]
    
    return selected  



tile_rect = []
def add_tiles(layers, selected_layer, mx, my, click, remove=False):
    
    pos = (mx,my)
    #print(tile_database)
    
    base_hover_x = pos[0] + scroll[0]
    base_hover_y = pos[1] + scroll[1]
    
    hover_x = int(round(base_hover_x / tiles_size - 0.5, 0))
    hover_y = int(round(base_hover_y / tiles_size - 0.5, 0))
    offset = offsets[selected_tile]["tile_offset"]
    if not remove:
        display.blit(tile_database[selected_tile], (hover_x * tiles_size - scroll[0], hover_y * tiles_size - scroll[1]))
    #print(snap)
    #print(hover_x)
    if click and pos[1] > 100:
    
        if snap: tile = Tiles(hover_x * tiles_size + offset[0], hover_y * tiles_size + offset[1], tiles_size, tiles_size, selected_tile)
        else: tile = Tiles(pos[0] + scroll[0], pos[1] + scroll[1], tiles_size, tiles_size, selected_tile)

        loc = str(tile.x) + ':' +str(tile.y)
        layers["layer_"+str(selected_layer)][loc] = [tile.x, tile.y, tile.width, tile.height,  tile.img]
        #print(layers)

     #{'layer_1': {'loc': [272, 272, 16, 16, <rect(272, 272, 16, 16)>]}}  
     
     
#{'layer_0':{'loc':[x,y,w,h,r]}}       
# tile = {'loc':[x,y,w,h,r]}
#[[tile1, tile2], [tile1, tile2], [tile1, tile2]]
    
#{"layer_0":{'loc':[]}}
#layers[layer] = {'loc':[]}
def tile_handler(layers, remove, Mouse_rect, select_layer):
    
    for i, layer in sorted(enumerate(layers), reverse=True):
        
        for j, tile in sorted(enumerate(layers[layer]), reverse=True):
            
            
            tile_data = layers[layer][tile]
            #print(tile_data)
            rect = pygame.Rect(tile_data[0]-scroll[0], tile_data[1]-scroll[1], tile_data[2], tile_data[3])
            #print(rect)
            if remove:
                if rect.colliderect(Mouse_rect):
                    
            
                    del layers[layer][tile]
            
            display.blit(tile_database[tile_data[4]], (rect.x, rect.y))

#{'layer_1': {'192:352': [192, 352, 16, 16, rect]
#{'layer_1': {'locationx:locationy':[tile_img]}}
#{{'locx, locy': [l]}}

#{'map':{"layer_0":{"2:2":[tile.png]}}}
def export_JSON(layers):
    exported_map = {}
    
    for layer in layers:
        for location in layers[layer]:
            exported_map['map'] = layers
            
            
    with open('export.json', 'w') as f:
    
    
        json.dump(exported_map, f)
            
    
def load_map(layers, layer_index, load):
    loaded_map = {}
    with open('assets/saved/export.json', 'r') as f:
        readed_map = json.load(f)
        
        if load == True:
            
            del layers
            layers = readed_map["map"]
            load = False
        for layer in layers:
            layer_index = layer[6:]
    
    return int(layer_index), layers
    #print(layers)
            
        
            
        
     
    
    

            
#Problem: We can't add tiles to the loaded map, we can't add new layers to the loaded map
#TODO: Make the click of a mouse add tiles to the last loc of the mouse cursor. #--------------
def main():
    global click
    global export
    global load
    clock = pygame.time.Clock()
    run = True
    click = False
    remove = False
    export = False
    load = False
    def render():
        global selected_tile
        global layer_value
        global select_value
        global click
        global tiles_size
        global snap
        global export
        global load
        
        display.fill((0, 0, 0))
        camera(scroll)
        if snap:
            #create_grid()
            pass
        
        mx, my = pygame.mouse.get_pos()
        
        Mouse_rect = pygame.Rect(mx, my, tiles_size, tiles_size)
        pygame.draw.rect(display, "Blue", Mouse_rect, 1)
        if remove: pygame.draw.rect(display, "Red", Mouse_rect, 5)
        
        layers = gen_layers(layer_value)
        if load == True: #future me dev.. this is where we load the map, once the key is pressed it sets to true, therefore triggering the function "load_map"
            layer_value, layers = load_map(layers, layer_value, load) 
        #layer_value is the ammount of layers, layers is the new map
        #print(load)
        #print(layer_value)
        tile_handler(layers, remove, Mouse_rect, select_value)
        add_tiles(layers, select_value, mx, my, click, remove)
        if export == True:
            export = False
            export_JSON(layers)
        
        
            
        panel = pygame.draw.rect(display, (70, 80, 70), ((0, 0), (WIDTH, 100)))
        panel_outline = pygame.draw.rect(display, (200, 210, 205), ((-4, -10), (WIDTH + 10, 120)), 10, 10)

        pygame.draw.polygon(display, (150, 160, 150), ((770, 95), (770, 70), (790, 82.5)))
        pygame.draw.polygon(display, (150, 160, 150), ((650, 95), (650, 70), (630, 82.5)))
        pygame.draw.rect(display, (150, 160, 150), ((445, 65), (150, 35)))
        pygame.draw.rect(display, (200, 210, 205), ((440, 65), (160, 35)), 5)

        pygame.draw.rect(display, (150, 160, 150), ((405, 65), (25, 35)), border_radius=20)
        pygame.draw.rect(display, (200, 210, 205), ((400, 65), (35, 35)), 5, 20)

        display.blit(font.render("Current layer: " + str(select_value), False, "White"), (10, 70))
        display.blit(font.render("Selected tile: " + str(selected_tile), False, "White"), (200, 70))
        display.blit(font.render("Tile Scale: " + str(tiles_size), False, "White"), (450, 70))
        display.blit(font.render("Layer: " + str(layer_value), False, "White"), (670, 70))
        display.blit(font.render("Snap", False, "White"), (395, 70))

        if (mx >= 440 and mx <= 600 and my < 95 and my > 65) and click:
            tiles_size *= 2
            if tiles_size == 128: tiles_size = 4
            click = False

        if (mx >= 390 and mx <= 470 and my > 65 and my < 105) and click:
            snap = not snap
            click = False
           

        if ((mx >= 770 and mx <= 790) and (my >= 70 and my <= 95)) and click:
            layer_value += 1
            click = False
        if ((mx >= 630 and mx <= 650) and (my >= 70 and my <= 95)) and click:
            layer_value -= 1
            click = False
#{'dirt':img of dirt}
        for loc, tile in enumerate(tiles_set):
            
            
            display.blit(pygame.transform.scale(tile_database[tile], (32, 32)), ((loc * 35) + 10, 5))

            if selected_tile == next(key for key, val in tile_database.items() if val == tile_database[tile]):
                pygame.draw.rect(display, "Red", (((loc * 35) + 9, 4), (34, 34)), 2, 3)
            if ((mx >= (loc * 35) + 10 and mx <= ((loc + 1) * 35) + 10) and my < 34) and click:
                selected_tile = next(key for key, val in tile_database.items() if val == tile_database[tile])

        try:
            for y in range(layer_value):
                pygame.draw.rect(display, (200 - (y * 5), 200, 100 + (y * 5)), ((767, (y * 32) + 117), (28, 30)))
                pygame.draw.rect(display, (50, 100, 150), ((765, (y * 32) + 115), (32, 32)), 2, 3)
                display.blit(font.render(str(y + 1), False, "Black"), ((771, (y * 32) + 117), (28, 30)))
                if y == select_value - 1:
                    pygame.draw.rect(display, (200, 100, 50), ((765, (y * 32) + 115), (32, 32)), 5, 3)
                if (mx >= 760 and my > ((y * 32) + 85) and my < ((y * 32) + 117)) and click:
                    select_value = y
        except: pass

        pygame.display.update()
    
    
    while run:
        clock.tick(60)
        #print(clock)
        render()
        
        global layer_value
        global select_value
        global selected_tile
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    layer_value += 1
                    #print(layer_value)

                if event.key == pygame.K_DOWN:
                    layer_value -= 1
                
                
                if event.key == pygame.K_e:
                    if select_value < layer_value:
                        
                        select_value += 1
                
                if event.key == pygame.K_q:
                    if select_value > 1:
                        
                        
                        select_value -= 1
                if event.key == pygame.K_i:
                    export = True
                
                if event.key == pygame.K_l:
                    load = True
                
                
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

                if event.button == 3:
                    remove = True
               
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
                
                if event.button == 3:
                    remove = False
                
   
               
      
main()
