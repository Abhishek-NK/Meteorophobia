try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import pygame
import random
import time

#colours
brownColour = "#8B4513"
greenColour = "#2E8B57"
skyBlueColour = "#87CEEB"
goldColour = "#DAA520"

# constants
CANVAS_DIMS = (800, 500)
STEP = 0
CANVAS_BACKGROUND = skyBlueColour
jumpLimit = 320
floor = 420
cordX = 30
cordY = floor

meteor = simplegui.load_image("http://i.cubeupload.com/0WcjLP.png")
meteor2 = simplegui.load_image("http://i.cubeupload.com/0WcjLP.png")
meteor3 = simplegui.load_image("http://i.cubeupload.com/0WcjLP.png")
meteorDims = (120, 120)
xMeteor = 100
xMeteor2 = 300
xMeteor3 = 600
yMeteor = -100
meteorSTEP = 0

MframeWidth = meteorDims[0]/1
MframeHeight = meteorDims[1]/1
MframeCentreX = MframeWidth/2
MframeCentreY = MframeHeight/2
MframeIndex = (0, 0)

img = simplegui.load_image("https://i.cubeupload.com/Q0GvDF.png")
imgDims = (64.0, 51.0)
angle = 0

frameWidth = imgDims[0]/4
frameHeight = imgDims[1]/3
frameCentreX = frameWidth/2
frameCentreY = frameHeight/2
frameIndex = (0, 0)

clock = pygame.time.Clock()
frameDuration = 60
xCoin = 400
yCoin = 420 #blaze
score = 0
highScore = 0
life = 3
endGame = False
startMessage = "FUCK YOU"
instruction1 = "FUCK THIS GAME"
instruction2 = "FUCK EVERYTHING"

right_pressed = False
left_pressed = False
up_pressed = False
down_pressed = False
space_pressed = False
testMenu = True



class collisions:
    def coinCollision(x1, x2): #coin, cordx
        if x2 > x1 - 20 and x2 < x1 + 20:
            return True

    def meteorCollision(x1, x2, y1, y2, xx2, xx3): #xMeteor, cordX, yMeteor, cordY
        if y2 < y1 + 70 and y2 > y1 - 70:
            if x2 < x1 + 70 and x2 > x1 - 70:
                return True

def play():
    global life
    global STEP
    global meteorSTEP
    global score
    global angle
    global startMessage
    global instruction1
    global instruction2

    STEP = 7
    meteorSTEP = 10
    startMessage = ""
    instruction1 = ""
    instruction2 = ""

def pause():
    global STEP
    global meteorSTEP

    STEP = 0
    meteorSTEP = 0


def resume():
    global STEP
    global meteorSTEP

    STEP = 7
    meteorSTEP = 10


def gameOver(x):
    if x <= 0:
        return True


def restart():
    global life
    global STEP
    global meteorSTEP
    global score
    global angle

    life = 3
    score = 0
    meteorSTEP = 10
    STEP = 7
    angle = 0


