from pygame import *
from math import *
from random import *


width,height=1800,900
screen=display.set_mode((width,height))
gameScreen="Main" #What screen it's on (Main, Scenes, Controls, and Credits)
#Colors
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
clock = time.Clock()

# Player
playerx = 100
playery = 100
playerH=300
playerW=100
VY=2
direction="Right"
ONGROUND=False
playerHealth=100
playerSprint=100

checker=1  #Checks if the player doesn't keep moving

rapid=0 #MagicArcher can't rapidly shoot
bullets=[] #Bullet list is for all the arrows shot
v=[20,0] #The speed at which the arrows are being shot at



#Main
scene=1 #scene number

frame=0 #player frame 
jeromeFrame=0 #jeromes frame
magicArcherFrame=0 #magic archer's frame
magicArcherFrame2=0 #second magic archer's frame
move=0 #the x value for the whole game
playerMovement="Walking" #this includes, walking, running, attacking, and more!
playerRect=Rect(443,585,90,200) #player's hit box

magicArcherSpeed1=0 #magic archer's speed
magicArcherMovement1="Nothing" #movement includes: waslking, running, attacking, and idle
magicArcherDirection1="Left" #direction
magicArcherSpeed2=0 #the speed
magicArcherMovement2="Nothing" #same as above, just a difference archer
magicArcherDirection2="Left" #same as above, just a difference archer

hellHoundFrame1=0 #frame
hellHoundSpeed1=0 #speed
hellHoundMovement1="Idle" #movement
hellHoundDirection1="Left" #direction
hellHoundFrame2=0 #frame
hellHoundSpeed2=0 #speed
hellHoundMovement2="Idle" #movement
hellHoundDirection2="Left" #direction
hhh1=100 #hell hound health
hellHoundHealth1=100 #health for hh1
hellHoundHealth2=100 #health for hh2
magicArcherHealth1=100 #health for ma1
magicArcherHealth2=100 #health for ma2


rapidAttackHellHound1=0 #makes it so the hh can't rapidly attack
rapidAttackHellHound2=0 #takes it so the hh can't rapidly attack
scene3TextBoxChecker=False #text box checker
scene4TextBoxChecker=False #text box checker


# Import
scene_one=image.load("scene1.png").convert_alpha() #scene 1 image load
monitorScreen=image.load("monitorscreen.png").convert_alpha() #image load
monitorScreen2=image.load("monitorscreen2.png").convert_alpha()#image load
i0=image.load("0.png").convert_alpha()#image load
i1=image.load("1.png").convert_alpha()#image load
i2=image.load("2.png").convert_alpha()#image load
i3=image.load("3.png").convert_alpha()#image load

scene4Background0=image.load("Scene4Backgrounds\\background0.png").convert_alpha()#image load
scene4Background1=image.load("Scene4Backgrounds\\background1.png").convert_alpha()#image load
scene4Background2=image.load("Scene4Backgrounds\\background2.png").convert_alpha()#image load
scene4Background3=image.load("Scene4Backgrounds\\background3.png").convert_alpha()#image load

scene5Background0=image.load("Scene5Backgrounds\\background0.png").convert_alpha()#image load
scene5Background1=image.load("Scene5Backgrounds\\background1.png").convert_alpha()#image load
scene5Background2=image.load("Scene5Backgrounds\\background2.png").convert_alpha()#image load
scene5Background3=image.load("Scene5Backgrounds\\background3.png").convert_alpha()#image load

playerRightIdle0=image.load("Player\\PlayerRightIdle0.png").convert_alpha()#image load
playerLeftIdle0=image.load("Player\\PlayerLeftIdle0.png").convert_alpha()#image load
wagon=image.load("wagon.png").convert_alpha()#image load
archer=image.load("archer.png").convert_alpha()#image load
scene6Background=image.load("scene6background.png").convert_alpha()

#Objects
rightArrow=image.load("Objects\\rightArrow.png").convert_alpha()#image load
leftArrow=image.load("Objects\\leftArrow.png").convert_alpha()#image load
rightFire=image.load("Objects\\rightFire.png").convert_alpha()#image load
leftFire=image.load("Objects\\leftFire.png").convert_alpha()#image load
mixer.init() #music init
mixer.music.load("Music\\music1.ogg") #load it
mixer.music.play() #play song

playerForwardWalk=[] #player script
playerBackwardWalk=[]#player script
playerRun=[]#player script
playerBackwardRun=[]#player script
playerAttackRight=[]#player script
playerAttackLeftBoxRect=Rect(playerx,playery,130,200) #left hit box

jeromeBackwardIdle=[] #jerome script
rapidAttack=0 #player can't rapidly attack

magicArcherBackwardRun=[] #magic archer script
magicArcherBackwardIdle=[]#magic archer script
magicArcherForwardIdle=[]#magic archer script
magicArcherForwardAttack=[]#magic archer script
magicArcherBackwardAttack=[]#magic archer script

magicArcherRightSpin=[]#magic archer script
magicArcherLeftSpin=[]#magic archer script


hellHoundBackwardJump=[] #hell hound script
hellHoundForwardJump=[] #hell hound script
hellHoundBackwardAttack=[] #hell hound script
hellHoundForwardAttack=[] #hell hound script
hellHoundBackwardRun=[] #hell hound script
hellHoundForwardRun=[] #hell hound script
deerGrasing=[] #deer script
playerAttackLeft=[] #player script

hammerSwordRight=[] #hammer sword script
hammerSwordLeft=[]#hammer sword script
hammerSwordAttackRight=[]#hammer sword script
hammerSwordAttackLeft=[]#hammer sword script
hammerSwordFrame=0 #hammer sword frame
hammerSwordSpeed=0 #hammer sword speed 
hammerSwordMovement="Idle" #movement
hammerSwordHealth=100 #hammer sword health

playerAttackLeftBoxRect=Rect(playerx,playery,130,200) #left hit box
hellHoundRect=Rect(-move+4500+hellHoundSpeed1,665,200,100) #hell hound hit box
hellHoundRect2=Rect(-move+4500+hellHoundSpeed1,665,200,100) #hell hound hit box

#attack checkers
rightArrowCheck=False
attackright=False
attackleft=False
attackHellHound1=False
attackHellHound2=False
attackMagicArcher1=False
attackMagicArcher2=False
attackHammerSword=False

#All text scene boxes lists
scene3TextBox=[]
scene3TextBoxNumber=0
scene4TextBox=[]
scene4TextBoxNumber=0

deerGrasingFrame=0 #deer grasing frame
attackpoint=0 

#IMPORTING IMABGES
for i in range(8):
    playerForwardWalk.append(image.load("Player\\PlayerWalkingForward" + str(i) + ".png"))
for i in range(8):
    playerBackwardWalk.append(image.load("Player\\PlayerWalkingBackward" + str(i) + ".png"))
for i in range(8):
    playerForwardWalk.append(image.load("Player\\PlayerWalkingForward" + str(i) + ".png"))
for i in range(8):
    playerRun.append(image.load("Player\\PlayerRunningForward" + str(i) + ".png"))
for i in range(8):
    playerBackwardRun.append(image.load("Player\\PlayerRunningBackward" + str(i) + ".png"))   

for i in range(3):
    jeromeBackwardIdle.append(image.load("Jerome\\JeromeLeftIdle" + str(i) + ".png"))
jeromeName=image.load("Jerome\\jeromeText.png")
ETalk=image.load("Jerome\\ETalk.png")

for i in range(8):
    magicArcherBackwardRun.append(image.load("MagicArcher\\magicArcherBackwardRun" + str(i) + ".png"))   
for i in range(8):
    magicArcherBackwardIdle.append(image.load("MagicArcher\\magicArcherBackwardIdle" + str(i) + ".png"))
for i in range(8):
    magicArcherForwardIdle.append(transform.flip(magicArcherBackwardIdle[i],True,False))
for i in range(15):
    magicArcherForwardAttack.append(image.load("MagicArcher\\magicArcherForwardAttack" + str(i) + ".png"))
for i in range(15):
    magicArcherBackwardAttack.append(transform.flip(magicArcherForwardAttack[i],True,False))

for i in range(6):
    hellHoundBackwardJump.append(image.load("HellHound\\HellHoundBackwardJump" + str(i) + ".png"))
for i in range(6):
    hellHoundForwardJump.append(transform.flip(hellHoundBackwardJump[i],True,False))
for i in range(6):
    hellHoundBackwardAttack.append(image.load("HellHound\\HellHoundBackwardAttack" + str(i) + ".png"))
for i in range(6):
    hellHoundForwardAttack.append(transform.flip(hellHoundBackwardAttack[i],True,False))
for i in range(5):
    hellHoundBackwardRun.append(image.load("HellHound\\HellHoundBackwardRun" + str(i) + ".png"))
for i in range(5):
    hellHoundForwardRun.append(transform.flip(hellHoundBackwardRun[i],True,False))

for i in range(14):
    scene3TextBox.append(image.load("Scene3Text\\Text" + str(i+1) + ".png"))
for i in range(12):
    scene4TextBox.append(image.load("Scene4Text\\Text" + str(i+1) + ".png"))
for i in range(5):
    playerAttackRight.append(image.load("Player\\playerRightAttack" + str(i) + ".png"))
for i in range(5):
    playerAttackLeft.append(transform.flip(playerAttackRight[i],True,False))
simonidle=image.load("Simon/SimonLeftIdle0.png")
wagon2=image.load("Objects/wagon.png")
well=image.load("Objects/well.png")

for i in range(8):
    hammerSwordRight.append(image.load("HammerE\\HammerEWalkRight" + str(i) + ".png"))
for i in range(8):
    magicArcherRightSpin.append(image.load("MagicArcher\\magicArcherRightSpin" + str(i) + ".png"))
for i in range(8):
    magicArcherLeftSpin.append(transform.flip(magicArcherRightSpin[i],True,False))
for i in range(8):
    hammerSwordLeft.append(transform.flip(hammerSwordRight[i],True,False))
for i in range(10):
    hammerSwordAttackRight.append(image.load("HammerE\\HammerEAttackRight" + str(i) + ".png"))
for i in range(10):
    hammerSwordAttackLeft.append(transform.flip(hammerSwordAttackRight[i],True,False))
    
for i in range(4):
    deerGrasing.append(image.load("Deer\\deerGrasing" + str(i+1) + ".png"))
large=[] #for scene 1
largeright=[] #for scene 1
for i in range(8):
    large.append(image.load("Large\\large" + str(i) + ".png"))
