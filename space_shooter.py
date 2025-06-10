import pygame
from os.path import join
from random import randint

pygame.init()
#for audio
pygame.mixer.init()
#importing bg music
bg_music = pygame.mixer_music.load(join('audio', 'game_music.wav'))
pygame.mixer_music.play(-1)

#for miscallenous musics
laser_music = pygame.mixer.Sound(join('audio', 'laser.wav'))
collide_music = pygame.mixer.Sound(join('audio', 'explosion.wav'))
death_music = pygame.mixer.Sound(join('audio', 'damage.ogg'))


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

#importing obstacles
obstacle_img = pygame.image.load(join('images', 'meteor.png'))
obstacles = []
for i in range(5):
        obstacle_rect = obstacle_img.get_rect(midbottom = (randint(0 , WIDTH), randint(-500 ,-50)))
        obstacles.append(obstacle_rect)
obstacle_speed = 3
obstacle_speed +=0.0001


#stars location 
star_pos= [(randint(0, WIDTH), randint(0, HEIGHT)) for i in range(30)]

#SPEED OF SPACESHIP
speed = 5

#LASERS FIRED
lasers = []
laser_speed = 6

#Run vairable
run = True

#SCORE
score = 0
font = pygame.font.Font(None, 50)

#GAME OVER
over = pygame.font.Font(None, 100)

#main game loop
while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        #FOR FIRING LASER:
                if event.type == pygame.MOUSEBUTTONDOWN:
                      if event.button == 1:
                            #NOW LETS CREATE A LASER
                            #sound 
                            laser_music.play()
                            laser_rect = laser_img.get_rect(midbottom = player_rect.midtop)
                            lasers.append(laser_rect)

        #AS NOW FOR UPDATING POSITION OF LASERS:
        for laser_rect in lasers[:]:
              laser_rect.y -= laser_speed

              if laser_rect.bottom < 0:
                    lasers.remove(laser_rect)
        
        #for movement of spaceship
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and player_rect.top>0:
             player_rect.y -= speed

        if key[pygame.K_s] and player_rect.bottom<HEIGHT:
             player_rect.y += speed

        if key[pygame.K_a] and player_rect.left>0:
             player_rect.x -= speed

        if key[pygame.K_d] and player_rect.right<WIDTH:
             player_rect.x += speed

        screen.fill((10,10,30))

        #for stars
        for pos in star_pos:
             screen.blit(stars, pos)
        
        #FOR PLAYERS    
        screen.blit(player_img, player_rect)
        clock.tick(60)

        #LASERS FIRED
        for laser_rect in lasers:
              screen.blit(laser_img, laser_rect)

        #OBSTACLES
        for obstacle_rect in obstacles:
                #OBASTACLES FALLING
                obstacle_rect.y += obstacle_speed
                if obstacle_rect.top > HEIGHT:
                        obstacle_rect.x = randint(0, WIDTH)         # random horizontal position
                        obstacle_rect.y = randint(-500, -50)        # start above the screen

                #actually drawing the osbtacle2
                screen.blit(obstacle_img, obstacle_rect)
                

        #DETECTING OBSTACLE AND LASER COLLISION
        for laser_rect in lasers[:]:
                for obstacle_rect in obstacles[:]:
                        if laser_rect.colliderect(obstacle_rect):
                                collide_music.play() #music first hehe
                                lasers.remove(laser_rect)
                                obstacle_rect.x = randint(0, WIDTH)
                                obstacle_rect.y = randint(-500, -50)
                                score +=1
                                break

        #FOR COLLISION WITH PLAYER
        for obstacle_rect in obstacles[:]:
               if player_rect.colliderect(obstacle_rect):
                        death_music.play()
                        game_over = over.render("GAME OVER", True, ('gray'), ('brown'))
                        screen.blit(game_over, (WIDTH/2, HEIGHT/2))
                        run = False
                      
                      
        score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surf, (20, 20))
        pygame.display.update()
pygame.quit() 
