import pygame,sys
#imports pygame
pygame.init()
#initialises snake game
from pygame.locals import *
#imports all modules
import random
import time

screen= pygame.display.set_mode((800,600))
#creates a game screen
pygame.mixer.init()
#initialises sound
pygame.display.set_caption("Arush's Car Racing Game")

logo=pygame.image.load("car.png")
#loads up image of car
pygame.display.set_icon(logo)
#sets image of car to screen icon

introfont= pygame.font.Font("freesansbold.ttf",38)
#selects font+size

def introimg(x,y):
#function to set up screen
    intro=pygame.image.load("Introduction for car game.png")
    #loads image
    screen.blit(intro,(x,y))
    #.blit pasts picture on the x and y coordinates

def instructionimg(x,y):
#function to set up instructions screen
    instruct=pygame.image.load("instructions for car game.png")
    #loads instruction image
    run= True
    while run:
        screen.blit(instruct,(x,y))
        pygame.display.update()
        #refreshes screen
        for event in pygame.event.get():
            #for loop checks every event
            if event.type== QUIT:
                run= False
                #if the user presses the cross button, it quits the game

def aboutimg(x,y):
#function to set up about screen
    about=pygame.image.load("About.png")
    #loads about image
    run= True
    while run:
        screen.blit(about,(x,y))
        pygame.display.update()
        #refreshes screen
        for event in pygame.event.get():
            #for loop checks every event
            if event.type== QUIT:
                run= False
                #if the user presses the cross button, it quits the game
                
def play(x,y):
    playtext= introfont.render("PLAY", True, (255,0,0))
    #sets up text for play button
    screen.blit(playtext, (x,y))
    #pastes text on coordinates
def about(x,y):
    abouttext= introfont.render("ABOUT", True, (255,0,0))
    #sets up text for about button
    screen.blit(abouttext, (x,y))
    #pastes text on coordinates
def instruction(x,y):
    instructiontext= introfont.render("INSTRUCTION", True, (255,0,0))
    #sets up text for about button
    screen.blit(instructiontext, (x,y))
    #pastes text on coordinates

def introscreen():
    #introduction screen
    run = True
    pygame.mixer.music.load("startingMusic.mp3")
    #loads sound
    pygame.mixer.music.play()
    #plays sound
    while run:
        screen.fill((0,0,0))
        #fills screen with rgb black color
        introimg(0,0)
        #calls intro image function
        play(100,500)
        #calls play function with coordinates
        instruction(260,500)
        #calls instruction function
        about(580,500)
        #calls about function

        x,y= pygame.mouse.get_pos()
        #pygame function which returns coordinates

        button1= pygame.Rect(60, 490,170, 50)
        #stores coordinates of bottom right (60,440) and top left coordinate (170,50)
        button2= pygame.Rect(250, 490, 300, 50)
        button3= pygame.Rect(560, 490, 180, 50)

        pygame.draw.rect(screen,(255,255,255), button1,10)
        #draws rectangle on the screen, white, with the button 1 coordinates and a thickness of 10
        pygame.draw.rect(screen,(255,255,255), button2,10)
        pygame.draw.rect(screen,(255,255,255), button3,10)

        if button1.collidepoint(x,y):
        #if button1 (area) is colliding with the mouse area
            pygame.draw.rect(screen,(0,255,255), button1,10)
            #changes colour of button
            if click:
                countdown()
        if button2.collidepoint(x,y):
        #if button2 (area) is colliding with the mouse area
            pygame.draw.rect(screen,(0,255,255), button2,10)
            #changes colour of button
            if click:
                instructionimg(0,0)
                #calls the instruction image

        if button3.collidepoint(x,y):
        #if button3 (area) is colliding with the mouse area
            pygame.draw.rect(screen,(0,255,255), button3,10)
            #changes colour of button
            if click:
                aboutimg(0,0)
                #calls the about image
                
        click=False

        for event in pygame.event.get():
            #checks the events
            if event.type==pygame.QUIT:
                #if user quits the program
                run=False
                    #stops loop
            if event.type==pygame.MOUSEBUTTONDOWN:
                #if mouse button is pressed
                if event.button==1:
                    #if left click...
                    click=True
            
        pygame.display.update()
            #updates display