for i in range(8):
    largeright.append(transform.flip(large[i],True,False))
mainscreen=image.load("mainScreen\\mainscreen.png").convert_alpha()
newgame=image.load("mainScreen\\newgame.png").convert_alpha()
controls=image.load("mainScreen\\controls.png").convert_alpha()
creditss=image.load("mainScreen\\credits.png").convert_alpha()
largeidlel=image.load("Large/LargeIdleLeft.png")
largeidler=image.load("Large/LargeIdleRight.png")
creditscreen=image.load("mainScreen\\creditscreen.png").convert_alpha()
controlscreen=image.load("mainScreen\\controlscreen.png").convert_alpha()
death=image.load("Death.png").convert_alpha()
def mainScreen():
    global gameScreen
    newgameRect=Rect(666,403,480,111) #button 1
    controlsRect=Rect(682,563,445,101) #button 2
    creditssRect=Rect(742,720,331,97) #button 3

    if newgameRect.collidepoint(mx,my): 
        screen.blit(newgame,(0,0)) #screen blit
        if mb[0]==1:
            gameScreen="Scene" #start game
            mixer.music.stop()
            mixer.init() #music init
            mixer.music.load("Music\\music2.ogg") #load it
            mixer.music.play() #play song
    elif controlsRect.collidepoint(mx,my): 
        screen.blit(controls,(0,0))
        if mb[0]==1:
            gameScreen="Controls" #control game screen
    elif creditssRect.collidepoint(mx,my):
        screen.blit(creditss,(0,0)) #screen blit
        if mb[0]==1:
            gameScreen="Credits" #credit game screen
    else:
        screen.blit(mainscreen,(0,0)) #screen blit
def creditsscreen():
    global gameScreen
    screen.blit(creditscreen,(0,0)) #screen blit
    creditscreenrect=Rect(30,815,160,55) #back rect
    if creditscreenrect.collidepoint(mx,my): 
        if mb[0]==1:
            if gameScreen=="Credits": 
                gameScreen="Main" #game screen = main
def controlss():
    global gameScreen
    screen.blit(controlscreen,(0,0)) #screen blit
    creditscreenrect=Rect(30,815,160,55) #back button
    if creditscreenrect.collidepoint(mx,my):
        if mb[0]==1:
            if gameScreen=="Controls":
                gameScreen="Main"
def player():
    if playerHealth<=0:
        screen.blit(death,(0,0))
    for i in range(playerHealth):
        draw.rect(screen,BLACK,(15,825,100*2+10,35)) #health bar
        draw.rect(screen,GREEN,(20,830,i*2,25)) #health bar
    global frame,playerx,playery,move,playerMovement,points,direction
    if scene==1 or  scene==7:
        if playerMovement=="Walking":
            keys=key.get_pressed()
            if keys[K_d]:
                screen.blit(large[int(frame)],(playerx,playery))
                playerx+=5 #moves up 5
                frame += 0.19 #0.1.......0.9
                direction="Left"
            elif keys[K_a]:
                screen.blit(largeright[int(frame)],(playerx,playery))
                playerx-=5 #move back 5
                frame+=0.19 #frame up
                if direction=="Left":
                    direction="Right"
            if frame >= 8:#the last frame is 7 (0 - 7)
                frame = 0 #frame goes back to 0
        else:
            if direction=="Left": #direction
                screen.blit(largeidler,(playerx,playery)) #idle blit
            if direction=="Right": #direction
                screen.blit(largeidlel,(playerx,playery)) #idle blit
    if scene>=2 and scene<=6:
        if playerMovement=="Walking":
            keys=key.get_pressed()
            if keys[K_d]:
                screen.blit(playerForwardWalk[int(frame)],(playerx,playery))
                playerx+=5 #player goes 5 up
                frame += 0.19 #0.1.......0.9
            elif keys[K_a]:
                screen.blit(playerBackwardWalk[int(frame)],(playerx,playery))
                playerx-=5 #player goes 5 down
                frame+=0.19
            if frame >= 8:#the last frame is 7 (0 - 7)
                frame = 0 #frame goes to 0
        elif playerMovement=="Running":
            keys=key.get_pressed()
            if keys[K_d]:
                screen.blit(playerRun[int(frame)],(playerx,playery))
                playerx+=1
                frame += 0.3 #0.1.......0.9
            elif keys[K_a]:
                screen.blit(playerBackwardRun[int(frame)],(playerx,playery))
                playerx-=5
                frame += 0.3 #0.1.......0.9
            if frame >= 8:#the last frame is 7 (0 - 7)
                frame = 0
        elif playerMovement=="Idle":
            if direction=="Right":
                screen.blit(playerRightIdle0,(playerx,playery)) #screen blit
            elif direction=="Left":
                screen.blit(playerLeftIdle0,(playerx,playery)) #screen blit
        elif playerMovement=="Attack":
            if direction=="Right":
                if frame>=5:
                    frame=0
                screen.blit(playerAttackRight[int(frame)],(playerx,playery-50)) #screen blit
                frame+=0.1
                if frame>=5:
                    playerMovement="Idle"
                    attackpoints=0
                    frame=0
            if direction=="Left":
                if frame>=5:
                    frame=0
                screen.blit(playerAttackLeft[int(frame)],(playerx,playery-50)) #screen blit
                frame+=0.1
                if frame>=5:
                    playerMovement="Idle" #idle
                    attackpoints=0
                    frame=0
def Player_Movement():
    global playerx,playery
    keys=key.get_pressed()
def Player_Jump():
    global playerx,playery,VY,ONGROUND
    keys=key.get_pressed()
    if keys[K_SPACE] and ONGROUND:
        playery-=100
        ONGROUND=False
    playery+=VY
    if scene==1:
        if playery>=470:
            playery=470  #stay on the ground
            VY=0   #stop falling
            ONGROUND=True
    elif scene==3:
        if playery>=580:
            playery=580  #stay on the ground
            VY=0   #stop falling
            ONGROUND=True
    
    
    VY+=0.1    #apply gravity

computerRect=Rect(1415,360,385,406) #rect button
monitorRect=Rect(782,413,245,51) #rect button

def drawArrows(bull):
    global scene
    
    for b in bull:
        brect=Rect(b[0],b[1],10,10) #arrow rect
        if scene>=3 and scene<=5:
            if rightArrowCheck==False: #checker
                screen.blit(leftArrow,(b[0],b[1])) #blit
            elif rightArrowCheck==True: #checker
                screen.blit(rightArrow,(b[0],b[1])) #blit
        if scene==6:
            if rightArrowCheck==False: #checker
                screen.blit(leftFire,(b[0],b[1])) #blit
            elif rightArrowCheck==True: #checker
                screen.blit(rightArrow,(b[0],b[1])) #blit 
    display.flip()
def moveArrows(bull):
    global playerHealth
    for b in bull:
        if scene==3:
            if (-move+8500+magicArcherSpeed1-(playerx))>=0: #direction movement
                b[0]-=b[2]
                b[1]-=b[3]

            elif (-move+8500+magicArcherSpeed1-(playerx))<=0: #direction movement
                b[0]+=b[2]
                b[1]+=b[3]
        if scene==5:
            if (-move+8500+magicArcherSpeed1-(playerx))>=0: #direction movement
                b[0]-=b[2]
                b[1]-=b[3]

            elif (-move+8500+magicArcherSpeed1-(playerx))<=0: #direction movement
                b[0]+=b[2]
                b[1]+=b[3]
        if scene==6:
            if (-move+8500+magicArcherSpeed1-(playerx))>=0: #direction movement
                b[0]-=b[2]
                b[1]-=b[3]

            elif (-move+8500+magicArcherSpeed1-(playerx))<=0: #direction movement
                b[0]+=b[2]
                b[1]+=b[3]

        if playerRect.collidepoint(b[0],b[1]): #if the arrows hits the player
            playerHealth-=10 #remove the health
            bull.remove(b) #delete the arrow

def scene1():
    global scene,playerMovement,move
    keys=key.get_pressed()
    if keys[K_LSHIFT] and keys[K_d]: #button pressed
        playerMovement="Running"
        direction="Right"
    elif keys[K_d]: #button pressed
        playerMovement="Walking"
        direction="Right"
    elif keys[K_LSHIFT] and keys[K_a]: #button pressed
        playerMovement="Running"
        direction="Left"
    elif keys[K_a]: #button pressed
        playerMovement="Walking"
        direction="Left"
    elif playerMovement=="Attack": #button pressed
        attackpoint=1
    else: #no button pressed
        playerMovement="Idle"



            
    if move>=0 and move<=13185: #between theses moves
        if playerMovement=="Running": #player movement
            if keys[K_d]:
                move+=15
                direction="Right" #direction
            elif keys[K_a]:
                move-=15
                direction="Left"
        elif playerMovement=="Walking": #player movement
            if keys[K_d]:
                move+=5
                direction="Right" #direction
            if keys[K_a]:
                move-=5
                direction="Left"
    screen.blit(scene_one,(0,0)) #blit background
    global scene
    Player_Movement()
    player()
    if computerRect.collidepoint(playerx,playery): #if player goes to computer
        if scene==1:
            scene=2 #goes to scene 2
def scene2():
    global scene
    #globilizing every variable
    screen.blit(monitorScreen,(0,0)) #screen blit
    if monitorRect.collidepoint(mx,my): 
        screen.blit(monitorScreen2,(0,0)) #screen blit
        if mb[0]==1:
            if scene==2:
                scene=3
