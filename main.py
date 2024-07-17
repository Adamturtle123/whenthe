import pygame
import os
import math
from map_loader import Map
from entity import Entity
from items import Item
from inventory import Inventory
WIDTH, HEIGHT = 800, 600

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
display = pygame.Surface((WIDTH, HEIGHT))
pygame.display.set_caption("whenthe")


#{"1:2: radad"}
money = 0
projectiles = []
shops = []
ui_database = {}
item_database = {}
ui_list = os.listdir("UI")
item_list = os.listdir("assets/items")
scroll = [0,0]
player = Entity(500, 60, 10, 20, "assets/player/player.png")
gun = Item(400,60,27,12,"assets/items/gun.png", "rifle")
inventory = Inventory()

def loading_ui(dir_list, ui_database, path):
    for item in dir_list:
            
        img = pygame.image.load(f'{path}/' + item).convert()
        img.set_colorkey((255,255,255))
        ui_database[item] = img.copy()
        
        return ui_database

loading_ui(ui_list, ui_database, "UI") #loading ui
loading_ui(item_list, item_database, "assets/items")
def get_distance_to_player(player, target):
    return math.sqrt(abs((target.hitbox.x - player.hitbox.x)) ^ 2 + abs((target.hitbox.y - player.hitbox.y+20)) ^ 2)


def control():
    key_press = pygame.key.get_pressed()
    if key_press[pygame.K_d]:
        player.movement[0] = player.speed
    
    elif key_press[pygame.K_a]:
        player.movement[0] = -player.speed

    else:
        player.movement[0] = 0

def main():
    
    clock = pygame.time.Clock()
    FPS = 60
    
    
    items = []
    items.append(gun)
    tile_list = os.listdir("assets/tiles")
    tile_database = {}
    world = Map(tile_database, tile_list)
    world_data = world.load_map("export")
    
    def render():
        display.fill((25,25,25))
        #----player stuff
        mx, my = pygame.mouse.get_pos()
        
        
        player.col_type, player.hitbox = player.move(world.tile_rect)
        player.gravity(player.col_type)
        player.update(scroll, display)
        
        
        for proj in projectiles:
            proj.render_projectile(display, scroll)
            #print(proj.movement)
            proj.movement[0] = (math.cos(math.radians(proj.angle)))*proj.speed
            proj.movement[1] = (math.sin(math.radians(proj.angle ) ))*proj.speed
            proj.hitbox.x += proj.movement[0]
            proj.hitbox.y += proj.movement[1] 
        
        #print(projectiles)
        
        for item in items:
            
            item.col_type, gun.hitbox = gun.move(world.tile_rect)
            item.gravity(gun.col_type)
            item.update(scroll, display)
            if int(get_distance_to_player(player, gun)) <= 3:
                display.blit(ui_database["E_key.png"], (gun.hitbox.x-scroll[0], gun.hitbox.y - scroll[1] - 20 ))
            is_picked = gun.pickup(player)
        
            if is_picked and len(inventory.inventory_slots[inventory.slot_index]) < 1:
                
                
                
                inventory.slot_index += 1
                if item.item_name not in inventory.inventory:
                    inventory.inventory[item.item_name] = []
                        #print("creating new subject")
                        
                inventory.inventory[item.item_name].append(item)
                items.remove(item)
                inventory.inventory_slots[inventory.slot_index-1].append(item)
                    
                if inventory.slot_index >= len(inventory.inventory_slots):
                    inventory.slot_index = 0
            
        control()
        selected_item = inventory.select_item()
        if selected_item:
            selected_item.angle = selected_item.item_func(selected_item, mx, my, projectiles, scroll)
            selected_item.hold_item(selected_item, player, display, scroll)
        
        
        for shop in shops:
            key_pressed = pygame.key.get_pressed()
            distance = get_distance_to_player(player, shop)
            
            if int(distance) <= 3:
                display.blit(ui_database["E_key.png"], (shop.hitbox.x - scroll[0], shop.hitbox.y - 20 - scroll[1]))

                if key_pressed[pygame.K_e]:
                    pass
                    
                    
                
            
        
        #-----tile stuff
        world.tiles(world_data, display, scroll, shops, Entity)
        inventory.make_slots(display, 200, 10 )
        
        clock.tick(FPS)
        scroll[0] += (player.hitbox.x - scroll[0] - 200)/20
        scroll[1] += (player.hitbox.y - scroll[1] - 200)/20
        pygame.display.update()
    
    while True:
        
        render()
        surf = pygame.transform.scale(display, (WIDTH*2, HEIGHT*2))
        WINDOW.blit(surf, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_e:
                    pass
                    
                    
                
                
                if event.key == pygame.K_SPACE:
                    player.jumps += 1
                    print(player.jumps)
                    
                    if player.jumps < 2:
                        player.y_momentum = player.jump_force
                        
                    
                    

                    

main()