def countdown():
    font2= pygame.font.Font("freesansbold.ttf",85)
    #changes font size
    countdownbackground=pygame.image.load("bg.png")
    #loads background image
    
    three=font2.render('3', True, (187,30,16))
    #defines the text for the number 3
    two=font2.render('2', True, (255,130,16))
    one=font2.render('1',True, (187,30,106))
    go=font2.render('GO',True, (0,255,0))

    screen.blit(countdownbackground,(0,0))
    #puts the background in the centre
    pygame.display.update()

    screen.blit(three,(350,250))
    #adds number 3 to screen
    pygame.display.update()
    time.sleep(1)
    #waits for one second
    
    screen.blit(countdownbackground,(0,0))
    #puts the background in the centre
    pygame.display.update()
    time.sleep(1)

    screen.blit(two,(350,250))
    #adds number 2 to screen
    pygame.display.update()
    time.sleep(1)
    #waits for one second
    
    screen.blit(countdownbackground,(0,0))
    #puts the background in the centre
    pygame.display.update()
    time.sleep(1)

    screen.blit(one,(350,250))
    #adds number 1 to screen
    pygame.display.update()
    time.sleep(1)
    #waits for one second

    screen.blit(countdownbackground,(0,0))
    #puts the background in the centre
    pygame.display.update()
    time.sleep(1)

    screen.blit(go,(300,250))
    #adds 'go' to screen
    pygame.display.update()
    time.sleep(1)
    #waits for one second

    gameloop()
    pygame.display.update()