def scene3():#SCENE THREE
    global magicArcherHealth1,move,hellHoundHealth1,deerGrasingFrame,attackpoints,hellHoundHealth2,hellHoundHealth3,rapidAttackHellHound1,rapidAttackHellHound3,scene3TextBoxChecker,rapidAttackHellHound2,playerHealth,attackMagicArcher1,magicArcherHealth1,attackleft,attackHellHound1,attackHellHound2,hellHoundRect1,hellHoundRect2,rapidAttack,hellHoundFrame1,rightArrowCheck,hellHoundMovement1,hellHoundSpeed1,hellHoundDirection1,hellHoundFrame2,hellHoundMovement2,hellHoundSpeed2,hellHoundDirection2,rapid,playerx,playery,magicArcherSpeed1,playerMovement,direction,jeromeFrame,scene,magicArcherFrame,magicArcherMovement1,hellHoundFrame3,hellHoundMovement3,hellHoundSpeed3,hellHoundDirection3
    #Globalizing every variable
    
    keys=key.get_pressed()#Key Pressed
    Player_Movement()#Calling player movement 
    screen.blit(i3,(0,0))#Background layer One
    screen.blit(i2,(-move/3,0))#Background layer Two
    screen.blit(i1,(-move/2,0))#Background layer Three
    
    screen.blit(i0,(-move,0))#Moving the background layer 0

    #Player Movement
    if keys[K_LSHIFT] and keys[K_d]:#Player moving right
        playerMovement="Running"#Player sprite action
        direction="Right"#Player image direction
    elif keys[K_d]:
        playerMovement="Walking"#Player sprite action
        direction="Right"#Player image direction
    elif keys[K_LSHIFT] and keys[K_a]:#Player moving left
        playerMovement="Running"#Player sprite action
        direction="Left"#Player image direction
    elif keys[K_a]:
        playerMovement="Walking"#Player sprite action
        direction="Left"#Player image direction
    elif playerMovement=="Attack":#player Attack 
        attackpoint=1#Attcking point the player inflicts
    else:
        playerMovement="Idle"#Player sprite action
          
    if move>=0 and move<=13185:# making sure the player does not leave the screen and the screen does not go beyound its boundrys
        #This is all while the player is running
        if playerMovement=="Running":#Player sprite action
            if keys[K_d]:#Player moving right
                move+=15#add 15 pixels to players location resulting in movement
                direction="Right"#Player image direction
            elif keys[K_a]:
                move-=15#minus 15 pixels to players location resulting in movement
                direction="Left"#Player image direction
        #This is all while the player is walking
        elif playerMovement=="Walking":#Player sprite action
            if keys[K_d]:
                move+=5#add 15 pixels to players location resulting in movement
                direction="Right"#Player image direction
            if keys[K_a]:
                move-=5#minus 15 pixels to players location resulting in movement
                direction="Left"#Player image direction

    #Making sure player stays on the screen
    if move<0:#Making sure the player doesnt leave the screen through the left side
        move=0#Stays at x=0
    if move>13185 and scene==3:#Making sure the player doesnt leave the screen trhough the right
        move=13185#Keeping the player at x=12185
        
    if move<1945:#If player hits x=1945
        screen.blit(jeromeBackwardIdle[int(jeromeFrame)],(-move+1500,580))#blits jerome the NPC
        jeromeFrame += 0.1 #0.1.......0.9#Jeromes frames and sprite
        if jeromeFrame>=3:#Reseting Jeromes sprite 
            jeromeFrame=0
    screen.blit(wagon,(-move+1500,600))#Blitting Jeromes wagon
    #screen.blit(archer,(-move+2500,570))
    
    if magicArcherHealth1<=0:#If the magic archers health is 0 or lower than he dies
        magicArcherMovement1="Death"#Magic archer dies
    elif ((-move+8900+magicArcherSpeed1)-(playerx))<=800:#IF the magic archer and player are in a certain range
        magicArcherMovement1="Attack"#THe magic archer will attack and if the player leaves the range the magic archer will follow
    elif move>=7100:#The magic archer will follow
        magicArcherMovement1="Running"#magic archer running
        
    if magicArcherMovement1=="Running":#magic archer running
        if magicArcherFrame>=8:#reseting magic archers frames
            magicArcherFrame=0
        screen.blit(magicArcherBackwardRun[int(magicArcherFrame)],(-move+8500+magicArcherSpeed1,580))#blitting the magic archer
        magicArcherFrame+=0.2#increaseing the magic archer
        magicArcherSpeed1-=5#lowering the magic archers 
        if magicArcherFrame>=8:#reseting magic archer frames
            magicArcherFrame=0
    elif magicArcherMovement1=="Attack":#magic archer attack 
        if (-move+8500+magicArcherSpeed1-(playerx))>=0:#if teh magic archer is in a certain range of the player he will shoot his arrows
            rightArrowCheck=False
            screen.blit(magicArcherBackwardAttack[int(magicArcherFrame)],(-move+8500+magicArcherSpeed1,580))#blits the magic archers left sprites 
        elif (-move+8500+magicArcherSpeed1-(playerx))<=0:#if the magic archer is in a certain range of the player
            rightArrowCheck=True
            screen.blit(magicArcherForwardAttack[int(magicArcherFrame)],(-move+8500+magicArcherSpeed1,580))#magic archer right sprites 
        magicArcherFrame+=0.15#magic archer frames increasing
        if magicArcherFrame>=8.65 and magicArcherFrame<=8.75:#if the magic archer frames are at  certain point
            bullets.append([-move+8570+magicArcherSpeed1,647,v[0],v[1]])#he will shoot his arrows
        if magicArcherFrame>=15:#reseting the archers sprits
            magicArcherFrame=0
        if rapid<78:#makes sure the archer does not constantly attack and so he has to reset his attack
            rapid+=1
        if rapid==78:
            rapid=0
    elif magicArcherMovement1=="Death":#kills the magic archer sprites
        magicArcherFrame=0
        
    if hellHoundHealth1<=0:#If hellhound's health equals 0 then he dies 
        hellHoundMovement1="Death"#Stops the hellhounds all together 
    elif ((-move+4500+hellHoundSpeed1)-(playerx))<=30 and ((-move+4500+hellHoundSpeed1)-(playerx))>=-130:#If the hellhound is in the players radius than it attacks the player
        hellHoundMovement1="Attack"
    elif move>2600:#IF the player position is at x=2600
        hellHoundMovement1="Jump"#hell ound jump 
    if hellHoundMovement1=="Jump":#If the hell hound jumps
        if (-move+4500+hellHoundSpeed1)-(playerx)>=0:#If the hellhound is in the radius of the player
            screen.blit(hellHoundBackwardJump[int(hellHoundFrame1)],(-move+4500+hellHoundSpeed1,600))#blit hell hound attack
            hellHoundFrame1+=0.2#Hell hound sprite frames
            if hellHoundFrame1>=6:#If the hell hound frames hit the max whih is 6 than the frames reset
                hellHoundFrame1=0
            hellHoundSpeed1-=6#hellhound frames go back 6 frames 
            hellHoundDirection1="Left"#Hell hounds direction = LEFT
        #Same as the code above but instead of the jump action its the hell hound left action
        if (-move+4500+hellHoundSpeed1)-(playerx)<=0:
            screen.blit(hellHoundForwardJump[int(hellHoundFrame1)],(-move+4500+hellHoundSpeed1,600))
            hellHoundFrame1+=0.2
            if hellHoundFrame1>=6:# reseting the Frames
                hellHoundFrame1=0
            hellHoundSpeed1+=6#Adding 6 frames to the hellhound
            hellHoundDirection1="Right"#Hellhound direction right 
    if hellHoundMovement1=="Attack":#Hellhound Attck
        if rapidAttackHellHound1<50:#Hellhound constant attack
            rapidAttackHellHound1+=1#Plus one
        if hellHoundDirection1=="Left":#If hellhound is looking left 
            screen.blit(hellHoundBackwardAttack[int(hellHoundFrame1)],(-move+4500+hellHoundSpeed1,665))#Hell hound left attack sprit blit
            hellHoundFrame1+=0.1#Hell hound frames plus 0.1
            if rapidAttackHellHound1==50:#If hellhound hits the player
                playerHealth-=3#PLayer health minus equals 3
                rapidAttackHellHound1=0#hellhound attack resets
            if hellHoundFrame1>=6:#If hell hound frames it max(6)
                hellHoundFrame1=0#Hellhound frames reset to 0
            hellHoundSpeed1-=0
        elif hellHoundDirection1=="Right":#IF the hellhounds direction if looking right
            screen.blit(hellHoundForwardAttack[int(hellHoundFrame1)],(-move+4500+hellHoundSpeed1,665))#Blit the right sprite
            hellHoundFrame1+=0.1#Increase the frames by one 
            if rapidAttackHellHound1==50:#Hellhound attacks player
                playerHealth-=3#Subtract player health by 3
                rapidAttackHellHound1=0#Hello hound attack stops
            if hellHoundFrame1>=6:#Resets the hellhound frames when they hit the max (6)
                hellHoundFrame1=0
            hellHoundSpeed1-=0
    if hellHoundMovement1=="Death":#If the hellhound dies it stops the sprite and the animation
        hellHoundFrame1=0

    #THIS IS ALL THE SAME AS HELLHOUND ONE
    if hellHoundHealth2<=0:
        hellHoundMovement2="Death"
    elif ((-move+5500+hellHoundSpeed2)-(playerx))<=30 and ((-move+5500+hellHoundSpeed2)-(playerx))>=-130:
        hellHoundMovement2="Attack"
    elif move>2600:
        hellHoundMovement2="Run"
    if hellHoundMovement2=="Run":
        if (-move+5500+hellHoundSpeed2)-(playerx)>=0:
            if hellHoundFrame2>=5:
                hellHoundFrame2=0
            screen.blit(hellHoundBackwardRun[int(hellHoundFrame2)],(-move+5500+hellHoundSpeed2,630))
            hellHoundFrame2+=0.2
            if hellHoundFrame2>=5:
                hellHoundFrame2=0
            hellHoundSpeed2-=8
            hellHoundDirection2="Left"
        if (-move+5500+hellHoundSpeed2)-(playerx)<=0:
            if hellHoundFrame2>=5:
                hellHoundFrame2=0
            screen.blit(hellHoundForwardRun[int(hellHoundFrame2)],(-move+5500+hellHoundSpeed2,630))
            hellHoundFrame2+=0.2
            if hellHoundFrame2>=5:
                hellHoundFrame2=0
            hellHoundSpeed2+=8
            hellHoundDirection2="Right"
    if hellHoundMovement2=="Attack":
        if rapidAttackHellHound2<50:
            rapidAttackHellHound2+=1
        if hellHoundDirection2=="Left":
            screen.blit(hellHoundBackwardAttack[int(hellHoundFrame2)],(-move+5500+hellHoundSpeed2,665))
            hellHoundFrame2+=0.1
            if rapidAttackHellHound2==50:
                playerHealth-=3
                rapidAttackHellHound2=0
            if hellHoundFrame2>=6:
                hellHoundFrame2=0
            hellHoundSpeed2-=0
        elif hellHoundDirection1=="Right":
            screen.blit(hellHoundForwardAttack[int(hellHoundFrame2)],(-move+5500+hellHoundSpeed2,665))
            hellHoundFrame2+=0.1
            if rapidAttackHellHound2==50:
                playerHealth-=3
                rapidAttackHellHound2=0
            if hellHoundFrame2>=6:
                hellHoundFrame2=0
            hellHoundSpeed2-=0
    if hellHoundMovement2=="Death":
        hellHoundFrame2=0

    #DRAWS THE HELLHOUND ATTACK BARS AND BACKGROUNDS FOR THE HEALTH PLACERMENTS ABOVE THE HELLHOUNDS
    for i in range(hellHoundHealth1):
        draw.rect(screen,BLACK,((-move+4568+hellHoundSpeed1),588,102,15))#THe black boarder of the healthbar
        draw.rect(screen,GREEN,((-move+4570+hellHoundSpeed1),590,i,10))#The actual halth bar the deareases as you attack the hellhound
    #EVERYTHING IS THE SAME FOR HELLHOUND TWO
    for y in range(hellHoundHealth2):
        draw.rect(screen,BLACK,((-move+5568+hellHoundSpeed2),588,102,15))
        draw.rect(screen,GREEN,((-move+5570+hellHoundSpeed2),590,y,10))
        
    #DRAWS THE MAGIC ARCHERS HEALTHBAR ABOVE HIM
    #EVERYTHING WITH THE HEALTH IS AS SAME AS THE HELLHOUNDS
    for y in range(magicArcherHealth1):        
        draw.rect(screen,BLACK,((-move+8568+magicArcherSpeed1),558,102,15))
        draw.rect(screen,GREEN,((-move+8570+magicArcherSpeed1),560,y,10))
        
    #draw.rect(screen,GREEN,(playerx,playery,130,200),1)
    #draw.rect(screen,GREEN,(playerx-50,playery,130,200),1)

    #screen.blit(hellhound,(1000,660))

    #PLAYER ATTACK 
    if rapidAttack<40:#IF the player attack if less than 40
        rapidAttack+=1#increase it by one (this will reset when the player attacks so he cant rapidly attack all the time)
        
    #DRAWING ALL OBJECT RECTS FOR THIS SCENE
    playerAttackRightBoxRect=Rect(playerx,playery,130,200)
    playerAttackLeftBoxRect=Rect(playerx-50,playery,130,200)
    hellHoundRect=Rect(-move+4500+hellHoundSpeed1,665,200,100)
    hellHoundRect2=Rect(-move+5500+hellHoundSpeed2,665,200,100)
    magicArcherRect1=Rect(-move+8500+magicArcherSpeed1,580,180,200)
    #draw.rect(screen,GREEN,magicArcherRect1,1)
    player()#PLayer function
    Player_Jump()#player jump function
    
    if playerAttackRightBoxRect.colliderect(hellHoundRect) or playerAttackLeftBoxRect.colliderect(hellHoundRect):#CHEcks if the player is colliding wiht the hellhound from the left and right
        if attackHellHound1==False:#if the hellhound wasnt already attacking the player it will now
            attackHellHound1=True
    else:
        if attackHellHound1==True:#If the hellhound is attacking the player it will stop (Stops the hellhound from rapidly attacking)
            attackHellHound1=False
            
    #SAME AS THE FIRST HELL HOUND
    if playerAttackRightBoxRect.colliderect(hellHoundRect2) or playerAttackLeftBoxRect.colliderect(hellHoundRect2):
        if attackHellHound2==False:
            attackHellHound2=True
    else:
        if attackHellHound2==True:
            attackHellHound2=False
            
    #SAME AS THE HELLHOUNDS
    if playerAttackRightBoxRect.colliderect(magicArcherRect1) or playerAttackLeftBoxRect.colliderect(magicArcherRect1):
        if attackMagicArcher1==False:
            attackMagicArcher1=True
    else:
        if attackMagicArcher1==True:
            attackMagicArcher1=False
            
    #BLITTING JEROME AND HIS SPEECH        
    scene3JeromeRect=Rect(-move+1450,580,150,200)#Jeromes hit box
    if playerRect.colliderect(scene3JeromeRect):#if the player and Jerome are in each others radius
        screen.blit(ETalk,(40,30))#BLits the rect boxes
        if keys[K_e]:#if 'e' is pressed
            if scene3TextBoxChecker==False:#if you are not already in convo with jerome now you will be
                scene3TextBoxChecker=True
    if scene3TextBoxChecker==True:#When you start the convo with Jerome
        if scene3TextBoxNumber<14:#If the text boxes are less then 12
            screen.blit(scene3TextBox[scene3TextBoxNumber],(390,715))#Blitting the text boxes
    if move>=11510:#GOes to the next scene and resets all the assets 
        if scene==3:
            scene=4
            hellHoundHealth2=100
            hellHoundHealth1=100
            move=0
            magicArcherHealth1=100
            magicArcherMovement="Nothing"
            hellHoundMovement1="Idle"
            hellHoundMovement2="Idle"

    #Blitting the deers
    screen.blit(deerGrasing[int(deerGrasingFrame)],(-move+3000,600))
    screen.blit(deerGrasing[int(deerGrasingFrame)],(-move+7000,600))
    screen.blit(deerGrasing[int(deerGrasingFrame)],(-move+10000,600))
    deerGrasingFrame+=0.05#Animating the deers
    if deerGrasingFrame>4:
        deerGrasingFrame=0

    #screen.blit(jeromeName,(-move+1490,540))
    #Jeromes name and press 'e' instrunction
    jeromeNameRect=Rect(-move+1200,540,800,500)
    #draw.rect(screen,GREEN,jeromeNameRect,1)
    if playerRect.colliderect(jeromeNameRect):
        screen.blit(jeromeName,(-move+1490,540))

        

