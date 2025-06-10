import pygame
from os.path import join
from random import randint

pygame.init()

WIDTH, HEIGHT= 1280,720
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Space Shooter')
clock = pygame.time.Clock()

#surface
surface = pygame.Surface((100,200))
surface.fill('orange')
x = 100

#importing player image
player_img = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_img.get_rect(center = (WIDTH/2, HEIGHT/1.5))

#importing stars
stars = pygame.image.load(join( 'images', 'star.png')).convert_alpha()

#imorting laser
laser_img = pygame.image.load(join('images', 'laser.png'))

#stars location 
star_pos= [(randint(0, WIDTH), randint(0, HEIGHT)) for i in range(20)]

#SPEED OF SPACESHIP
speed = 5

#LASERS FIRED
lasers = []
laser_speed = 3

#Run vairable
run = True

#main game loop
while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        #FOR FIRING LASER:
                if event.type == pygame.MOUSEBUTTONDOWN:
                      if event.button == 1:
                            #NOW LETS CREATE A LASER
                            laser_rect = laser_img.get_rect(midbottom = player_rect.midtop)
                            lasers.append(laser_rect)

        #AS NOW FOR UPDATING POSITION OF LASERS:
        for laser_rect in lasers[:]:
              laser_rect.y -= laser_speed

              if laser_rect.bottom < 0:
                    lasers.remove(laser_rect)
        
        #for movement of spaceship
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
             player_rect.y -= speed

        if key[pygame.K_s]:
             player_rect.y += speed

        if key[pygame.K_a]:
             player_rect.x -= speed

        if key[pygame.K_d]:
             player_rect.x += speed

        
        




        screen.fill('gray')

        #for stars
        for pos in star_pos:
             screen.blit(stars, pos)
        
        #FOR PLAYERS    
        screen.blit(player_img, player_rect)
        clock.tick(60)

        #LASERS FIRED
        for laser_rect in lasers:
              screen.blit(laser_img, laser_rect)

        pygame.display.update()
pygame.quit() 
