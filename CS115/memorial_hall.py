#!/usr/local/bin/python3
'''
Author: Kelly Sovacool
Email: kellysovacool@uky.edu
Section: 006
Purpose: Draw a building in a graphics window.
Preconditions: None
Postconditions: A window with shapes that look kind of like Memorial Hall.
Date: 8 Feb. 2015
'''
from graphics import *

def main():
    win = GraphWin("Lab3", 700, 700)
    win.setBackground('deepskyblue')
    
    # Draws the pavement
    ground = Rectangle(Point(0,680), Point (702,702))
    ground.setFill('ivory3')
    ground.setOutline('ivory3')
    ground.draw(win)
    # Left side grassy area
    grass1 = Polygon(Point(224,680), Point(0,680), Point(0,685), Point(219,685))
    grass1.setFill('springgreen4')
    grass1.setOutline('ivory4')
    grass1.draw(win)
    # Right side grassy area
    grass2 = Polygon(Point(476,680), Point(702,680), Point(702,685), Point(481,685))
    grass2.setFill('springgreen4')
    grass2.setOutline('ivory4')
    grass2.draw(win)
    
    # Draws the brick parts of the building
    brickbase = Rectangle(Point(196,540), Point(504,680))
    brickbase.setFill('brown4')
    brickbase.setOutline('saddlebrown')
    brickbase.draw(win)
    bricktower = Rectangle(Point(280,484), Point(420,344))
    bricktower.setFill('brown4')
    bricktower.setOutline('saddlebrown')
    bricktower.draw(win)  
    bricktrim = Rectangle(Point(278,449), Point(422,445))
    bricktrim.setFill('ivory')
    bricktrim.setOutline('ivory4')
    bricktrim.draw(win)
    
    # Draws the left portion of the main roof
    triangle1 = Polygon(Point(182,540), Point(252,498), Point(252,540))
    triangle1.setFill('ivory3')
    triangle1.setOutline('ivory4')
    triangle1.draw(win)
    # Interior of triangle1
    triangle2 = Polygon(Point(196,536), Point(252,503), Point(252, 536))
    triangle2.setFill('ivory4')
    triangle2.setOutline('ivory4')
    triangle2.draw(win)
    # Draws the right portion of the main roof
    triangle3 = Polygon(Point(518,540), Point(448,498), Point(448,540))
    triangle3.setFill('ivory3')
    triangle3.setOutline('ivory4')
    triangle3.draw(win)
    # Interior of triangle3
    triangle4 = Polygon(Point(502,536), Point(448,503), Point(448,536))
    triangle4.setFill('ivory4')
    triangle4.setOutline('ivory4')
    triangle4.draw(win)
    
    # Draws the Parthenon-like roof part
    ceiling = Rectangle(Point(252,540), Point(448,498))
    ceiling.setFill('ivory')
    ceiling.setOutline('ivory3')
    ceiling.draw(win)
    # Big triangle in the middle
    triangle5 = Polygon(Point(238,498), Point(462,498), Point(350,442))
    triangle5.setFill('ivory3')
    triangle5.setOutline('ivory4')
    triangle5.draw(win)
    # Interior of triangle 5
    triangle6 = Polygon(Point(256,494), Point(350,449), Point(444,494))
    triangle6.setFill('ivory')
    triangle6.setOutline('ivory3')
    triangle6.draw(win)
    
    # Draws the stairs
    staircase = Polygon(Point(224,680,), Point(476,680), Point(448,652), Point(252,652))
    staircase.setFill('ivory3')
    staircase.setOutline('ivory4')
    staircase.draw(win)
    for x in range(0,26,4):
        steps = Line(Point(452+x,656+x), Point(249-x,656+x))
        steps.setFill('antiquewhite4')
        steps.setWidth(2)
        steps.draw(win)
    
    # Draws the door
    frame = Rectangle(Point(329,587), Point(371,652))
    frame.setFill('ivory3')
    frame.setOutline('ivory3')
    frame.draw(win)
    door = Rectangle(Point(329,652), Point(371,596))
    door.setFill('ivory3')
    door.setOutline('ivory4')
    door.draw(win)
    crack = Line(Point(350,652), Point(350,596))
    crack.setOutline('ivory4')
    crack.draw(win)
    for x in range(0,7,5):
        handle = Line(Point(x+348,622), Point(x+348,630))
        handle.setOutline('DarkGoldenrod4')
        handle.setWidth(2)
        handle.draw(win)
    
    # Draws the big pillars
    for x in range(0,192,34):
        bigpillar = Polygon(Point(x+251,652), Point(x+251,645), Point(x+258,645), Point(x+258,540), Point(x+251,540), Point(x+251,533), Point(x+279,533), Point(x+279,540), Point(x+272,540), Point(x+272,645), Point(x+279,645), Point(x+279,652))
        bigpillar.setFill('ivory')
        bigpillar.setOutline('ivory4')
        bigpillar.draw(win)
    
    # Draws 'MEMORIAL HALL'
    txt = Text(Point(350,520), 'MEMORIAL HALL')
    txt.setFill('antiquewhite4')
    txt.setFace('times roman')
    txt.draw(win)
    
    # Draws the clock
    clocktrim = Circle(Point(350,386),19)
    clocktrim.setFill('ivory3')
    clocktrim.setOutline('ivory3')
    clocktrim.draw(win)
    for x in range(0,50,22):
        clocksquare1 = Rectangle(Point(350,389), Point(328+x,383))
        clocksquare1.setFill('ivory2')
        clocksquare1.setOutline('ivory3')
        clocksquare1.draw(win)
    for x in range(0,50,22):
        clocksquare2 = Rectangle(Point(347,383), Point(353,364+x))
        clocksquare2.setFill('ivory2')
        clocksquare2.setOutline('ivory3')
        clocksquare2.draw(win)
    clockface = Circle(Point(350,386), 14)
    clockface.setFill('white')
    clockface.setOutline('ivory3')
    clockface.draw(win)
    clockminhand = Line(Point(350,386,), Point(350,375))
    clockminhand.draw(win)
    clockhourhand = Line(Point(350,386,), Point(356,379))
    clockhourhand.draw(win)
    
    # Draws the base of the white tower
    trapezoid = Polygon(Point(280,344), Point(273,337), Point(427,337), Point(420,344))
    trapezoid.setFill('white')
    trapezoid.setOutline('antiquewhite4')
    trapezoid.draw(win)
    mediumsquare = Polygon(Point(294,337), Point(406,337), Point(406,232), Point(294,232))
    mediumsquare.setFill('white')
    mediumsquare.setOutline('antiquewhite4')
    mediumsquare.draw(win)
    squaretop = Polygon(Point(287,232), Point(413,232), Point(413,225), Point(287,225))
    squaretop.setFill('white')
    squaretop.setOutline('antiquewhite4')
    squaretop.draw(win)
    squaretrim = Polygon(Point(292,242), Point(292,246), Point(408,246), Point(408,242))
    squaretrim.setFill('ivory3')
    squaretrim.setOutline('antiquewhite4')
    squaretrim.draw(win)
    
    # Draws the cylindrical piece
    cylinderbase = Polygon(Point(308,225), Point(392,225), Point(392,204),Point(385,197), Point(315,197), Point(308,204))
    cylinderbase.setFill('white')
    cylinderbase.setOutline('antiquewhite4')
    cylinderbase.draw(win)
    cylinderroom = Polygon(Point(315,197), Point(385,197), Point(385,141), Point(392,134), Point(308,134), Point(315,141))
    cylinderroom.setFill('white')
    cylinderroom.setOutline('antiquewhite4')
    cylinderroom.draw(win)
    cylindertop = Polygon(Point(308,134), Point(308,127), Point(392,127), Point(392,134))
    cylindertop.setFill('white')
    cylindertop.setOutline('antiquewhite4')
    cylindertop.draw(win)
    # Draws the windows
    for x in range(-20,23,21):
        windowtop = Circle(Point(x+350,150), 7)
        windowtop.setFill('skyblue')
        windowtop.setOutline('skyblue')
        windowtop.draw(win)
        windowbottom = Rectangle(Point(x+343,150), Point(x+357,193))
        windowbottom.setFill('skyblue')
        windowbottom.setOutline('skyblue')
        windowbottom.draw(win)
        # Draws the vertical window panes
        windowpanevert = Line(Point(x+350,193), Point(x+350,143))
        windowpanevert.setOutline('antiquewhite4')
        windowpanevert.draw(win)
    # Draws the horizontal window panes
    for x in range(0,-36,-7):
        windowpanehoriz = Line(Point(322,x+187), Point(380,x+187))
        windowpanehoriz.setOutline('white')
        windowpanehoriz.draw(win)
    
    # Draws the mini Parthenon thing
    miniparbase = Polygon(Point(322,337), Point(378,337), Point(378,316), Point(322,316))
    miniparbase.setFill('white')
    miniparbase.setOutline('antiquewhite4')
    miniparbase.draw(win)
    # Draws the mini Parthenon pillars
    for x in range(0,42,41):
        minipillar = Polygon(Point(x+322,316), Point(x+322,310), Point(x+326,310), Point(x+326,248), Point(x+322,248), Point(x+322,242), Point(x+337,242), Point(x+337,248), Point(x+333,248), Point(x+333,310), Point(x+337,310), Point(x+337,316))
        minipillar.setFill('white')
        minipillar.setOutline('antiquewhite4')
        minipillar.draw(win)
    miniceiling = Polygon(Point(322,232), Point(378,232), Point(378,242), Point(322,242))
    miniceiling.setFill('white')
    miniceiling.setOutline('antiquewhite4')
    miniceiling.draw(win)
    # Draws the mini triangles
    minitriangle1 = Polygon(Point(322,232), Point(378,232), Point(350,204))
    minitriangle1.setFill('ivory3')
    minitriangle1.setOutline('antiquewhite4')
    minitriangle1.draw(win)
    minitriangle2 = Polygon(Point(331,228), Point(369,228), Point(350,210))
    minitriangle2.setFill('white')
    minitriangle2.setOutline('antiquewhite4')
    minitriangle2.draw(win)
    # Draws the vent window
    venttop = Circle(Point(350,265), 10)
    venttop.setFill('ivory4')
    venttop.setOutline('ivory4')
    venttop.draw(win)
    ventbottom = Rectangle(Point(340,265), Point(360,316))
    ventbottom.setFill('ivory4')
    ventbottom.setOutline('ivory4')
    ventbottom.draw(win)
    # Draws the vent slats
    for x in range(0,60,3):
        slat = Line(Point(339,314-x), Point(361,314-x))
        slat.setOutline('white')
        slat.draw(win)
    
    # Draws the bell house
    bellbase = Polygon(Point(327,127), Point(373,127), Point(373,110), Point(327,110))
    bellbase.setFill('white')
    bellbase.setOutline('antiquewhite4')
    bellbase.draw(win)
    # Draws the dome
    dome = Circle(Point(350,70), 23)
    dome.setFill('aquamarine')
    dome.setOutline('antiquewhite4')
    dome.draw(win)
    # Makes the dome a semi-circle
    sky = Rectangle(Point(327,70,), Point(373,93))
    sky.setFill('deepskyblue')
    sky.setOutline('deepskyblue')
    sky.draw(win)
    # Draws the dome trim
    dometrim1 = Polygon(Point(324,68), Point(324,72), Point(376,72), Point(376,68))
    dometrim1.setFill('white')
    dometrim1.setOutline('antiquewhite4')
    dometrim1.draw(win)
    dometrim2 = Polygon(Point(327,72), Point(327,77), Point(372,77), Point(372,72))
    dometrim2.setFill('ivory3')
    dometrim2.setOutline('antiquewhite4')
    dometrim2.draw(win)
    # Draws the tiny pillars
    for x in range(0,33,16):
        tinypillar = Polygon(Point(x+327,110), Point(x+327,105), Point(x+330,105), Point(x+330,77), Point(x+327,77), Point(x+327,72), Point(x+340,72), Point(x+340,77), Point(x+337,77), Point(x+337,105), Point(x+340,105), Point(x+340,110))
        tinypillar.setFill('white')
        tinypillar.setOutline('antiquewhite4')
        tinypillar.draw(win)
    
    # Draws the lightning rod
    lightcirc = Circle(Point(350,44), 3)
    lightcirc.setFill('darkgoldenrod4')
    lightcirc.setOutline('darkgoldenrod4')
    lightcirc.draw(win)
    lighttri = Polygon(Point(347,44), Point(353,44), Point(350,37))
    lighttri.setFill('darkgoldenrod4')
    lighttri.setOutline('darkgoldenrod4')
    lighttri.draw(win)
    lightflat = Line(Point(347,38), Point(353,38))
    lightflat.setFill('darkgoldenrod4')
    lightflat.draw(win)
    lightrod = Line(Point(350,38), Point(350,20))
    lightrod.setFill('darkgoldenrod4')
    lightrod.draw(win)
        
    # Draws the sun's rays
    for x in range(0,149,49):
        ray = Line(Point(0,0), Point(x+0,200-x))
        ray.setOutline('yellow')
        ray.draw(win)   
    # Draws the sun
    sun = Circle(Point(0,0), 125)
    sun.setFill('yellow')
    sun.setOutline('yellow')
    sun.draw(win)
    # Draws the mouth
    mouth = Circle(Point(52,60), 25)
    mouth.setFill('pink')
    mouth.setOutline('red')
    mouth.draw(win)
    # Makes the mouth a semi-circle
    mouthsemi = Rectangle(Point(27,60), Point(77,35))
    mouthsemi.setFill('yellow')
    mouthsemi.setOutline('yellow')
    mouthsemi.draw(win)
    lip = Line(Point(27,60), Point(77,60))
    lip.setOutline('red')
    lip.draw(win)
    # Draws the eyes
    for x in range(0,36,35):
            eyes = Circle(Point(x+35,35), 10)
            eyes.setFill('white')
            eyes.draw(win)
    iris1 = Circle(Point(37,37), 3)
    iris1.setFill('black')
    iris1.draw(win)
    iris2 = Circle(Point(72,37), 3)
    iris2.setFill('black')
    iris2.draw(win)
    
    # Draws the speech bubble
    box = Rectangle(Point(155,20), Point(305,75))
    box.setFill('white')
    box.setOutline('white')
    box.draw(win)
    arrow = Polygon(Point(155,75), Point(155,55), Point(115,70))
    arrow.setFill('white')
    arrow.setOutline('white')
    arrow.draw(win)
    
    # Prompts the user to click the mouse to close the window
    clicktext = Text(Point(230,47), "Click to close this window")
    clicktext.draw(win)
    win.getMouse()
    win.close()
    
main()