def scene4():
    global move,hammerSwordRight,hammerSwordFrame,attackHammerSword,scene4TextBoxChecker,scene,magicArcherHealth1,hellHoundHealth1,hellHoundHealth2,attackMagicArcher1,hammerSwordMovement,hammerSwordSpeed,playerMovement,playerHealth,direction,rapidAttack,hellHoundSpeed1,hellHoundMovement1,hellHoundFrame1,attackHellHound1,attackHellHound2,rapid,rapidAttackHellHound1,hellHoundDirection1,hellHoundSpeed2,hellHoundMovement2,hellHoundFrame2,rapidAttackHellHound2,hellHoundDirection2,magicArcherSpeed1,magicArcherMovement1,magicArcherFrame
    keys=key.get_pressed()
    Player_Movement()
    screen.blit(scene4Background3,(0,0))
    screen.blit(scene4Background2,(-move/3,0))
    #screen.blit(scene4Background1,(-move/2,0))
    screen.blit(scene4Background0,(-move/2,0))
    #Player Movement
    if keys[K_LSHIFT] and keys[K_d]:#Player moving right
        playerMovement="Running"#Player sprite action
        direction="Right"#Player image direction
    elif keys[K_d]:
        playerMovement="Walking"#Player sprite action
        direction="Right"#Player image direction
    elif keys[K_LSHIFT] and keys[K_a]:#Player moving left
        playerMovement="Running"#Player sprite action
        direction="Left"#Player image direction
    elif keys[K_a]:
        playerMovement="Walking"#Player sprite action
        direction="Left"#Player image direction
    elif playerMovement=="Attack":#player Attack 
        attackpoint=1#Attcking point the player inflicts
    else:
        playerMovement="Idle"#Player sprite action
    if move>=0 and move<=23185: #between move
        if playerMovement=="Running": #player movement
            if keys[K_d]:
                move+=17 #move 17 up
                direction="Right"
            elif keys[K_a]:
                move-=17 #move 17 back
                direction="Left"
        elif playerMovement=="Walking": #player movement
            if keys[K_d]:
                move+=5 #move 5 up
                direction="Right"
            if keys[K_a]:
                move-=5 #move 5 back
                direction="Left"
    #The player cannot leave the world
    if move<0: 
        move=0
    if move>23185:
        move=23185
    #simon, wagon, and well screen blits
    screen.blit(simonidle,(-move/2+1500,580))
    simonBoxRect=Rect(-move/2+1450,580,150,200) #simon hit box
    screen.blit(wagon2,(-move/2+1600,650))
    screen.blit(well,(-move/2+1000,536))
    player()


    if magicArcherHealth1<=0: #health less than 0
        magicArcherMovement1="Death" #movement
    elif ((-move/2+8900+magicArcherSpeed1)-(playerx))<=450: #the distance
        magicArcherMovement1="Attack" #movement
    elif move>=4500:
        magicArcherMovement1="Running" #movement
    if magicArcherMovement1=="Running":
        if magicArcherFrame>=8: #frame over 9
            magicArcherFrame=0 #frame to 0
        screen.blit(magicArcherBackwardRun[int(magicArcherFrame)],(-move/2+8500+magicArcherSpeed1,580)) #screen blit for script
        magicArcherFrame+=0.2 #MA frame
        magicArcherSpeed1-=5 #MA speed
        if magicArcherFrame>=8: #MA frame over 9
            magicArcherFrame=0 #MA frame to 0
    elif magicArcherMovement1=="Attack": #movement to attack
        if (-move/2+8500+magicArcherSpeed1-(playerx))>=0: #distance
            rightArrowCheck=False #left arrow
            screen.blit(magicArcherLeftSpin[int(magicArcherFrame)],(-move/2+8500+magicArcherSpeed1,580)) #arrow spinning
        elif (-move/2+8500+magicArcherSpeed1-(playerx))<=0: #distance
            rightArrowCheck=True #right arrow
            screen.blit(magicArcherRightSpin[int(magicArcherFrame)],(-move/2+8500+magicArcherSpeed1,580)) #arrow spinning
        magicArcherFrame+=0.15 #MA frame
        if magicArcherFrame>=7.55 and magicArcherFrame<=7.75: #if the frame is between these two
            playerHealth-=6 #player health minus 6
        if magicArcherFrame>=8: #frame it 8
            magicArcherFrame=0 #frame is 0
        #checking for rapid attack
        if rapid<78:
            rapid+=1
        if rapid==78:
            rapid=0
    elif magicArcherMovement1=="Death": #if the magic arhcer dies
        magicArcherFrame=0 #stop all frame, or frame is 0
        
    if hellHoundHealth1<=0: #if the hh health is 0
        hellHoundMovement1="Death" #movement
    elif ((-move/2+4500+hellHoundSpeed1)-(playerx))<=30 and ((-move/2+4500+hellHoundSpeed1)-(playerx))>=-130: #distance
        hellHoundMovement1="Attack" #movement
    elif move>4000: #if the move is 4000
        hellHoundMovement1="Jump" #movement
    if hellHoundMovement1=="Jump": #movement check
        if (-move/2+4500+hellHoundSpeed1)-(playerx)>=0: #distance
            screen.blit(hellHoundBackwardJump[int(hellHoundFrame1)],(-move/2+4500+hellHoundSpeed1,600)) #screen blit
            hellHoundFrame1+=0.2 #hh frame
            if hellHoundFrame1>=6: #if frame is over 6
                hellHoundFrame1=0 #hh frame to 0
            hellHoundSpeed1-=4 #hh speed goes back 
            hellHoundDirection1="Left" #direction
        if (-move/2+4500+hellHoundSpeed1)-(playerx)<=0: #distance
            screen.blit(hellHoundForwardJump[int(hellHoundFrame1)],(-move/2+4500+hellHoundSpeed1,600)) #screen blit
            hellHoundFrame1+=0.2 #hh frame
            if hellHoundFrame1>=6: #hh frame over 6
                hellHoundFrame1=0 #hh frame to 0
            hellHoundSpeed1+=4 #hh speed plus 4
            hellHoundDirection1="Right" #direction
    if hellHoundMovement1=="Attack": #movement
        if rapidAttackHellHound1<50: #checking rapid attack
            rapidAttackHellHound1+=1 #rapid attack increases by 1
        if hellHoundDirection1=="Left": #direction
            screen.blit(hellHoundBackwardAttack[int(hellHoundFrame1)],(-move/2+4500+hellHoundSpeed1,665)) #screen blit attack script
            hellHoundFrame1+=0.1 #hh frame
            if rapidAttackHellHound1==50: #rapid attack
                playerHealth-=3 #player health minus 3
                rapidAttackHellHound1=0 #rapid attack to 0
            if hellHoundFrame1>=6: #hh frame over 6
                hellHoundFrame1=0
            hellHoundSpeed1-=0
        elif hellHoundDirection1=="Right":
            screen.blit(hellHoundForwardAttack[int(hellHoundFrame1)],(-move/2+4500+hellHoundSpeed1,665))
            hellHoundFrame1+=0.1
            if rapidAttackHellHound1==50:
                playerHealth-=3
                rapidAttackHellHound1=0
            if hellHoundFrame1>=6:
                hellHoundFrame1=0
            hellHoundSpeed1-=0
    if hellHoundMovement1=="Death":
        hellHoundFrame1=0
