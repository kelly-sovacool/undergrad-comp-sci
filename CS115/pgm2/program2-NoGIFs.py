'''
Author: Kelly Sovacool
Email: kellysovacool@uky.edu
Section: 006
Purpose: Create a simple game of golf in a graphics window
Preconditions: Input via entry boxes in graphics window: number of swings, difficulty level, angle of swing, velocity of swing
Postconditions: Output in graphics window: hole location for each swing, final location of ball for each swing, whether the ball reached the hole for each swing, percent of shots that reached the hole
Date: 25 Feb. 2015
'''
from math import sin, pi, sqrt
from graphics import *
from random import randrange
def main():
    
    # 1. Create a graphics window
    win = GraphWin('Golf', 500, 500)
    win.setBackground('lightskyblue1')
    # 2. Display startup message, "Golf!!"
    startup = Text(Point(250,50), 'Golf!!')
    startup.setSize(25)
    startup.setFace('helvetica')
    startup.setStyle('bold')
    startup.setFill('dark green')
    startup.draw(win)
    # 3. Get user input for number of swings
    swings_txt = Text(Point(250, 90), "How many swings do you want to try?")
    swings_txt.setFill('blue')
    swings_txt.setSize(15)
    swings_txt.draw(win)
    swings_entry = Entry(Point(400, 90), 3)
    swings_entry.draw(win)
    # 4. Get user input for level of difficulty
    level_txt = Text(Point(250, 120), "Level of difficulty (smaller is harder)")
    level_txt.setFill('blue')
    level_txt.setSize(15)
    level_txt.draw(win)
    level_entry = Entry(Point(400, 120), 3)
    level_entry.draw(win)
    # 5. Wait for a click before continuing
    click_txt = Text(Point(250,160), '(Click to continue)')
    click_txt.setFill('DarkOrange2')
    click_txt.setSize(15)
    click_txt.draw(win)
    win.getMouse()
    # 6. Display "Ok, let's play!"
    play_txt = Text(Point(250, 160), "Ok, let's play!")
    play_txt.setFill('blue')
    play_txt.setSize(25)
    play_txt.draw(win)
    # 7. Wait for another click before continuing
    click_txt.move(0,50)
    win.getMouse()
    
    # 8. Draw a 'golf course' in graphics window
    click_txt.undraw()
    startup.undraw()
    swings_txt.undraw()
    swings_entry.undraw()
    level_txt.undraw()
    level_entry.undraw()
    play_txt.undraw()
    grass = Rectangle(Point(0,450), Point(502,502))
    grass.setFill('dark green')
    grass.setOutline('dark green')
    grass.draw(win)
    legs = Polygon(Point(12,470), Point(17,420), Point(33,420), Point(38,470), Point(33,470), Point(25,428), Point(17,470))
    legs.setFill('khaki')
    legs.draw(win)
    for x in range(0,22,21):
        shoes = Polygon(Point(x+12,470), Point(x+17,470), Point(x+20,472), Point(x+20,474), Point(x+12,474))
        shoes.setFill('sienna')
        shoes.draw(win)
    club_handle = Polygon(Point(25,423), Point(26,423), Point(33,475), Point(34,475))
    club_handle.setOutline('gray35')
    club_handle.draw(win)
    club_end = Polygon(Point(35,475), Point(35,477), Point(31,477), Point(31,475))
    club_end.setOutline('gray25')
    club_end.setFill('gray25')
    club_end.draw(win)
    torso = Polygon(Point(17,420), Point(33,420), Point(33,390), Point(17,390))
    torso.setFill('blue')
    torso.draw(win)
    sleeve1 = Polygon(Point(17,390), Point(16,398), Point(18,404), Point(22,401))
    sleeve1.setFill('white')
    sleeve1.draw(win)
    sleeve2 = Polygon(Point(34,390), Point(31,397), Point(34,405), Point(35,395))
    sleeve2.setFill('white')
    sleeve2.draw(win)
    arm1 = Polygon(Point(19,404), Point(20,398), Point(23,407), Point(26,416), Point(25,423), Point(22,413))
    arm1.setFill('bisque2')
    arm1.draw(win)
    arm2 = Polygon(Point(26,416), Point(27,423), Point(30,413), Point(33,404), Point(32,398), Point(29,407))
    arm2.setFill('bisque2')
    arm2.draw(win)
    head = Oval(Point(20,393), Point(30,375))
    head.setFill('bisque2')
    head.draw(win)
    hat = Polygon(Point(20,380), Point(20,375), Point(30, 375), Point(30,378), Point(32,378), Point(32,380))
    hat.setFill('white')
    hat.draw(win)
    difficulty = level_entry.getText()
    difficulty_txt = Text(Point(55,20), 'Difficulty: ' + difficulty)
    difficulty_txt.setFill('dark green')
    difficulty_txt.setSize(14)
    difficulty_txt.draw(win)
    
    # 9. Initialize accumulator for shots that reached the hole
    shots_made = 0
    # 10. Initialize accumulator for swing count
    swing_count = 1
    # 11. Begin loop; the number of iterations equals the number of swings
    swings_total = int(swings_entry.getText())
    for i in range(swings_total):
        # 12. Display swing number        
        swing_count = str(swing_count)
        swing_txt = Text(Point(250,20), 'Swing #' + swing_count)
        swing_txt.setFill('blue')
        swing_txt.setSize(20)
        swing_txt.draw(win)
        # 13. Generate random number for hole location
        hole_loc = randrange(250,470)
        str_hole_loc = str(hole_loc)
        
        # 14. Draw oval for hole in graphics window
        hole = Oval(Point(hole_loc - 5, 473), Point(hole_loc + 5, 477))
        hole.setFill('black')
        hole.setOutline('gray')
        hole.draw(win)
        flagpole = Line(Point(hole_loc,475), Point(hole_loc, 398))
        flagpole.setFill('gray40')
        flagpole.setWidth(2)
        flagpole.draw(win)
        flag = Polygon(Point(hole_loc - 1, 400), Point(hole_loc - 1, 415), Point(hole_loc - 13, 407))
        flag.setFill('orange')
        flag.setOutline('gray40')
        flag.draw(win)
        ball = Circle(Point(38,475), 2)
        ball.setFill('white')
        ball.draw(win)        
        ref_line = Line(Point(38,485), Point(hole_loc, 485))
        ref_line.setFill('white')
        ref_line.draw(win) # for user's reference of the distance
        ref_ball = Text(Point(38,495), '38')
        ref_ball.setFill('white')
        ref_ball.draw(win)
        ref_hole = Text(Point(hole_loc, 495), str_hole_loc)
        ref_hole.setFill('white')
        ref_hole.draw(win)
        
        # 15. Display hole location
        location_txt = Text(Point(250, 60), 'Hole location: ' + str_hole_loc)
        location_txt.setSize(15)
        location_txt.setStyle('bold')
        location_txt.setFill('dark green')
        location_txt.draw(win)  
        
        # 16. Get user input for angle in degrees
        angle_txt = Text(Point(220,100), 'Angle in degrees')
        angle_txt.setFill('blue')
        angle_txt.setSize(15)
        angle_txt.draw(win)
        angle_entry = Entry(Point(300, 100), 3)
        angle_entry.draw(win)
        # 17. Get user input for velocity
        veloc_txt = Text(Point(230,130), 'Initial velocity')
        veloc_txt.setFill('blue')
        veloc_txt.setSize(15)
        veloc_txt.draw(win)
        veloc_entry = Entry(Point(300, 130), 3)
        veloc_entry.draw(win)
        # 18. Wait for a click before continuing
        click_txt.draw(win)
        win.getMouse()
        click_txt.undraw()
        veloc_val = float(veloc_entry.getText())
        angle_deg = float(angle_entry.getText())
        
        # 19. Convert angle from degrees to radians
        angle_rad = angle_deg * pi / 180
        # 20. Calculate the distance traveled by the ball
        gravity_con = 9.8
        ball_dist = veloc_val**2 * sin(2 * angle_rad) / gravity_con
        # 21. Calculate the maximum height reached by the ball
        max_height = veloc_val**2 * (sin(angle_rad))**2 / (2 * gravity_con)
        ground_level = 475 # y-coord of the ball's starting place
        adj_max_height = ground_level - max_height # adjusted for inverted coord plane
        ball_start_loc = 38 # The x-coord of the ball's starting place
        ball_final_loc = ball_dist + ball_start_loc
        int_ball_final_loc = int(ball_final_loc) # range needs ints
            
        ball.undraw()    
        # 22. Draw trajectory of ball in graphics window
        for x in range(ball_start_loc, int_ball_final_loc + 1, 5):
            # models trajectory as a parabola
            trajectory_eqn = max_height / ((ball_final_loc - (ball_dist / 2 + ball_start_loc))**2) * (x - (ball_dist / 2 + ball_start_loc))**2 + adj_max_height
            ball_moving = Circle(Point(x, trajectory_eqn), 2)
            ball_moving.setFill('white')
            ball_moving.draw(win)
            ball_moving.undraw()
        ball_end = Circle(Point(ball_final_loc,475), 2)
        ball_end.setFill('white')
        ball_end.draw(win)
        # 23. Report the final location of the ball, rounded to 1 decimal place
        str_ball_final_loc = str(round(ball_final_loc, 1))
        ball_loc_txt = Text(Point(250,160), 'Ball travels to ' + str_ball_final_loc)
        ball_loc_txt.setFill('blue')
        ball_loc_txt.setSize(15)
        ball_loc_txt.draw(win)
        
        difficulty = float(difficulty)    
        # 24. If the difference between the final ball location and hole location is less than or equal to difficulty level:
        if abs(hole_loc - ball_final_loc) <= difficulty:
            # 25. Output "you made it!"
            report = Text(Point(250,185), 'You made it!')
            report.setStyle('bold')
            report.setFill('forest green')
            # 26. Add 1 to the accumulator for shots that made it
            shots_made += 1
        # 27. If the difference between the final ball location and hole location is greater than difficulty level
        else:
            # 28. Output "you missed"
            report = Text(Point(250,185), 'You missed')
            report.setStyle('bold')
            report.setFill('firebrick')
        report.setSize(20)
        report.draw(win)
        
        # 29. Add one to the swing count
        swing_count = int(swing_count)
        swing_count += 1
        # 30. Wait for user click before continuing
        click_txt.draw(win)
        win.getMouse()
        click_txt.undraw() # Resetting the course before the next hole
        hole.undraw()
        swing_txt.undraw()
        location_txt.undraw()
        ball_loc_txt.undraw()
        report.undraw()
        ball_end.undraw()
        ref_line.undraw()
        ref_ball.undraw()
        ref_hole.undraw()
        flagpole.undraw()
        flag.undraw()
    end_txt = Text(Point(250,350),'')   
    # 31. Calculate percentage of shots that reached the hole, rounded to 1 decimal place
    score = 100 * round(shots_made / swings_total, 1)
    if score >= 90:
        end_txt.setText("You're a pro!")
    elif score >= 80:
        end_txt.setText("Not bad.")
    elif score >= 60:
        end_txt.setText("You could use some practice...")
    else:
        end_txt.setText("Go back to playing candy crush. Golf isn't for you.")
    end_txt.setFill('blue')
    end_txt.setSize(15)
    score = str(score)
    # 32. Report percentage of shots that reached the hole
    result_txt = Text(Point(250,250), 'You got ' + score + '%')
    result_txt.setSize(20)
    result_txt.setStyle('bold italic')
    result_txt.setFill('blue')
    end_txt.draw(win)
    result_txt.draw(win)
    # 33. Wait for a click before closing the window
    close_txt = Text(Point(250,300), '(Click to close this window)')
    close_txt.setFill('DarkOrange2')
    close_txt.setSize(20)
    close_txt.draw(win)
    win.getMouse()
    win.close()
main()