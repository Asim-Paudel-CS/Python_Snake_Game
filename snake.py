from asyncio.windows_events import NULL
from time import *
from asyncore import loop
from turtle import right
from graphics import *
from random import *

def Clear(wind):
    for item in wind.items[:]:
        item.undraw()
    wind.update()

def CreateWindow(enter_Width):
    global win
    winSize = enter_Width
    win = GraphWin("Snake Game",winSize,winSize)
    win.setBackground('black')

def CreatePoint(enter_X_Value,enter_Y_Value):
    global varCircle
    varPoint = Point(enter_X_Value,enter_Y_Value)
    varCircle = Circle(varPoint,5)
    varCircle.setFill('red')
    varCircle.draw(win)

def CreateRandomPoint(enter_X_Value,enter_Y_Value):
    global varRandomCircle
    varPoint = Point(enter_X_Value,enter_Y_Value)
    varRandomCircle = Circle(varPoint,5)
    varRandomCircle.setFill('yellow')
    varRandomCircle.draw(win)


def CreatePlayerTail(enter_X_Value,enter_Y_Value):
    varPoint = Point(enter_X_Value,enter_Y_Value)
    varTail.append(Circle(varPoint,3))
    varTail[snakeLen].setFill('yellow')
    varTail[snakeLen].draw(win)
    
def MovePoint():
    global snakeLen
    global varTail
    varTail = []
    snakeX,snakeY = list(),list()
    snakeLen = 0
    varKeyArrows = 'Right'
    pointPosX = 200
    pointPosY = 200
    CreatePoint(pointPosX,pointPosY)
    CreateRandomPoint(randint(3,win.getWidth()-3),randint(3,win.getHeight()-3))
    while True:
        headXprev = varCircle.getCenter().getX()
        headYprev = varCircle.getCenter().getY()
        varKey = win.checkKey()
        if varKey == 'Up' or varKey == 'Down' or varKey == 'Right' or varKey == 'Left':
            if varKeyArrows == 'Up' and varKey == 'Down':
                NULL
            elif varKeyArrows == 'Down' and varKey == 'Up':
                NULL
            elif varKeyArrows == 'Left' and varKey == 'Right':
                NULL
            elif varKeyArrows == 'Right' and varKey == 'Left':
                NULL
            else:
                varKeyArrows = varKey
        elif varKey == 'Escape':
            break
        else:
            NULL
        if varKeyArrows == 'Down' and varCircle.getCenter().getY() + varCircle.getRadius() < win.getHeight():
            varCircle.move(0,5)
        if varKeyArrows == 'Up' and varCircle.getCenter().getY() - varCircle.getRadius() > 0:
            varCircle.move(0,-5)
        if varKeyArrows == 'Left' and varCircle.getCenter().getX() - varCircle.getRadius() > 0:
            varCircle.move(-5,0)
        if varKeyArrows == 'Right' and varCircle.getCenter().getX() + varCircle.getRadius() < win.getWidth():
            varCircle.move(5,0)
        if CheckIntersectionRandomCirclePlayer():
            varRandomCircle.undraw()
            CreateRandomPoint(randint(3,win.getWidth()-3),randint(3,win.getHeight()-3))
            CreatePlayerTail(varCircle.getCenter().getX(),varCircle.getCenter().getY())
            snakeLen += 1
        if snakeLen == 1:
            varTail[0].move(headXprev-varTail[0].getCenter().getX(),headYprev-varTail[0].getCenter().getY())
        elif snakeLen >= 2:
            i = len(varTail) - 1
            varTail[i].move(headXprev-varTail[i].getCenter().getX(),headYprev-varTail[i].getCenter().getY())
            varTail.insert(0,varTail.pop(i))
        if CheckIntersectionSnakeItselfOrWall():
            print ("End")
            DisplayEndMessage()
            break
        sleep(0.03)

def DisplayEndMessage():
    Clear(win)
    global varCircle
    varPoint = Point(win.getWidth()/2,win.getHeight()/2)
    textPrint = "---GAME OVER---\n"+"Your Score is: "+str(snakeLen)+"\nPress Any Key to Exit\nPress R to retry"
    textVar = Text(varPoint,textPrint)
    textVar.setFill('red')
    textVar.draw(win)
    sleep(2)
    varKey = win.getKey()
    if varKey == 'r':
        win.close()
        Main()
    

def CheckIntersectionSnakeItselfOrWall():
    tolorance = 2
    playerUp = varCircle.getCenter().getY()-varCircle.getRadius()
    playerDown = varCircle.getCenter().getY()+varCircle.getRadius()
    playerLeft = varCircle.getCenter().getX()-varCircle.getRadius()
    playerRight = varCircle.getCenter().getX()+varCircle.getRadius()
    if playerUp <= 0 or playerLeft <=0 or playerDown >= win.getHeight() or playerRight >= win.getWidth():
        return True
    if snakeLen >= 1:
        for i in range (0,len(varTail)-1):
            if abs(varCircle.getCenter().getX() - varTail[i].getCenter().getX()) <= tolorance and abs(varCircle.getCenter().getY() - varTail[i].getCenter().getY()) <= tolorance:
                return True
    return False


def CheckIntersectionRandomCirclePlayer():
    playerUp = varCircle.getCenter().getY()-varCircle.getRadius()
    playerDown = varCircle.getCenter().getY()+varCircle.getRadius()
    playerLeft = varCircle.getCenter().getX()-varCircle.getRadius()
    playerRight = varCircle.getCenter().getX()+varCircle.getRadius()
    randpointUp = varRandomCircle.getCenter().getY()-varRandomCircle.getRadius()
    randpointDown = varRandomCircle.getCenter().getY()+varRandomCircle.getRadius()
    randpointLeft = varRandomCircle.getCenter().getX()-varRandomCircle.getRadius()
    randpointRight = varRandomCircle.getCenter().getX()+varRandomCircle.getRadius()
    intersected = True
    if playerUp > randpointDown or playerDown < randpointUp or playerLeft > randpointRight or playerRight < randpointLeft:
        intersected = False
    return intersected
        

def Main():
    CreateWindow(400)   
    MovePoint()
    win.close()
Main()