#SAME AS ABOVE, JUST DIFFERENT SPEED AND ATTACK
    if hellHoundHealth2<=0:
        hellHoundMovement2="Death"
    elif ((-move/2+5500+hellHoundSpeed2)-(playerx))<=30 and ((-move/2+5500+hellHoundSpeed2)-(playerx))>=-130:
        hellHoundMovement2="Attack"
    elif move>2600:
        hellHoundMovement2="Run"
    if hellHoundMovement2=="Run":
        if (-move/2+5500+hellHoundSpeed2)-(playerx)>=0:
            if hellHoundFrame2>=5:
                hellHoundFrame2=0
            screen.blit(hellHoundBackwardRun[int(hellHoundFrame2)],(-move/2+5500+hellHoundSpeed2,630))
            hellHoundFrame2+=0.2
            if hellHoundFrame2>=5:
                hellHoundFrame2=0
            hellHoundSpeed2-=8
            hellHoundDirection2="Left"
        if (-move/2+5500+hellHoundSpeed2)-(playerx)<=0:
            if hellHoundFrame2>=5:
                hellHoundFrame2=0
            screen.blit(hellHoundForwardRun[int(hellHoundFrame2)],(-move/2+5500+hellHoundSpeed2,630))
            hellHoundFrame2+=0.2
            if hellHoundFrame2>=5:
                hellHoundFrame2=0
            hellHoundSpeed2+=8
            hellHoundDirection2="Right"
    if hellHoundMovement2=="Attack":
        if rapidAttackHellHound2<50:
            rapidAttackHellHound2+=1
        if hellHoundDirection2=="Left":
            screen.blit(hellHoundBackwardAttack[int(hellHoundFrame2)],(-move/2+5500+hellHoundSpeed2,665))
            hellHoundFrame2+=0.1
            if rapidAttackHellHound2==50:
                playerHealth-=3
                rapidAttackHellHound2=0
            if hellHoundFrame2>=6:
                hellHoundFrame2=0
            hellHoundSpeed2-=0
        elif hellHoundDirection1=="Right":
            screen.blit(hellHoundForwardAttack[int(hellHoundFrame2)],(-move/2+5500+hellHoundSpeed2,665))
            hellHoundFrame2+=0.1
            if rapidAttackHellHound2==50:
                playerHealth-=3
                rapidAttackHellHound2=0
            if hellHoundFrame2>=6:
                hellHoundFrame2=0
            hellHoundSpeed2-=0
    if hellHoundMovement2=="Death":
        hellHoundFrame2=0

#PLAYER HEALTH BARS FOR HELL HOUND AND HAMMER SWORD, AND MAGIC ARCHER
    for i in range(hellHoundHealth1):
        draw.rect(screen,BLACK,((-move/2+4568+hellHoundSpeed1),588,102,15))
        draw.rect(screen,GREEN,((-move/2+4570+hellHoundSpeed1),590,i,10))
    for y in range(hellHoundHealth2):
        draw.rect(screen,BLACK,((-move/2+5568+hellHoundSpeed2),588,102,15))
        draw.rect(screen,GREEN,((-move/2+5570+hellHoundSpeed2),590,y,10))
    for y in range(magicArcherHealth1):
        draw.rect(screen,BLACK,((-move/2+8568+magicArcherSpeed1),558,102,15))
        draw.rect(screen,GREEN,((-move/2+8570+magicArcherSpeed1),560,y,10))
    for y in range(hammerSwordHealth):
        draw.rect(screen,BLACK,((-move/2+10068+hammerSwordSpeed),558,102,15))
        draw.rect(screen,GREEN,((-move/2+10070+hammerSwordSpeed),560,y,10))

    if rapidAttack<40: #checking for rapid attack
        rapidAttack+=1 #rapid attack
    #hit boxes for all entities
    playerAttackRightBoxRect=Rect(playerx,playery,130,200)
    playerAttackLeftBoxRect=Rect(playerx-50,playery,130,200)
    hellHoundRect=Rect(-move/2+4500+hellHoundSpeed1,665,200,100)
    hellHoundRect2=Rect(-move/2+5500+hellHoundSpeed2,665,200,100)
    magicArcherRect1=Rect(-move/2+8500+magicArcherSpeed1,580,180,200)
    hammerSwordRect=Rect(-move/2+9980+hammerSwordSpeed,580,200,210)

    if playerAttackRightBoxRect.colliderect(hellHoundRect) or playerAttackLeftBoxRect.colliderect(hellHoundRect): #if rect is collided
        if attackHellHound1==False:
            attackHellHound1=True
    else:
        if attackHellHound1==True:
            attackHellHound1=False
    if playerAttackRightBoxRect.colliderect(hellHoundRect2) or playerAttackLeftBoxRect.colliderect(hellHoundRect2):#if rect is collided
        if attackHellHound2==False:
            attackHellHound2=True
    else:
        if attackHellHound2==True:
            attackHellHound2=False
    if playerAttackRightBoxRect.colliderect(magicArcherRect1) or playerAttackLeftBoxRect.colliderect(magicArcherRect1):#if rect is collided
        if attackMagicArcher1==False:
            attackMagicArcher1=True
    else:
        if attackMagicArcher1==True:
            attackMagicArcher1=False
    if playerAttackRightBoxRect.colliderect(hammerSwordRect) and playerAttackLeftBoxRect.colliderect(hammerSwordRect):#if rect is collided
        if attackHammerSword==False:
            attackHammerSword=True
    else:
        if attackHammerSword==True:
            attackHammerSword=False


#MOST OF IT THE SAME AS STUFF ABOVE! IT'S ALL ABOUT MOVING SPRITES!
    if hammerSwordHealth<=0:
        hammerSwordMovement="Death"
    elif (-move/2+10000+hammerSwordSpeed)-(playerx)>=-200 and (-move/2+10000+hammerSwordSpeed)-(playerx)<=100: #distance
        hammerSwordMovement="SwordAttack" #sword attack
    elif move>=15600: #if move is over 15600
        hammerSwordMovement="Walk" #movement goes to walk
    if hammerSwordMovement=="Walk":
        if (-move/2+10000+hammerSwordSpeed)-(playerx)>=100: #distance
            screen.blit(hammerSwordLeft[int(hammerSwordFrame)],(-move/2+10000+hammerSwordSpeed,580)) #screen blit
            hammerSwordFrame+=0.2 #hh frame
            hammerSwordSpeed-=4
            if hammerSwordFrame>=8:
                hammerSwordFrame=0
        elif (-move/2+10000+hammerSwordSpeed)-(playerx)<=-200:
            screen.blit(hammerSwordRight[int(hammerSwordFrame)],(-move/2+10000+hammerSwordSpeed,580))
            hammerSwordFrame+=0.2
            hammerSwordSpeed+=4
            if hammerSwordFrame>=8:
                hammerSwordFrame=0
    if hammerSwordMovement=="SwordAttack":
        if (-move/2+10000+hammerSwordSpeed)-(playerx)>=-200 and (-move/2+10000+hammerSwordSpeed)-(playerx)<=0:
            if hammerSwordFrame>=8:
                hammerSwordFrame=0 
            screen.blit(hammerSwordAttackRight[int(hammerSwordFrame)],(-move/2+10000+hammerSwordSpeed,580))
            hammerSwordFrame+=0.1
            hammerSwordSpeed+=0
            if hammerSwordFrame>=8:
                hammerSwordFrame=0
        if (-move/2+10000+hammerSwordSpeed)-(playerx)>=0 and (-move/2+10000+hammerSwordSpeed)-(playerx)<101:
            if hammerSwordFrame>=8:
                hammerSwordFrame=0 
            screen.blit(hammerSwordAttackLeft[int(hammerSwordFrame)],(-move/2+9950+hammerSwordSpeed,580))
            hammerSwordFrame+=0.1
            hammerSwordSpeed+=0
            if hammerSwordFrame>=8:
                hammerSwordFrame=0
        if hammerSwordFrame>=7.65 and hammerSwordFrame<=7.75:
            playerHealth-=5

    if playerRect.colliderect(simonBoxRect): #if collided
        screen.blit(ETalk,(40,30)) #text
        if keys[K_e]:
            if scene4TextBoxChecker==False:
                scene4TextBoxChecker=True
    if scene4TextBoxChecker==True: #checker
        if scene4TextBoxNumber<12: #chekcer
            screen.blit(scene4TextBox[scene4TextBoxNumber],(390,715))#screen blit for all text boxes
        if scene4TextBoxNumber==9:
            playerHealth=100
    if move>=20970:
        if scene==4:
            scene=5
            hellHoundHealth2=100
            hellHoundHealth1=100
            move=0
            playerHealth=100
            magicArcherHealth1=100
            magicArcherMovement="Nothing"
            hellHoundMovement1="Idle"
            hellHoundMovement2="Idle"