def draw(canvas):
    global img
    global frameIndex
    global cordX
    global cordY
    global xCoin
    global score
    global xMeteor
    global yMeteor
    global angle
    global life
    global STEP
    global meteorSTEP
    global xMeteor2
    global xMeteor3
    global testMenu
    global startMessage
    global instruction1
    global instruction2
    global highScore
    time.sleep(1/30)


    canvas.draw_text(startMessage, (250, 100), 30, "black")
    canvas.draw_text(instruction1, (205, 150), 30, "black")
    canvas.draw_text(instruction2, (280, 200), 30, "black")
    canvas.draw_circle((xCoin, yCoin), 15, 3, 'gray', goldColour)

    canvas.draw_image(img,
                      (frameWidth * frameIndex[0] + frameCentreX,
                       frameHeight * frameIndex[1] + frameCentreY),
                      (frameWidth, frameHeight),
                      (cordX, cordY),
                      imgDims,
                      angle)

    canvas.draw_line((0, 480), (800, 480), 50, brownColour)
    canvas.draw_line((0, 450), (800, 450), 10, greenColour)
    canvas.draw_text("Score: " + str(score), (10, 25), 21, "white")
    canvas.draw_text("  |||  Lives: " + str(life), (80, 25), 21, "white")

    yMeteor += meteorSTEP
    canvas.draw_image(meteor,
                      (MframeWidth * MframeIndex[0] + MframeCentreX,
                       MframeHeight * MframeIndex[1] + MframeCentreY),
                      (MframeWidth, MframeHeight),
                      (xMeteor, yMeteor),
                      meteorDims,
                      angle)
    if yMeteor > floor:
        yMeteor = -100
        xMeteor = random.randint(0, 800)

    if score > 5:
        if meteorSTEP != 0:
            meteorSTEP = 15
            canvas.draw_image(meteor2,
                              (MframeWidth * MframeIndex[0] + MframeCentreX,
                               MframeHeight * MframeIndex[1] + MframeCentreY),
                              (MframeWidth, MframeHeight),
                              (xMeteor2, yMeteor),
                              meteorDims,
                              angle)
            if yMeteor == -100:
                xMeteor2 = random.randint(0, 800)

    if score > 10:
        if meteorSTEP != 0:
            meteorSTEP = 20
            canvas.draw_image(meteor3,
                              (MframeWidth * MframeIndex[0] + MframeCentreX,
                               MframeHeight * MframeIndex[1] + MframeCentreY),
                              (MframeWidth, MframeHeight),
                              (xMeteor3, yMeteor),
                              meteorDims,
                              angle)
            if yMeteor == -100:
                xMeteor3 = random.randint(0, 800)

    if right_pressed:
        if frameIndex != (1, 0):
            cordX += STEP
            frameIndex = (1, 0)

        else:
            frameIndex = list(frameIndex)
            frameIndex[1] = frameIndex[1] + 1
            frameIndex = tuple(frameIndex)
            cordX += STEP

    if left_pressed:
        if frameIndex != (3, 0):
            frameIndex = (3, 0)
            cordX -= STEP

        else:
            frameIndex = list(frameIndex)
            frameIndex[1] = frameIndex[1] + 1
            frameIndex = tuple(frameIndex)
            cordX -= STEP

    if up_pressed and cordY > (jumpLimit - 40) and cordY:
        if cordY > 320:
            frameIndex = (0, 2)
            cordY -= 27*0.9

    if cordY < floor:
        if cordY > 0:
            cordY += 10*1.1

    #this makes the player fall back down to the floor when jumped
    if cordY > floor:
        cordY = floor

    if down_pressed:
        frameIndex = [0, 0]

    if cordX > 801:
        cordX = 1

    if cordX < 0:
        cordX = 799

    if collisions.coinCollision(xCoin, cordX):
        xCoin = random.randint(0, 800)
        score += 1

    if collisions.meteorCollision(xMeteor, cordX, yMeteor, cordY, xMeteor2, xMeteor3):
        if life > 0:
            life -= 1
            yMeteor = -20
            xMeteor = random.randint(0, 800)

    if gameOver(life):
        frameIndex = [2, 1]
        angle = 300
        STEP = 0
        canvas.draw_text("GAME OVER", (200, 200), 30, "black")
        canvas.draw_text("Press 'restart' to play again", (200, 250), 30, "black")
        meteorSTEP = 0

        if score > highScore:
            highScore = score

        canvas.draw_text("Highscore: " + str(highScore), (200, 300), 30, "black")

    if space_pressed:
        if meteorSTEP == 0:
            resume()
        pause()

def keydown(key):
    global right_pressed
    global left_pressed
    global up_pressed
    global down_pressed
    global space_pressed

    if key == simplegui.KEY_MAP['right']:
        right_pressed = True
    elif key == simplegui.KEY_MAP['left']:
        left_pressed = True
    elif key == simplegui.KEY_MAP['up']:
        up_pressed = True
    elif key == simplegui.KEY_MAP['down']:
        down_pressed = True
    elif key == simplegui.KEY_MAP['p']:
        space_pressed = True

def keyup(key):
    global right_pressed
    global left_pressed
    global up_pressed
    global down_pressed
    global space_pressed

    if key == simplegui.KEY_MAP['right']:
        right_pressed = False
    elif key == simplegui.KEY_MAP['left']:
        left_pressed = False
    elif key == simplegui.KEY_MAP['up']:
        up_pressed = False
    elif key == simplegui.KEY_MAP['down']:
        down_pressed = False
    elif key == simplegui.KEY_MAP['p']:
        space_pressed = False


frame = simplegui.create_frame("Meteorophobia", CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background(CANVAS_BACKGROUND)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Play", play, 100)
frame.add_button("Pause", pause, 100)
frame.add_button("Resume", resume, 100)
frame.add_button("Restart", restart, 100)

# Start the frame animation
frame.start()