def gameloop():
    pygame.mixer.music.load("BackgroundMusic.mp3")
    #loads background music
    pygame.mixer.music.play()
    #plays background music
    crash_sound=pygame.mixer.Sound("car crash.wav")
    score_value=0
    font1= pygame.font.Font("freesansbold.ttf",25)

    def show_score(x,y):
    #function to display the score
        score=font1.render("SCORE: "+str(score_value), True, (255,0,0))
        screen.blit(score,(x,y))

    with open("highscore.txt","r")as f:
    #opens a file which contains all time highscore
        highscore=f.read()
        #stores the value in the file in the highscore variable
        
    def show_highscore(x,y):
    #function to display the  highscore
        hiscore=font1.render("HIGH SCORE: "+str(highscore), True, (255,0,0))
        screen.blit(hiscore,(x,y))
        pygame.display.update()

    def gameover():
        gameoverimg=pygame.image.load("gameover.png")
        run=True
        #runs game
        while run:
        #while game is running
            screen.blit(gameoverimg,(0,0))
            #displays game over
            time.sleep(0.5)
            #waits for 0.5 seconds before displaying score
            show_score(300,400)
            time.sleep(0.5)
            show_highscore(330,450)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    run=False
                    pygame.quit()
                    sys.exit()
                if event.type== pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        #if the space bar is pressed down
                        countdown()
                    if event.key== pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    bg= pygame.image.load("bg.png")
    
    maincar=pygame.image.load("car.png")
    maincarx=350
    maincary=495
    maincarxchange=0
    maincarychange=0
    #sets up main car with coordinates
    
    car1=pygame.image.load("car1 for car game.png")
    car1x=random.randint(178,490)
    car1y=100
    car1ychange= 5
    #sets up car1 with coordinates and speed of 10 downwards

    car2=pygame.image.load("car2 for car game.png")
    car2x=random.randint(178,490)
    car2y=100
    car2ychange=5
    #sets up car 2 

    car3=pygame.image.load("car3 for game.png")
    car3x=random.randint(178,490)
    car3y=100
    car3ychange= 5
    #sets up car 3

    run=True
    while run:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run=False
                pygame.quit()
                sys.exit()
        #allows user to quit the game
    
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    #if the right arrow is is pressed down
                    maincarxchange+=5
                    #moves car 5 pixels to right
                
                if event.key== pygame.K_LEFT:
                        maincarxchange-=5
                        #moves car 5 pixels to left
                if event.key== pygame.K_UP:
                        maincarychange-=5
                        #moves car 5 pixels up
                if event.key== pygame.K_DOWN:
                        maincarychange+=5
                        #moves car 5 pixels down

            if event.type== pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    maincarxchange=0
                if event.key== pygame.K_LEFT:
                        maincarxchange=0
                if event.key== pygame.K_UP:
                        maincarychange=0
                if event.key== pygame.K_DOWN:
                        maincarychange=0
                #^^This if selection stops the car from moving as soon as the key is not pressed                               


        if maincarx<178:
            #if the main car is beyond the limit of the road on left side...
            maincarx=178
            #stops car from passing
            
        if maincarx>490:
            #if the main car is beyond the limit of the road on right side...
            maincarx=490
            #stops car from passing

        if maincary>495:
            #if main car is beyond the limits on the bottom...
            maincary=495
            #stops car from passing
            
        if maincary<0:
            #if main car is beyond limits on the top...
            maincary=0
            #stops car from passing

        screen.fill((0,0,0))
        #fills screen with black colour
        
        screen.blit(bg,(0,0))
        #puts the background on the screen
        
        screen.blit(maincar,(maincarx, maincary))
        #puts main car with the coordinates
        
        screen.blit(car1,(car1x, car1y))
        #puts car1 with the coordinates
        screen.blit(car2,(car2x, car2y))
        #puts car2 with the coordinates
        screen.blit(car3,(car3x, car3y))
        #puts car3 with the coordinates

        show_score(570,280)
        #displays score
        show_highscore(0,0)
        #displays highscore

        maincarx+=maincarxchange
        #changes the car x coordinates when moved
        maincary+=maincarychange
        #changes the car y coordinates

        car1y+=car1ychange
        car2y+=car2ychange
        car3y+=car3ychange

        if car1y>670:
            #if car touches the exact bottom
            car1y=-50
            #puts the car at the top
            car1x=random.randint(178,490)
            #chooses random x coordinate for car
            score_value+=1
            #adds one to score as it means that the the enemy car didn't touch main car

        if car1y>670:
            #if car touches the exact bottom
            car1y=-50
            #puts the car at the top
            car1x=random.randint(178,490)
            #chooses random x coordinate for car
            score_value+=1
            #adds one to score as it means that the the enemy car didn't touch main car

        if car2y>670:
            #if car touches the exact bottom
            car2y=-70
            #puts the car at the top
            car2x=random.randint(178,490)
            #chooses random x coordinate for car
            score_value+=1
            #adds one to score as it means that the the enemy car didn't touch main car

        if car3y>670:
            #if car touches the exact bottom
            car3y=-10
            #puts the car at the top
            car3x=random.randint(178,490)
            #chooses random x coordinate for car
            score_value+=1
            #adds one to score as it means that the the enemy car didn't touch main car

        if score_value> int(highscore):
            highscore=score_value
            '''with open("highscore.txt","r")as f:'''

        def iscollision(car1x,car1y, maincarx, maincary):
            #function which checks if there is a collision
            distance=abs(car1x-maincarx)+abs(car1y-maincary)
            #adds the total distance between the car

            if distance<50:
                return True
            else:
                return False
        coll1=iscollision(car1x,car1y, maincarx, maincary)
        #passes the coordinates of car one to iscollision function
        coll2=iscollision(car2x, car2y, maincarx, maincary)
        #passes the coordinates of car two to iscollision function
        coll3=iscollision(car3x, car3y, maincarx, maincary)
        #passes the coordinates of car three to iscollision function

        if coll1 or coll2 or coll3:
        #if the either of the functions returns true
            car1ychange=0
            car2ychange=0
            car3ychange=0
            
            car1y=0
            car2y=0
            car3y=0

            maincarxchange=0
            maincarychange=0
            pygame.mixer.music.stop()
            crash_sound.play()
            time.sleep(1)
            gameover()
        with open("highscore.txt","w")as f:
          f.write(str(highscore))
        pygame.display.update()
                    
introscreen()

    