def scene5():
    global move,playerMovement,magicArcherHealth1,magicArcherHealth2,direction,magicArcherSpeed1,scene,magicArcherMovement1,attackMagicArcher1,attackMagicArcher2,attackMagicArcher2,attackHammerSword,hammerSwordFrame,hammerSwordHealth,hammerSwordSpeed,hammerSwordMovement,magicArcherFrame,magicArcherFrame2,rapid,rapidAttack,rightArrowCheck,magicArcherSpeed2,magicArcherMovement2,playerHealth
    #globizated all variables
    keys=key.get_pressed()
    Player_Movement()
    #background blitting
    screen.blit(scene5Background3,(0,0))
    screen.blit(scene5Background2,(-move/3,0))
    screen.blit(scene5Background1,(-move/2,0))
    screen.blit(scene5Background0,(-move,0))
    #SAME AS ABOVE
    if keys[K_LSHIFT] and keys[K_d]:
        playerMovement="Running"
        direction="Right"
    elif keys[K_d]:
        playerMovement="Walking"
        direction="Right"
    elif keys[K_LSHIFT] and keys[K_a]:
        playerMovement="Running"
        direction="Left"
    elif keys[K_a]:
        playerMovement="Walking"
        direction="Left"
    elif playerMovement=="Attack":
        attackpoint=1
    else:
        playerMovement="Idle"
    if move>=0 and move<=23185:
        if playerMovement=="Running":
            if keys[K_d]:
                move+=17
                direction="Right"
            elif keys[K_a]:
                move-=17
                direction="Left"
        elif playerMovement=="Walking":
            if keys[K_d]:
                move+=5
                direction="Right"
            if keys[K_a]:
                move-=5
                direction="Left"
    if move<0:
        move=0
    if move>23185:
        move=23185
    player()

    #SAME MAGIC ARHCER FOR SCENE 3
    if magicArcherHealth1<=0:
        magicArcherMovement1="Death"
    elif ((-move+8900+magicArcherSpeed1)-(playerx))<=800:
        magicArcherMovement1="Attack"
    elif move>=7100:
        magicArcherMovement1="Running"
    if magicArcherMovement1=="Running":
        if magicArcherFrame>=8:
            magicArcherFrame=0
        screen.blit(magicArcherBackwardRun[int(magicArcherFrame)],(-move+8500+magicArcherSpeed1,580))
        magicArcherFrame+=0.2
        magicArcherSpeed1-=5
        if magicArcherFrame>=8:
            magicArcherFrame=0
    elif magicArcherMovement1=="Attack":
        if (-move+8500+magicArcherSpeed1-(playerx))>=0:
            rightArrowCheck=False
            screen.blit(magicArcherBackwardAttack[int(magicArcherFrame)],(-move+8500+magicArcherSpeed1,580))
        elif (-move+8500+magicArcherSpeed1-(playerx))<=0:
            rightArrowCheck=True
            screen.blit(magicArcherForwardAttack[int(magicArcherFrame)],(-move+8500+magicArcherSpeed1,580))
        magicArcherFrame+=0.15
        if magicArcherFrame>=8.65 and magicArcherFrame<=8.75:
            bullets.append([-move+8570+magicArcherSpeed1,647,v[0],v[1]])
        if magicArcherFrame>=15:
            magicArcherFrame=0
        if rapid<78:
            rapid+=1
        if rapid==78:
            rapid=0
    elif magicArcherMovement1=="Death":
        magicArcherFrame=0

    if magicArcherHealth2<=0:
        magicArcherMovement2="Death"
    elif ((-move+9100+magicArcherSpeed2)-(playerx))<=75:
        magicArcherMovement2="Attack"
    elif move>=4500:
        magicArcherMovement2="Running"
    if magicArcherMovement2=="Running":
        if magicArcherFrame2>=8:
            magicArcherFrame2=0
        screen.blit(magicArcherBackwardRun[int(magicArcherFrame2)],(-move+9100+magicArcherSpeed2,580))
        magicArcherFrame2+=0.2
        magicArcherSpeed2-=5
        if magicArcherFrame2>=8:
            magicArcherFrame2=0
    elif magicArcherMovement2=="Attack":
        if (-move+9100+magicArcherSpeed2-(playerx))>=-171:
            rightArrowCheck=False
            screen.blit(magicArcherLeftSpin[int(magicArcherFrame2)],(-move+9100+magicArcherSpeed2,580))
        elif (-move+9100+magicArcherSpeed2-(playerx))<=80:
            rightArrowCheck=True
            screen.blit(magicArcherRightSpin[int(magicArcherFrame2)],(-move+9100+magicArcherSpeed2,580))
        magicArcherFrame2+=0.15
        if magicArcherFrame2>=7.55 and magicArcherFrame2<=7.75:
            playerHealth-=3
        if magicArcherFrame2>=8:
            magicArcherFrame2=0
        if rapid<78:
            rapid+=1
        if rapid==78:
            rapid=0
    elif magicArcherMovement2=="Death":
        magicArcherFrame2=0
    #SAME AS SCENE 4
    if hammerSwordHealth<=0:
        hammerSwordMovement="Death"
    elif (-move/2+9300+hammerSwordSpeed)-(playerx)>=-200 and (-move+9300+hammerSwordSpeed)-(playerx)<=120:
        hammerSwordMovement="SwordAttack"
    elif move>=15600:
        hammerSwordMovement="Walk"
    else:
        hammerSwordMovement="Walk"
    if hammerSwordMovement=="Walk":
        #print((-move/2+10000+hammerSwordSpeed)-(playerx))
        if (-move+9300+hammerSwordSpeed)-(playerx)>=121:
            screen.blit(hammerSwordLeft[int(hammerSwordFrame)],(-move+9300+hammerSwordSpeed,580))
            hammerSwordFrame+=0.2
            hammerSwordSpeed-=4
            if hammerSwordFrame>=8:
                hammerSwordFrame=0
        elif (-move+9300+hammerSwordSpeed)-(playerx)<=-200:
            screen.blit(hammerSwordRight[int(hammerSwordFrame)],(-move+9300+hammerSwordSpeed,580))
            hammerSwordFrame+=0.2
            hammerSwordSpeed+=4
            if hammerSwordFrame>=8:
                hammerSwordFrame=0
    if hammerSwordMovement=="SwordAttack":
        #print(move,(-move/2+10000+hammerSwordSpeed)-(playerx))
        if (-move+9300+hammerSwordSpeed)-(playerx)>=-1200 and (-move+9300+hammerSwordSpeed)-(playerx)<=0:
            if hammerSwordFrame>=8:
                hammerSwordFrame=0 
            screen.blit(hammerSwordAttackRight[int(hammerSwordFrame)],(-move+9300+hammerSwordSpeed,580))
            hammerSwordFrame+=0.1
            hammerSwordSpeed+=0
            if hammerSwordFrame>=8:
                hammerSwordFrame=0
        if (-move+9300+hammerSwordSpeed)-(playerx)>=0 and (-move+9300+hammerSwordSpeed)-(playerx)<120:
            if hammerSwordFrame>=8:
                hammerSwordFrame=0 
            screen.blit(hammerSwordAttackLeft[int(hammerSwordFrame)],(-move+9250+hammerSwordSpeed,580))
            hammerSwordFrame+=0.1
            hammerSwordSpeed+=0
            if hammerSwordFrame>=8:
                hammerSwordFrame=0
        else:
            hammerSwordMovement="Walk"
        if hammerSwordFrame>=7.65 and hammerSwordFrame<=7.75:
            playerHealth-=2
    #HIT BOXES FOR ALL ENTITIES
    playerAttackRightBoxRect=Rect(playerx,playery,130,200)
    playerAttackLeftBoxRect=Rect(playerx-50,playery,130,200)
    magicArcherRect1=Rect(-move+8500+magicArcherSpeed1,580,180,200)
    magicArcherRect2=Rect(-move+9100+magicArcherSpeed2,580,180,200)
    hammerSwordRect=Rect(-move+9300+hammerSwordSpeed,580,200,210)

    #HEALTH BARS FOR ALL ENTITIES
    for y in range(magicArcherHealth1):
        draw.rect(screen,BLACK,((-move+8568+magicArcherSpeed1),558,102,15))
        draw.rect(screen,GREEN,((-move+8570+magicArcherSpeed1),560,y,10))
    for y in range(magicArcherHealth2):
        draw.rect(screen,BLACK,((-move+9168+magicArcherSpeed2),558,102,15))
        draw.rect(screen,GREEN,((-move+9170+magicArcherSpeed2),560,y,10))
    for y in range(hammerSwordHealth):
        draw.rect(screen,BLACK,((-move+9368+hammerSwordSpeed),558,102,15))
        draw.rect(screen,GREEN,((-move+9370+hammerSwordSpeed),560,y,10))

    #CHECKING IF THE PLAYER COLLIDES WITH ALL ENTITIES FOR ATTACKING
    if playerAttackRightBoxRect.colliderect(magicArcherRect1) or playerAttackLeftBoxRect.colliderect(magicArcherRect1):
        if attackMagicArcher1==False:
            attackMagicArcher1=True
    else:
        if attackMagicArcher1==True:
            attackMagicArcher1=False
    if playerAttackRightBoxRect.colliderect(magicArcherRect2) or playerAttackLeftBoxRect.colliderect(magicArcherRect2):
        if attackMagicArcher2==False:
            attackMagicArcher2=True
    else:
        if attackMagicArcher2==True:
            attackMagicArcher2=False
    if playerAttackRightBoxRect.colliderect(hammerSwordRect) and playerAttackLeftBoxRect.colliderect(hammerSwordRect):
        if attackHammerSword==False:
            attackHammerSword=True
    else:
        if attackHammerSword==True:
            attackHammerSword=False
            
    if rapidAttack<40:
        rapidAttack+=1

    if move>=9000:
        if scene==5:
            scene=6
            hellHoundHealth2=100
            hellHoundHealth1=100
            move=0
            magicArcherHealth1=100
            magicArcherHealth2=100
            magicArcherMovement="Nothing"
            hellHoundMovement1="Idle"
            hellHoundMovement2="Idle"
            checker=1
            hammerSwordHealth=100

