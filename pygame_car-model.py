import pygame 
import sys # for ending python script 
import random
import pygame.font
pygame.font.init()



screen_width = 1000
screen_height = 600
player_height = 100
player_width = 200
rect_x = 700
rect_y = 300
#rect_x = random.randint(100,600)
#rect_y = random.randint(100,500)
rect_size_x = 200
rect_size_y = 100
color = (164,14,76)
speed_rect_x =-1



# initialize pygame and define time & clock




# set size of window in pixels
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

# set name of the window
pygame.display.set_caption("My Pygame Window")


# create player sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #self.image = pygame.Surface((player_width, player_height))
        #self.image.fill((9,64,116))
        self.image = pygame.transform.rotate(pygame.image.load('car.png'), 180)
        self.rect = self.image.get_rect()

       
        self.rect = self.image.get_rect()
        #self.rect.x = random.randint(100,500)
        #self.rect.y = random.randint(100,300)
        self.rect.x = 20
        self.rect.y = 100

# create player sprite instance
player = Player(100, 100)

# create rectangle sprite class
class Rectangle(pygame.sprite.Sprite):
    def __init__(self, x, y, size_x, size_y, color,speed):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.image.load('car1.png'), 0)
        self.rect = self.image.get_rect()
        #self.rect.x = random.randint(100,500)
        #self.rect.y = random.randint(100,500)
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.speed = speed_rect_x
        self.collided = False
       

    def update(self):
        self.rect.move_ip(int(speed_rect_x), 0) # move the rectangle by its speed vector each update

# create rectangle sprite instance
rectangle = Rectangle(rect_x, rect_y, rect_size_x, rect_size_y, color,speed_rect_x)



# add player and rectangle sprites to sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(player, rectangle)

#----------------- initialize pygame module
pygame.init()
clock = pygame.time.Clock()


#-------------------
# background image
background_image = pygame.transform.rotate(pygame.image.load("Background.jpg").convert(),180)
background_x = 0
background_x2 = background_image.get_width()
scroll_speed = 5


# game running conditions
while True:
    # handle events --> if user quits 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # exits python script 
    clock.tick(200)

    #----------------
    #background
    background_x -= scroll_speed
    background_x2 -= scroll_speed
    if background_x < -background_image.get_width():
        background_x = background_image.get_width()
    if background_x2 < -background_image.get_width():
        background_x2 = background_image.get_width()
    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x2, 0))

    # handle player movement + borders
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if player.rect.x > 0:
            player.rect.x -= 1
        else: 
            print('border_-x')
            
    #else:
        #player.rect.x +=1  to move player with 1 to +x; constant velo
    if keys[pygame.K_d]:
        if player.rect.x < screen_width - player_width:
            player.rect.x += 1
        else:
            print('border_x')


    if keys[pygame.K_w]:
        if player.rect.y + 20 > 0:
            player.rect.y -= 1
        else:
            print('border_y')


    if keys[pygame.K_s]:
        if player.rect.y < screen_height - player_height:
            player.rect.y += 1
        else:
            print('border_-y')
    
    #-------------------------------------------------------------------------
    #rectangle collision with borders
    
    rectangle.update()
    
    #if rectangle.rect.x <0:
       # rectangle.rect.x =0
       # all_sprites.remove(rectangle)

    if rectangle.rect.y + rect_size_y >screen_height:
        print('rect_border_-y')
        all_sprites.remove(rectangle)

    if rectangle.rect.y < 0:
        print('rect_border_y')
        all_sprites.remove(rectangle)

    for i in range(0,100):
        if rectangle.rect.x <0:
            print('border_rect_-x')
            rectangle.rect.x = 1100
            rectangle.rect.y = random.randint(0,300)

    
    #----------------------------------------------------------------
    # handle collision between player and rectangle
    if player.rect.colliderect(rectangle.rect):
        print('collision')
        if keys[pygame.K_a]:
            player.rect.x += 1
        if keys[pygame.K_d]:
            player.rect.x -= 1
        if keys[pygame.K_w]:
            player.rect.y += 1
        if keys[pygame.K_s]:
            player.rect.y -= 1
        if rectangle.rect.x < player.rect.x + player_width:
            print('pass')
            break
            rectangle.rect.x =1000  #moves rect out of way
            rectangle.rect.y+=0  #moves rect out of way
            #all_sprites.remove(rectangle)  ##removes rectangle if collides with player
        
    #----------------------------
    # draw game over screen
   
    #------------------------------
    # restart game
   

    # draw the background color of window; still in loop 
    #screen.fill((255, 255, 255))

    # draw the sprites on the screen
    
    
    screen.blit(player.image, player.rect)
    player.update(size[1], size[1])
    all_sprites.update()
    all_sprites.draw(screen)
    
    # update the display 
    pygame.display.update()



