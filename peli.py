import pygame
import time
import random
import winsound
import threading

pygame.init()                                                                  #starts pygame


display_width = 800                                                            #parameters for display
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (0, 220, 0)

opiskelija_width = 90
opiskelija_height = 90
beer_width = 70
beer_height = 80
dice_width = 67
dice_height = 67
kela_width = 70
kela_height = 70


gameDisplay = pygame.display.set_mode((display_width, display_height))         #sets dislpay reso
pygame.display.set_caption('Get nobs or die tryin Beta 0.1')                            #nameofthegame
clock = pygame.time.Clock()

#Loads car image
opiskelijaImg = pygame.image.load('lobo.png')
beerImg = pygame.image.load('beer.png')
diceImg = pygame.image.load('dice.png')
kelaImg = pygame.image.load('kela.png')

# mauu, matu, kalja


def mauu():
    winsound.PlaySound('maijumauu.wav', winsound.SND_FILENAME)


def matu():
    winsound.PlaySound('matuhavisit.wav', winsound.SND_FILENAME)


def kali():
    aani = random.randrange(0, 3)
    #print(aani)
    if aani == 0:
        winsound.PlaySound('joonaskali.wav', winsound.SND_FILENAME)
    elif aani == 1:
        winsound.PlaySound('joonaskalii.wav', winsound.SND_FILENAME)
    elif aani == 2:
        winsound.PlaySound('joonaskaliii.wav', winsound.SND_FILENAME)
    else:
        print('lol')

def button(msg, x, y, w, h, ib, ab, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ab, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "start":
                game_loop()
            elif action == "lol":
                print("lol")





    else:
        pygame.draw.rect(gameDisplay, ib, (x, y, w, h))

    smallText = pygame.font.Font('freesansbold.ttf', 28)
    TextSurf, TextRect = text_objects("Start!", smallText)
    TextRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(TextSurf, TextRect)



def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 38)
        TextSurf, TextRect = text_objects("Get nobs or die tryin B 0.1", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)



        button("Start!", 150, 450, 100, 50, green, bright_green, "start")
        #pygame.draw.rect(gameDisplay, bright_green, (150, 450, 100, 50))


        pygame.display.update()
        clock.tick(15)

def nobs_gained(counter):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Nobs Gained: " +str(counter), True, black)
    gameDisplay.blit(text, (0, 0))


def beers_drank(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Beers drank: " +str(count), True, black)
    gameDisplay.blit(text, (250, 0))


def beer(beerx, beery):
    gameDisplay.blit(beerImg, (beerx, beery))


def kela(kelax, kelay):
    gameDisplay.blit(kelaImg, (kelax, kelay))


def dice(dicex, dicey):
    gameDisplay.blit(diceImg, (dicex, dicey))


#Displays car
def opiskelija(x, y):
    gameDisplay.blit(opiskelijaImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


#function for messages
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 28)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

#function for failure
def failure():
    thread_matu = threading.Thread(target=matu)
    thread_matu.start()
    message_display("TUKIKUUKAUDET LOPPU!")




def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    counter = 0
    x_change = 0

    beer_startx = random.randrange(0, display_width)
    beer_starty = -600
    beer_speed = 7

    dice_startx = random.randrange(0, display_width)
    dice_starty = -400
    dice_speed = 7

    kela_startx = random.randrange(0, display_width)
    kela_starty = -1200
    kela_speed = 3
#    block_width = 100
#    block_height = 100

    gained = 0
    drank = 0


    gameExit = False

    while not gameExit:
        for event in pygame.event.get():                                            #creates loop for the game
            if event.type == pygame.QUIT:                                           #enables quit
                pygame.quit()
                quit()


    #Movement definitions
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   # if x > 100:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
# if x > display_width - opiskelija_width or x < 0:




            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0


        x += x_change
        gameDisplay.fill(white)

        #def blocks(blockx, blocky, blockw, bloch, color):
        beer(beer_startx, beer_starty)
        beer_starty += beer_speed
        dice(dice_startx, dice_starty)
        dice_starty += dice_speed
        kela(kela_startx, kela_starty)
        kela_starty += kela_speed
        opiskelija(x, y)
        nobs_gained(gained)
        beers_drank(drank)

       # if x > display_width - opiskelija_width or x < 0:

            #failure()
        if beer_starty > display_height:
            beer_starty = 0 - beer_height
            beer_startx = random.randrange(0, display_width)
        if dice_starty > display_height:
            dice_starty = 0 - dice_height
            dice_startx = random.randrange(0, display_width)
        if kela_starty > display_height:
            kela_starty = -1200
            kela_startx = random.randrange(0, display_width)


        if y < beer_starty + beer_height:
            #print('lol')
            if beer_startx < x + opiskelija_width and beer_startx + beer_width > x:
            #if x > beer_startx and x < beer_startx + beer_width or x + opiskelija_width > beer_startx and x + opiskelija_width < beer_startx + beer_width:
                #print('x')
                drank += 1
                thread_kali = threading.Thread(target=kali)
                thread_kali.start()
                beer_speed += 0.9
                dice_speed += 0.5
                kela_speed += 0.7

                beer_starty = -400
                beer_startx = random.randrange(0, display_width)

                #failure()

        if y < dice_starty + dice_height:
            #print('apua')
            if dice_startx < x + opiskelija_width and dice_startx + opiskelija_width > x:
            #if x > dice_startx and x < dice_startx + dice_width or x + opiskelija_width > dice_startx and x + opiskelija_width < dice_startx + dice_width:
                gained += 1
                thread_mau = threading.Thread(target=mauu)
                thread_mau.start()
                dice_starty = -200
                dice_startx = random.randrange(0, display_width)

                #print(gained)
        if y < kela_starty + kela_height:
            if kela_startx < x + opiskelija_width and kela_startx + opiskelija_width > x:
                failure()


        pygame.display.update()                                                     #updates screen
        clock.tick(60)                                                              #frames per second

game_intro()
game_loop()
pygame.quit()                                                                   #quits pygame
quit()
