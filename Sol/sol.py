from math import *
from graphics import *
from operator import *

#graph window initialisation
width, height = 400, 200
offset = 20
win = GraphWin('Graphics', width, height)
win.setCoords(-offset, -height/2, width-offset, height/2)
win.setBackground('White')
win2 = GraphWin('Graphics', width, height)
win2.setCoords(-offset, -height/2, width-offset, height/2)
win2.setBackground('White')


# --- constants, do not touch! ---
# 1 degree in radians:
degree = pi / 180
#Earth radius:
r0 = 6366
# Earth's distance from the Sun
dist = 150000000
# Earth's axis tilt angle
beta = 22.5 * degree

# --- variables, change as you like ---
# latitude
delta = 62 * degree
# Earth's axis direction == time of the year (0 NH WS / SH SS, 180 NH SS / SH WS)
sunAngle = 180 * degree


def calculateAngle(i, sunAngle, r, z0, sunX, sunY):
    pX = sin(i * degree) * r
    y = cos(i * degree) * r 
    
    if y == 0:
        tempAngle = pi / 2
    else:
        tempAngle = atan(z0/y)
        
    lineLen = sqrt(y * y + z0 * z0)
    if xor(xor(y < 0, z0 < 0), delta < 0):
        lineLen = -lineLen
    
    pY = cos(tempAngle + beta) * lineLen
    pZ = sin(tempAngle + beta) * lineLen

    dotProduct = pX * sunX + pY * sunY + pZ * 0
    
    angle = acos(dotProduct / (sqrt(pX*pX+pY*pY+pZ*pZ)*sqrt(sunX*sunX+sunY*sunY)))
    angle = angle * 180 / pi
    return angle

def main():
    drawLines(win)

    y0 = cos(delta) * r0
    z0 = sin(delta) * r0
    r = cos(delta) * r0
    sunX = sin(sunAngle) * dist
    sunY = cos(sunAngle) * dist

    day = sunAngle
    for i in range(0, 360):
        angle = calculateAngle(i, day, r, z0, sunX, sunY)
        anglePoint = Point(i, 90-angle)
        anglePoint.setOutline('lightblue')
        anglePoint.draw(win)

    drawLines(win2)
    for i in range(0,365):
        day = i * degree / 365 * 360
        y0 = cos(delta) * r0
        z0 = sin(delta) * r0
        r = cos(delta) * r0
        sunX = sin(day) * dist
        sunY = cos(day) * dist        
        
        sunX = sin(day) * dist
        sunY = cos(day) * dist
        angle = calculateAngle(180, day, r, z0, sunX, sunY)
        
        anglePoint = Point(i, 90-angle)
        anglePoint.setOutline('green')
        anglePoint.draw(win2)


#draw scale lines
def drawLines(window):
    xAxisLine = Line(Point(0,0),Point(360,0))
    xAxisLine.setOutline('gray')
    xAxisLine.draw(window)
    xAxisLine = Line(Point(0,45),Point(360,45))
    xAxisLine.setOutline('lightgray')
    xAxisLine.draw(window)
    xAxisLine = Line(Point(0,-45),Point(360,-45))
    xAxisLine.setOutline('lightgray')
    xAxisLine.draw(window)
    xAxisLine = Line(Point(0,90),Point(360,90))
    xAxisLine.setOutline('lightgray')
    xAxisLine.draw(window)
    xAxisLine = Line(Point(0,-90),Point(360,-90))
    xAxisLine.setOutline('lightgray')
    xAxisLine.draw(window)
    xAxisLine = Line(Point(90,-90),Point(90,90))
    xAxisLine.setOutline('lightgray')
    xAxisLine.draw(window)
    xAxisLine = Line(Point(180,-90),Point(180,90))
    xAxisLine.setOutline('lightgray')
    xAxisLine.draw(window)
    xAxisLine = Line(Point(270,-90),Point(270,90))
    xAxisLine.setOutline('lightgray')
    xAxisLine.draw(window)
    xAxisLine = Line(Point(0,-90),Point(0,90))
    xAxisLine.setOutline('lightgray')
    xAxisLine.draw(window)
    xAxisLine = Line(Point(360,-90),Point(360,90))
    xAxisLine.setOutline('lightgray')
    xAxisLine.draw(window)

main()
                   
##    pt = Point(x/20,y/20)
##    pt.setOutline('lightgreen')
##    pt.draw(win)
##    pt2 = Point(x/20,z/20)
##    pt2.setOutline('black')
##    pt2.draw(win)
##    pt3 = Point(y/20,z/20)
##    pt3.setOutline('red')
##    pt3.draw(win)

    
#turtle example:

#from turtle import *


#color('red', 'yellow')
#begin_fill()
#while True:
#    forward(200)
#    left(170)
#    if abs(pos()) < 1:
#        break
#end_fill()
#done()
    
# download graphics module and extract
# on command line:> python setup.py install