def scene6():
    global move,playerMovement,direction,magicArcherSpeed1,magicArcherMovement1,magicArcherFrame,rapid,rapidAttack,rightArrowCheck,magicArcherSpeed2,magicArcherMovement2,playerHealth,scene,magicArcherHealth1,move,hellHoundHealth1,deerGrasingFrame,attackpoints,hellHoundHealth2,hellHoundHealth3,rapidAttackHellHound1,rapidAttackHellHound3,scene3TextBoxChecker,rapidAttackHellHound2,playerHealth,attackMagicArcher1,magicArcherHealth1,attackleft,attackHellHound1,attackHellHound2,hellHoundRect1,hellHoundRect2,rapidAttack,hellHoundFrame1,rightArrowCheck,hellHoundMovement1,hellHoundSpeed1,hellHoundDirection1,hellHoundFrame2,hellHoundMovement2,hellHoundSpeed2,hellHoundDirection2,rapid,playerx,playery,magicArcherSpeed1,playerMovement,direction,jeromeFrame,scene,magicArcherFrame,magicArcherMovement1,hellHoundFrame3,hellHoundMovement3,hellHoundSpeed3,hellHoundDirection3
    #Globalizing every variable

    player()
    keys=key.get_pressed()#Key Pressed
    Player_Movement()#Calling player movement 
    screen.blit(scene6Background,(-move,0))#Background layer One
    
    #Player Movement
    if keys[K_LSHIFT] and keys[K_d]:#Player moving right
        playerMovement="Running"#Player sprite action
        direction="Right"#Player image direction
    elif keys[K_d]:
        playerMovement="Walking"#Player sprite action
        direction="Right"#Player image direction
    elif keys[K_LSHIFT] and keys[K_a]:#Player moving left
        playerMovement="Running"#Player sprite action
        direction="Left"#Player image direction
    elif keys[K_a]:
        playerMovement="Walking"#Player sprite action
        direction="Left"#Player image direction
    elif playerMovement=="Attack":#player Attack 
        attackpoint=1#Attcking point the player inflicts
    else:
        playerMovement="Idle"#Player sprite action
          
    if move>=0 and move<=13185:# making sure the player does not leave the screen and the screen does not go beyound its boundrys
        #This is all while the player is running
        if playerMovement=="Running":#Player sprite action
            if keys[K_d]:#Player moving right
                move+=15#add 15 pixels to players location resulting in movement
                direction="Right"#Player image direction
            elif keys[K_a]:
                move-=15#minus 15 pixels to players location resulting in movement
                direction="Left"#Player image direction
        #This is all while the player is walking
        elif playerMovement=="Walking":#Player sprite action
            if keys[K_d]:
                move+=5#add 15 pixels to players location resulting in movement
                direction="Right"#Player image direction
            if keys[K_a]:
                move-=5#minus 15 pixels to players location resulting in movement
                direction="Left"#Player image direction

    #Making sure player stays on the screen
    if move<0:#Making sure the player doesnt leave the screen through the left side
        move=0#Stays at x=0
    if move>13185 and scene==3:#Making sure the player doesnt leave the screen trhough the right
        move=13185#Keeping the player at x=12185
        

    
    if magicArcherHealth1<=0:#If the magic archers health is 0 or lower than he dies
        magicArcherMovement1="Death"#Magic archer dies
    elif ((-move+8900+magicArcherSpeed1)-(playerx))<=800:#IF the magic archer and player are in a certain range
        magicArcherMovement1="Attack"#THe magic archer will attack and if the player leaves the range the magic archer will follow
    elif move>=7100:#The magic archer will follow
        magicArcherMovement1="Running"#magic archer running
        
    if magicArcherMovement1=="Running":#magic archer running
        if magicArcherFrame>=8:#reseting magic archers frames
            magicArcherFrame=0
        screen.blit(magicArcherBackwardRun[int(magicArcherFrame)],(-move+8500+magicArcherSpeed1,580))#blitting the magic archer
        magicArcherFrame+=0.2#increaseing the magic archer
        magicArcherSpeed1-=5#lowering the magic archers 
        if magicArcherFrame>=8:#reseting magic archer frames
            magicArcherFrame=0
    elif magicArcherMovement1=="Attack":#magic archer attack 
        if (-move+8500+magicArcherSpeed1-(playerx))>=0:#if teh magic archer is in a certain range of the player he will shoot his arrows
            rightArrowCheck=False
            screen.blit(magicArcherBackwardAttack[int(magicArcherFrame)],(-move+8500+magicArcherSpeed1,580))#blits the magic archers left sprites 
        elif (-move+8500+magicArcherSpeed1-(playerx))<=0:#if the magic archer is in a certain range of the player
            rightArrowCheck=True
            screen.blit(magicArcherForwardAttack[int(magicArcherFrame)],(-move+8500+magicArcherSpeed1,580))#magic archer right sprites 
        magicArcherFrame+=0.15#magic archer frames increasing
        if magicArcherFrame>=8.65 and magicArcherFrame<=8.75:#if the magic archer frames are at  certain point
            bullets.append([-move+8570+magicArcherSpeed1,647,v[0],v[1]])#he will shoot his arrows
        if magicArcherFrame>=15:#reseting the archers sprits
            magicArcherFrame=0
        if rapid<78:#makes sure the archer does not constantly attack and so he has to reset his attack
            rapid+=1
        if rapid==78:
            rapid=0
    elif magicArcherMovement1=="Death":#kills the magic archer sprites
        magicArcherFrame=0
        
    if hellHoundHealth1<=0:#If hellhound's health equals 0 then he dies 
        hellHoundMovement1="Death"#Stops the hellhounds all together 
    elif ((-move+4500+hellHoundSpeed1)-(playerx))<=30 and ((-move+4500+hellHoundSpeed1)-(playerx))>=-130:#If the hellhound is in the players radius than it attacks the player
        hellHoundMovement1="Attack"
    elif move>2600:#IF the player position is at x=2600
        hellHoundMovement1="Jump"#hell ound jump 
    if hellHoundMovement1=="Jump":#If the hell hound jumps
        if (-move+4500+hellHoundSpeed1)-(playerx)>=0:#If the hellhound is in the radius of the player
            screen.blit(hellHoundBackwardJump[int(hellHoundFrame1)],(-move+4500+hellHoundSpeed1,600))#blit hell hound attack
            hellHoundFrame1+=0.2#Hell hound sprite frames
            if hellHoundFrame1>=6:#If the hell hound frames hit the max whih is 6 than the frames reset
                hellHoundFrame1=0
            hellHoundSpeed1-=6#hellhound frames go back 6 frames 
            hellHoundDirection1="Left"#Hell hounds direction = LEFT
        #Same as the code above but instead of the jump action its the hell hound left action
        if (-move+4500+hellHoundSpeed1)-(playerx)<=0:
            screen.blit(hellHoundForwardJump[int(hellHoundFrame1)],(-move+4500+hellHoundSpeed1,600))
            hellHoundFrame1+=0.2
            if hellHoundFrame1>=6:# reseting the Frames
                hellHoundFrame1=0
            hellHoundSpeed1+=6#Adding 6 frames to the hellhound
            hellHoundDirection1="Right"#Hellhound direction right 
    if hellHoundMovement1=="Attack":#Hellhound Attck
        if rapidAttackHellHound1<50:#Hellhound constant attack
            rapidAttackHellHound1+=1#Plus one
        if hellHoundDirection1=="Left":#If hellhound is looking left 
            screen.blit(hellHoundBackwardAttack[int(hellHoundFrame1)],(-move+4500+hellHoundSpeed1,665))#Hell hound left attack sprit blit
            hellHoundFrame1+=0.1#Hell hound frames plus 0.1
            if rapidAttackHellHound1==50:#If hellhound hits the player
                playerHealth-=3#PLayer health minus equals 3
                rapidAttackHellHound1=0#hellhound attack resets
            if hellHoundFrame1>=6:#If hell hound frames it max(6)
                hellHoundFrame1=0#Hellhound frames reset to 0
            hellHoundSpeed1-=0
        elif hellHoundDirection1=="Right":#IF the hellhounds direction if looking right
            screen.blit(hellHoundForwardAttack[int(hellHoundFrame1)],(-move+4500+hellHoundSpeed1,665))#Blit the right sprite
            hellHoundFrame1+=0.1#Increase the frames by one 
            if rapidAttackHellHound1==50:#Hellhound attacks player
                playerHealth-=3#Subtract player health by 3
                rapidAttackHellHound1=0#Hello hound attack stops
            if hellHoundFrame1>=6:#Resets the hellhound frames when they hit the max (6)
                hellHoundFrame1=0
            hellHoundSpeed1-=0
    if hellHoundMovement1=="Death":#If the hellhound dies it stops the sprite and the animation
        hellHoundFrame1=0

    #THIS IS ALL THE SAME AS HELLHOUND ONE
    if hellHoundHealth2<=0:
        hellHoundMovement2="Death"
    elif ((-move+5500+hellHoundSpeed2)-(playerx))<=30 and ((-move+5500+hellHoundSpeed2)-(playerx))>=-130:
        hellHoundMovement2="Attack"
    elif move>2600:
        hellHoundMovement2="Run"
    if hellHoundMovement2=="Run":
        if (-move+5500+hellHoundSpeed2)-(playerx)>=0:
            if hellHoundFrame2>=5:
                hellHoundFrame2=0
            screen.blit(hellHoundBackwardRun[int(hellHoundFrame2)],(-move+5500+hellHoundSpeed2,630))
            hellHoundFrame2+=0.2
            if hellHoundFrame2>=5:
                hellHoundFrame2=0
            hellHoundSpeed2-=8
            hellHoundDirection2="Left"
        if (-move+5500+hellHoundSpeed2)-(playerx)<=0:
            if hellHoundFrame2>=5:
                hellHoundFrame2=0
            screen.blit(hellHoundForwardRun[int(hellHoundFrame2)],(-move+5500+hellHoundSpeed2,630))
            hellHoundFrame2+=0.2
            if hellHoundFrame2>=5:
                hellHoundFrame2=0
            hellHoundSpeed2+=8
            hellHoundDirection2="Right"
    if hellHoundMovement2=="Attack":
        if rapidAttackHellHound2<50:
            rapidAttackHellHound2+=1
        if hellHoundDirection2=="Left":
            screen.blit(hellHoundBackwardAttack[int(hellHoundFrame2)],(-move+5500+hellHoundSpeed2,665))
            hellHoundFrame2+=0.1
            if rapidAttackHellHound2==50:
                playerHealth-=3
                rapidAttackHellHound2=0
            if hellHoundFrame2>=6:
                hellHoundFrame2=0
            hellHoundSpeed2-=0
        elif hellHoundDirection1=="Right":
            screen.blit(hellHoundForwardAttack[int(hellHoundFrame2)],(-move+5500+hellHoundSpeed2,665))
            hellHoundFrame2+=0.1
            if rapidAttackHellHound2==50:
                playerHealth-=3
                rapidAttackHellHound2=0
            if hellHoundFrame2>=6:
                hellHoundFrame2=0
            hellHoundSpeed2-=0
    if hellHoundMovement2=="Death":
        hellHoundFrame2=0

    #DRAWS THE HELLHOUND ATTACK BARS AND BACKGROUNDS FOR THE HEALTH PLACERMENTS ABOVE THE HELLHOUNDS
    for i in range(hellHoundHealth1):
        draw.rect(screen,BLACK,((-move+4568+hellHoundSpeed1),588,102,15))#THe black boarder of the healthbar
        draw.rect(screen,GREEN,((-move+4570+hellHoundSpeed1),590,i,10))#The actual halth bar the deareases as you attack the hellhound
    #EVERYTHING IS THE SAME FOR HELLHOUND TWO
    for y in range(hellHoundHealth2):
        draw.rect(screen,BLACK,((-move+5568+hellHoundSpeed2),588,102,15))
        draw.rect(screen,GREEN,((-move+5570+hellHoundSpeed2),590,y,10))
        
    #DRAWS THE MAGIC ARCHERS HEALTHBAR ABOVE HIM
    #EVERYTHING WITH THE HEALTH IS AS SAME AS THE HELLHOUNDS
    for y in range(magicArcherHealth1):        
        draw.rect(screen,BLACK,((-move+8568+magicArcherSpeed1),558,102,15))
        draw.rect(screen,GREEN,((-move+8570+magicArcherSpeed1),560,y,10))
        
    #draw.rect(screen,GREEN,(playerx,playery,130,200),1)
    #draw.rect(screen,GREEN,(playerx-50,playery,130,200),1)

    #screen.blit(hellhound,(1000,660))

    #PLAYER ATTACK 
    if rapidAttack<40:#IF the player attack if less than 40
        rapidAttack+=1#increase it by one (this will reset when the player attacks so he cant rapidly attack all the time)
        
    #DRAWING ALL OBJECT RECTS FOR THIS SCENE
    playerAttackRightBoxRect=Rect(playerx,playery,130,200)
    playerAttackLeftBoxRect=Rect(playerx-50,playery,130,200)
    hellHoundRect=Rect(-move+4500+hellHoundSpeed1,665,200,100)
    hellHoundRect2=Rect(-move+5500+hellHoundSpeed2,665,200,100)
    magicArcherRect1=Rect(-move+8500+magicArcherSpeed1,580,180,200)
    #draw.rect(screen,GREEN,magicArcherRect1,1)
    player()#PLayer function
    Player_Jump()#player jump function
    
    if playerAttackRightBoxRect.colliderect(hellHoundRect) or playerAttackLeftBoxRect.colliderect(hellHoundRect):#CHEcks if the player is colliding wiht the hellhound from the left and right
        if attackHellHound1==False:#if the hellhound wasnt already attacking the player it will now
            attackHellHound1=True
    else:
        if attackHellHound1==True:#If the hellhound is attacking the player it will stop (Stops the hellhound from rapidly attacking)
            attackHellHound1=False
            
    #SAME AS THE FIRST HELL HOUND
    if playerAttackRightBoxRect.colliderect(hellHoundRect2) or playerAttackLeftBoxRect.colliderect(hellHoundRect2):
        if attackHellHound2==False:
            attackHellHound2=True
    else:
        if attackHellHound2==True:
            attackHellHound2=False
            
    #SAME AS THE HELLHOUNDS
    if playerAttackRightBoxRect.colliderect(magicArcherRect1) or playerAttackLeftBoxRect.colliderect(magicArcherRect1):
        if attackMagicArcher1==False:
            attackMagicArcher1=True
    else:
        if attackMagicArcher1==True:
            attackMagicArcher1=False

    if move>=11510:#GOes to the next scene and resets all the assets 
        if scene==6:
            scene=7
