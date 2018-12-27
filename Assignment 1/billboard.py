
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9967729
#    Student name: Andrew Ford
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  BILLBOARD
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "paste_up".
#  You are required to complete this function so that when the
#  program is run it produces an image of an advertising billboard
#  whose arrangement is determined by data stored in a list which
#  specifies how individual paper sheets are to be pasted onto the
#  backing.  See the instruction sheet accompanying this file for
#  full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

sheet_width = 200 # pixels
sheet_height = 500 # pixels
backing_margin = 20 # pixels
backing_width = sheet_width * 4 + backing_margin * 2
backing_height = sheet_height + backing_margin * 2
canvas_top_and_bottom_border = 150 # pixels
canvas_left_and_right_border = 300 # pixels
canvas_width = (backing_width + canvas_left_and_right_border)
canvas_height = (backing_height + canvas_top_and_bottom_border)

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# set up the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(mark_centre_points = True):

    # Set up the drawing canvas
    setup(canvas_width, canvas_height)

    # Draw as fast as possible
    tracer(False)

    # Colour the sky blue
    bgcolor('sky blue')

    # Draw the ground as a big green rectangle (sticking out of the
    # bottom edge of the drawing canvas slightly)
    overlap = 5 # pixels
    grass_height = 100 # pixels
    penup()
    goto(-(canvas_width // 2 + overlap),
         -(canvas_height // 2 + overlap)) # start at the bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_height + overlap)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_height + overlap)
    end_fill()

    # Draw a nice warm sun peeking into the image
    penup()
    goto(-canvas_width // 2, canvas_height // 2)
    color('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height // 3)
    color('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Draw the billboard's wooden backing as four frames
    # and some highlighted coordinates
    #
    # Outer rectangle
    goto(- backing_width // 2, - backing_height // 2) # bottom left
    pencolor('sienna'); fillcolor('tan'); width(3)
    begin_fill()
    pendown()
    setheading(90) # face north
    forward(backing_height)
    right(90) # face east
    forward(backing_width)
    right(90) # face south
    forward(backing_height)
    right(90) # face west
    forward(backing_width)
    end_fill()

    # Inner rectangle
    penup()
    goto(- backing_width // 2 + backing_margin,
         - backing_height // 2 + backing_margin) # bottom left
    fillcolor('gainsboro')
    begin_fill()
    pendown()
    setheading(90) # face north
    forward(backing_height - backing_margin * 2)
    right(90) # face east
    forward(backing_width - backing_margin * 2)
    right(90) # face south
    forward(backing_height - backing_margin * 2)
    right(90) # face west
    forward(backing_width - backing_margin * 2)
    end_fill()

    # Draw lines separating the locations where the sheets go
    width(1); pencolor('dim grey')
    for horizontal in [-sheet_width, 0, sheet_width]:
        penup()
        goto(horizontal, sheet_height // 2)
        pendown()
        setheading(270) # point south
        forward(sheet_height)
         
    # Mark the centre points of each sheet's location, if desired
    if mark_centre_points:
        penup()
        points = [[[round(-sheet_width * 1.5), 0], 'Location 1'],
                  [[round(-sheet_width * 0.5), 0], 'Location 2'],
                  [[round(sheet_width * 0.5), 0], 'Location 3'],
                  [[round(sheet_width * 1.5), 0], 'Location 4']]
        for centre_point, label in points:
            goto(centre_point)
            dot(4)
            write('  ' + label + '\n  (' + str(centre_point[0]) + ', 0)',
                  font = ('Arial', 12, 'normal'))
     
    # Reset everything ready for the student's solution
    color('black')
    width(1)
    penup()
    home()
    setheading(0)
    tracer(True)


# End the program by hiding the cursor and releasing the canvas
def release_drawing_canvas():
    tracer(True)
    hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data------------------------------------------------------#
#
# The list in this section contains the data sets you will use to
# test your code.  Each of the data sets is a list specifying the
# way in which sheets are pasted onto the billboard:
#
# 1. The name of the sheet, from 'Sheet A' to 'Sheet D'
# 2. The location to paste the sheet, from 'Location 1' to
#    'Location 4'
# 3. The sheet's orientation, either 'Upright' or 'Upside down'
#
# Each data set does not necessarily mention all four sheets.
#
# In addition there is an extra value, either 'X' or 'O' at the
# start of each data set.  The purpose of this value will be
# revealed only in Part B of the assignment.  You should ignore it
# while completing Part A.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#
# Note that your solution must work for all the data sets below
# AND ANY OTHER DATA SETS IN THE SAME FORMAT!
#

data_sets = [
    # These two initial data sets don't put any sheets on the billboard
    # Data sets 0 - 1
    ['O'],
    ['X'],
    # These data sets put Sheet A in all possible locations and orientations
    # Data sets 2 - 9
    ['O', ['Sheet A', 'Location 1', 'Upright']],
    ['O', ['Sheet A', 'Location 2', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright']],
    ['O', ['Sheet A', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 1', 'Upside down']],
    ['O', ['Sheet A', 'Location 2', 'Upside down']],
    ['O', ['Sheet A', 'Location 3', 'Upside down']],
    ['O', ['Sheet A', 'Location 4', 'Upside down']],
    # These data sets put Sheet B in all possible locations and orientations
    # Data sets 10 - 17
    ['O', ['Sheet B', 'Location 1', 'Upright']],
    ['O', ['Sheet B', 'Location 2', 'Upright']],
    ['O', ['Sheet B', 'Location 3', 'Upright']],
    ['O', ['Sheet B', 'Location 4', 'Upright']],
    ['O', ['Sheet B', 'Location 1', 'Upside down']],
    ['O', ['Sheet B', 'Location 2', 'Upside down']],
    ['O', ['Sheet B', 'Location 3', 'Upside down']],
    ['O', ['Sheet B', 'Location 4', 'Upside down']],
    # These data sets put Sheet C in all possible locations and orientations
    # Data sets 18 - 25
    ['O', ['Sheet C', 'Location 1', 'Upright']],
    ['O', ['Sheet C', 'Location 2', 'Upright']],
    ['O', ['Sheet C', 'Location 3', 'Upright']],
    ['O', ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down']],
    ['O', ['Sheet C', 'Location 2', 'Upside down']],
    ['O', ['Sheet C', 'Location 3', 'Upside down']],
    ['O', ['Sheet C', 'Location 4', 'Upside down']],
    # These data sets put Sheet D in all possible locations and orientations
    # Data sets 26 - 33
    ['O', ['Sheet D', 'Location 1', 'Upright']],
    ['O', ['Sheet D', 'Location 2', 'Upright']],
    ['O', ['Sheet D', 'Location 3', 'Upright']],
    ['O', ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet D', 'Location 1', 'Upside down']],
    ['O', ['Sheet D', 'Location 2', 'Upside down']],
    ['O', ['Sheet D', 'Location 3', 'Upside down']],
    ['O', ['Sheet D', 'Location 4', 'Upside down']],
    # These data sets place two sheets in various locations and orientations
    # Data sets 34 - 38
    ['O', ['Sheet D', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet B', 'Location 1', 'Upright']],
    ['O', ['Sheet D', 'Location 1', 'Upside down'],
          ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down']],
    ['X', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down']],
    # These data sets place three sheets in various locations and orientations
    # Data sets 39 - 43
    ['O', ['Sheet A', 'Location 4', 'Upright'],
          ['Sheet B', 'Location 3', 'Upright'],
          ['Sheet C', 'Location 2', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down'],
          ['Sheet D', 'Location 3', 'Upside down'],
          ['Sheet A', 'Location 4', 'Upright']], 
    ['O', ['Sheet B', 'Location 4', 'Upright'],
          ['Sheet D', 'Location 2', 'Upside down'],
          ['Sheet C', 'Location 1', 'Upside down']], 
    ['X', ['Sheet A', 'Location 4', 'Upright'],
          ['Sheet D', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upright']],
    # These data sets place four sheets in various locations and orientations
    # Data sets 44 - 48
    ['O', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 2', 'Upright'],
          ['Sheet B', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 1', 'Upright'],
          ['Sheet A', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upside down']],
    ['O', ['Sheet C', 'Location 2', 'Upright'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down'],
          ['Sheet A', 'Location 4', 'Upright']],
    ['X', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upside down']],     
    # These data sets draw the entire image upside down
    # Data sets 49 - 50
    ['X', ['Sheet A', 'Location 4', 'Upside down'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down']],
    ['O', ['Sheet A', 'Location 4', 'Upside down'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down']],
    # These are the final, 'correct' arrangements of sheets
    # Data sets 51 - 52
    ['X', ['Sheet A', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']]
    ]

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "paste_up" function.
#

# Paste the sheets onto the billboard as per the provided data set

# SHEET A =========================================================
def sheet_A():
    # Background colour
    color('#050812')
    begin_fill()
    pendown()
    forward(100)
    left(90)
    forward(250)
    left(90)
    forward(200)
    left(90)
    forward(500)
    left(90)
    forward(200)
    left(90)
    forward(250)
    end_fill()
    
    # Bottom Purple Walls
    right(180)
    forward(100)
    color('#1b2768')
    begin_fill()
    forward(150)
    right(90)
    forward(50)
    right(90)
    forward(70)
    left(90)
    forward(150)
    right(90)
    forward(80)
    right(90)
    forward(200)
    end_fill()


    # Top Purple Walls
    left(90)
    forward(165)
    begin_fill()
    pendown()
    forward(185)
    left(90)
    forward(50)
    left(90)
    forward(145)
    circle(40, 90)
    forward(10)
    end_fill()
    penup()

    #White Outline
    left(90)
    pencolor('white')
    pendown()
    forward(185)
    left(90)
    forward(200)
    left(90)
    forward(500)
    left(90)
    forward(200)
    left(90)
    forward(315)
    right(90)
    penup()

    # White Dots
    left(180)
    forward(120)
    right(90)
    color('white')
    begin_fill()
    pendown()
    circle(10)
    penup()
    forward(80)
    pendown()
    circle(10)
    penup()
    forward(80)
    pendown()
    circle(10)
    end_fill()
    penup()

# SHEET B =========================================================
def sheet_B():
    # Background colour
    color('#050812')
    begin_fill()
    pendown()
    forward(100)
    left(90)
    forward(250)
    left(90)
    forward(200)
    left(90)
    forward(500)
    left(90)
    forward(200)
    left(90)
    forward(250)
    end_fill()

    # Top Purple Walls
    forward(65)
    color('#1b2768')
    begin_fill()
    left(90)
    forward(200)
    right(90)
    forward(185)
    right(90)
    forward(30)
    right(90)
    forward(105)
    left(90)
    forward(170)
    right(90)
    forward(80)
    end_fill()
    
    # Bottom Purple Walls
    forward(165)
    begin_fill()
    forward(80)
    right(90)
    forward(170)
    left(90)
    forward(70)
    right(90)
    forward(30)
    right(90)
    forward(150)
    right(90)
    forward(200)
    end_fill()

    # White Outline
    right(90)
    pencolor('white')
    forward(150)
    right(90)
    forward(200)
    right(90)
    forward(500)
    right(90)
    forward(200)
    right(90)
    forward(350)
    left(90)

    # White semicircles
    left(90)
    forward(95)
    left(90)
    color('white')
    pendown()
    begin_fill()
    circle(10, 180)
    end_fill()
    penup()

    left(90)
    forward(260)
    left(90)
    pendown()
    begin_fill()
    circle(10, 180)
    end_fill()
    penup()

    # White circle
    right(180)
    forward(80)
    right(180)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()

    right(90)
    forward(230)
    forward(82)
    right(90)
    forward(35)
    right(180)
    color('yellow')
    pendown()
    begin_fill()
    circle(80) # Yellow pacman circle
    end_fill()
    penup()

    # Pacman's mouth
    left(90)
    forward(80)
    left(90)
    forward(20)
    left(180)
    color('#050812')
    pendown()
    begin_fill()
    right(32)
    forward(130)
    left(122)
    forward(2*130*sin(32*pi/180))
    left(122)
    forward(130)
    end_fill()
    penup()

    # White dot inside Pacman's mouth
    left(32)
    left(90)
    forward(52.7)
    left(90)
    forward(18.03)
    right(90)
    pendown()
    begin_fill()
    color('white')
    circle(10)
    end_fill()
    penup()

# SHEET C =========================================================
def sheet_C():
    # Background colour
    color('#050812')
    begin_fill()
    pendown()
    forward(100)
    left(90)
    forward(250)
    left(90)
    forward(200)
    left(90)
    forward(500)
    left(90)
    forward(200)
    left(90)
    forward(250)
    end_fill()

    # Top Purple Wall
    left(90)
    forward(200)
    right(90)
    forward(65)
    color('#1b2768')
    begin_fill()
    forward(80)
    right(90)
    forward(50)
    right(90)
    forward(80)
    right(90)
    forward(50)
    end_fill()
    
    # Top Circle
    right(180)
    forward(50)
    begin_fill()
    circle(40)
    end_fill()
    
    right(180)
    forward(50)
    left(90)
    penup()
    forward(245)
    pendown()
    
    # Bottom Purple Wall
    begin_fill()
    right(180)
    forward(80)
    right(90)
    forward(50)
    right(90)
    forward(80)
    right(90)
    forward(50)
    end_fill()

    #Bottom Circle
    right(180)
    forward(50)
    begin_fill()
    circle(40)
    end_fill()
    penup()

    #White Outline
    left(180)
    forward(50)
    pencolor('white')
    pendown()
    left(90)
    forward(70)
    left(90)
    forward(200)
    left(90)
    forward(500)
    left(90)
    forward(200)
    left(90)
    forward(430)
    penup()
    left(90)
    forward(50)

    #White Circles
    left(90)
    forward(180)
    forward(215)
    left(90)
    forward(50)
    right(180)

    #White semicircle
    color('white')
    pendown()
    begin_fill()
    circle(10, 180)
    end_fill()
    penup()

    #White Circles
    left(90)
    forward(20)
    left(90)
    penup()
    forward(80)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()

    forward(80)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()

    right(180)
    forward(10)
    left(90)
    forward(70)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()

    forward(80)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()

    forward(80)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()

    forward(80)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()

    forward(80)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()

    right(180)
    forward(170)
    left(90)
    forward(70)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()

    #White semicircle
    forward(80)
    left(90)
    forward(20)
    left(90)
    pendown()
    begin_fill()
    circle(10,180)
    end_fill()
    penup()

# SHEET D =========================================================
def sheet_D():
    #Background Colour
    color('#050812')
    pencolor('white')
    begin_fill()
    forward(100)
    pendown()
    left(90)
    forward(250)
    left(90)
    forward(200)
    left(90)
    forward(500)
    left(90)
    forward(200)
    left(90)
    forward(250)
    end_fill()
    penup()

    #Horizontal Adjustment
    left(90)
    forward(15)
    right(90)

    # Purple Walls
    color('#1b2768')
    left(90)
    forward(105)
    pendown()
    left(90)
    forward(180)
    left(90)
    begin_fill()
    circle(40)
    end_fill()
    left(90)    
    forward(325)
    left(90)
    begin_fill()
    circle(40)
    end_fill()
    left(90)
    forward(40)
    right(90)
    forward(40)
    left(90)
    begin_fill()
    forward(245)
    left(90)
    forward(80)
    left(90)
    forward(245)
    left(90)
    forward(80)
    end_fill()
    penup()

    # White Dots
    right(90)
    forward(110)
    color('white')
    begin_fill()
    pendown()
    right(90)
    circle(10)
    penup()
    forward(80)
    pendown()
    circle(10)
    end_fill()
    penup()

# Main function

def paste_up(data_set_element):
    info = data_sets[data_set_element]
    # This assigns the desired element of data_sets to the variable info,
    # which will contains the information on the corrent sheets to be pasted.

    # This function sets the correct position and orientation for each sheet
    def pos_orient(data_pos):
        # If the element within info is a specific location, go to that location
        if info[data_pos][1] == "Location 1": 
            goto(-300, 0)
            setheading(0) #Each drawing starts facing EAST
        elif info[data_pos][1] == "Location 2":
            goto(-100, 0)
            setheading(0)
        elif info[data_pos][1] == "Location 3":
            goto(100, 0)
            setheading(0)
        elif info[data_pos][1] == "Location 4":
            goto(300, 0)
            setheading(0)

        if info[data_pos][2] == "Upside down": #Determines orientation of each sheet
            setheading(180)
            # To draw the sheet upside down, start facing the opposite direction, WEST.

    # This function allows the paste_up function to determine which sheets in
    # info are assigned to which positions before4 pasting them accordingly.
    def sheets(sheet_number):
        n = 0 # Initiate counter
        for hello in range(len(info)-1):
            # This for loop loops through the following commands len(info)-1 number of times,
            # where len(info)-1 is the number of sheets to be pasted up.
            n = n+1 # Starting n = 1 skips the zeroth element of info ie. ('X')
            if info[n][0] == sheet_number:
                # This IF statement checks if inputted sheet (ie. "Sheet A") matches
                # each sheet within info, if it does, it calls the pos_orient
                # function before pasting up the sheet.
                pos_orient(n)
                if sheet_number == "Sheet A":
                    sheet_A() # This function is defined above and draws the sheets
                elif sheet_number == "Sheet B":
                    sheet_B()
                elif sheet_number == "Sheet C":
                    sheet_C()
                elif sheet_number == "Sheet D":
                    sheet_D()

    # Calling the sheets function which checks if each sheet is in the
    # specific element of data_sets, then pastes it in its correct position and
    # orientation.
    sheets("Sheet A")
    sheets("Sheet B") # call this function for each sheet
    sheets("Sheet C")
    sheets("Sheet D")

    # If the first element (zeroth) of info is 'X', draw the initials A.F
    # The following code is to draw the initials
    if info[0] == 'O':
        goto(-350,-150)
        setheading(30)
        pendown()
        pencolor('green')
        pensize(20)
        for hello in range(30): # Create a line with a slight curve
            forward(15)
            left(1)
        setheading(270)
        right(15)
        for hello in range(15):
            forward(15)
            left(1)
        for hello in range(25):
            forward(4)
            left(2)
        for hello in range(25):
            forward(2)
            left(4)
        setheading(337)
        penup()
        forward(38)
        pendown()
        circle(1)
        setheading(0)
        penup()
        forward(40)
        pendown()
        left(60)
        for hello in range(25):
            forward(13)
            left(2)
        setheading(330)
        for hello in range(20):
            forward(10)
            left(2)
        penup()
        goto(150,0)
        pendown()
        setheading(330)
        for hello in range(15):
            forward(10)
            left(3)
        penup()
        goto(-200,-50)
        pendown()
        setheading(330)
        for hello in range(11):
            forward(12)
            left(4)
    # End graffiti

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your billboard.  Do not change any of this code except
# where indicated by comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the centre points of each sheet on the backing
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with one that describes the image
# ***** displayed on your billboard when the sheets are pasted
# ***** correctly
title("Describe your billboard's image here")

### Call the student's function to display the billboard
### ***** Change the number in the argument to this function
### ***** to test your code with a different data set
paste_up(52)

# Exit gracefully
release_drawing_canvas()

#
#--------------------------------------------------------------------#

