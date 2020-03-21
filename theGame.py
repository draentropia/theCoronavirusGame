import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The GaMe')

clock = pygame.time.Clock()
crashed = False
coronaImg = pygame.image.load('images/corona.png')
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
block_color = ( 53,115,255)

virus_width = 150

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "  +str(count), True, black)
    game_display.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(game_display, color, [thingx, thingy, thingw, thingh])

def virus(x,y):
    game_display.blit(coronaImg, (x,y))

def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, large_text)
    TextRect.center = ((display_width/2), (display_height/2))
    game_display.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You crashed')

def game_loop():
    game_exit = False
    x = (display_width * 0.45)
    y = (display_height * 0.75)
    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    thing_count = 1

    dodged = 0

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        game_display.fill(white)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        virus(x,y)
        things_dodged(dodged)

        if x > display_width - virus_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+virus_width > thing_startx and x + virus_width < thing_startx+thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()