def scene7():
    global scene,playerMovement,move
    keys=key.get_pressed()
    if keys[K_LSHIFT] and keys[K_d]: #button pressed
        playerMovement="Running"
        direction="Right"
    elif keys[K_d]: #button pressed
        playerMovement="Walking"
        direction="Right"
    elif keys[K_LSHIFT] and keys[K_a]: #button pressed
        playerMovement="Running"
        direction="Left"
    elif keys[K_a]: #button pressed
        playerMovement="Walking"
        direction="Left"
    elif playerMovement=="Attack": #button pressed
        attackpoint=1
    else: #no button pressed
        playerMovement="Idle"



            
    if move>=0 and move<=13185: #between theses moves
        if playerMovement=="Running": #player movement
            if keys[K_d]:
                move+=15
                direction="Right" #direction
            elif keys[K_a]:
                move-=15
                direction="Left"
        elif playerMovement=="Walking": #player movement
            if keys[K_d]:
                move+=5
                direction="Right" #direction
            if keys[K_a]:
                move-=5
                direction="Left"
    screen.blit(scene_one,(0,0)) #blit background
    global scene
    Player_Movement()
    player() 


    
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            if scene==3:
                attackpoints=1
                playerMovement="Attack"
                #TEXT BOX CHECKING
                if scene3TextBoxChecker==True:
                    scene3TextBoxNumber+=1
                    if scene3TextBoxNumber>=14:
                        scene3TextBoxChecker=False
                #BASIC CHECKING IF THE HELL GOUND WAS ATTACKED OR NOT
                if attackHellHound1==True and hellHoundHealth1!=0 and rapidAttack==40:
                    hellHoundHealth1-=50
                    rapidAttack=0
                    attackHellHound1=False
                    playerMovement="Attack"
                if attackHellHound2==True and hellHoundHealth2!=0 and rapidAttack==40:
                    hellHoundHealth2-=50
                    rapidAttack=0
                    attackHellHound2=False
                if attackMagicArcher1==True and magicArcherHealth1!=0 and rapidAttack==40:
                    magicArcherHealth1-=15
                    rapidAttack=0
                    attackMagicArcher1=False
            if scene==4:
                playerMovement="Attack"
                #TEXT BOX CHECKING
                if scene4TextBoxChecker==True:
                    scene4TextBoxNumber+=1
                    if scene4TextBoxNumber>=12:
                        scene4TextBoxChecker=False
                #BASIC CHECKING IF THE HELL GOUND WAS ATTACKED OR NOT
                if attackHellHound1==True and hellHoundHealth1!=0 and rapidAttack==40:
                    hellHoundHealth1-=75
                    rapidAttack=0
                    attackHellHound1=False
                    playerMovement="Attack"
                if attackHellHound2==True and hellHoundHealth2!=0 and rapidAttack==40:
                    hellHoundHealth2-=75
                    rapidAttack=0
                    attackHellHound2=False
                if attackMagicArcher1==True and magicArcherHealth1!=0 and rapidAttack==40:
                    magicArcherHealth1-=15
                    rapidAttack=0
                    attackMagicArcher1=False
                if attackHammerSword==True and hammerSwordHealth!=0 and rapidAttack==40:
                    hammerSwordHealth-=15
                    rapidAttack=0
                    attackHammerSword=False
            if scene==5:
                playerMovement="Attack"
                #BASIC CHECKING IF THE HELL GOUND WAS ATTACKED OR NOT
                if attackMagicArcher1==True and magicArcherHealth1!=0 and rapidAttack==40:
                    magicArcherHealth1-=20
                    rapidAttack=0
                    attackMagicArcher1=False
                    playerMovement="Attack"
                if attackMagicArcher2==True and magicArcherHealth2!=0 and rapidAttack==40:
                    magicArcherHealth2-=20
                    rapidAttack=0
                    attackMagicArcher2=False
                    playerMovement="Attack"
                if attackHammerSword==True and hammerSwordHealth!=0 and rapidAttack==40:
                    hammerSwordHealth-=20
                    rapidAttack=0
                    attackHammerSword=False
                    playerMovement="Attack"
            if scene==6:
                attackpoints=1
                playerMovement="Attack"
                #BASIC CHECKING IF THE HELL GOUND WAS ATTACKED OR NOT
                if attackHellHound1==True and hellHoundHealth1!=0 and rapidAttack==40:
                    hellHoundHealth1-=50
                    rapidAttack=0
                    attackHellHound1=False
                    playerMovement="Attack"
                if attackHellHound2==True and hellHoundHealth2!=0 and rapidAttack==40:
                    hellHoundHealth2-=50
                    rapidAttack=0
                    attackHellHound2=False
                if attackMagicArcher1==True and magicArcherHealth1!=0 and rapidAttack==40:
                    magicArcherHealth1-=15
                    rapidAttack=0
                    attackMagicArcher1=False

                       
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
   
    clock.tick(70)
    #Calling Functions
    if gameScreen=="Main":
        mainScreen()
    elif gameScreen=="Credits":
        creditsscreen()
    elif gameScreen=="Controls":
        controlss()
    if gameScreen=="Scene":
        if scene==1:
            if checker==1:
                checker=2
                playerx=450
                playery=400
                playerH=200
                playerW=80
            scene1()
        elif scene==2:
            scene2()
        elif scene==3:
            playerx=450
            playery=580
            playerH=200
            playerW=80
            scene3()
            moveArrows(bullets)
            drawArrows(bullets)
        elif scene==4:
            playerx=450
            playery=580
            playerH=200
            playerW=80
            scene4()
        elif scene==5:
            playerx=450
            playery=580
            playerH=200
            playerW=80
            scene5()
            moveArrows(bullets)
            drawArrows(bullets)
        elif scene==6:
            playerx=450
            playery=580
            playerH=200
            playerW=80
            moveArrows(bullets)
            drawArrows(bullets)
            scene6()
            checker=1
        elif scene==7:
            if checker==1:
                checker=2
                playerx=450
                playery=400
                playerH=200
                playerW=80
            scene7()
            
    display.flip()
            
quit()
