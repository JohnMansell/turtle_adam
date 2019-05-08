import turtle
import numpy as np
import time

screen = turtle.Screen()
screenMinX = -screen.window_width() / 2
screenMinY = -screen.window_height() / 2
screenMaxX = screen.window_width() / 2
screenMaxY = screen.window_height() / 2

screen.setworldcoordinates(screenMinX, screenMinY, screenMaxX, screenMaxY)

pen = turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.penup()

# --------------------------------
#       Initialize Variables
# --------------------------------
wavelength = 100
length = 90
correction = 0

initial_state = True
first_state = False
second_state = False
third_state = False
sum_state = False

mousex = 0
mousey = 0

font_12 = ("Calibri", 12, "normal")
font_24 = ("Calibri", 24, "normal")

# --------------------------------
#       Initialize Turtles
# --------------------------------

# Turtle - Wavelength
wavelength_plus_turtle = turtle.Turtle()
wavelength_minus_turtle = turtle.Turtle()

# Turtle - Length
length_plus_turtle = turtle.Turtle()
length_minus_turtle = turtle.Turtle()

# Turtle - Waves
initial = turtle.Turtle()
first = turtle.Turtle()
second = turtle.Turtle()
third = turtle.Turtle()

# Turtle - Sum
sum_turtle = turtle.Turtle()
total = turtle.Turtle()

# Turtle - ABCD
albert = turtle.Turtle()
beatrice = turtle.Turtle()
clyde = turtle.Turtle()
dave = turtle.Turtle()

# --------------------------------
#       Turtles Array
# --------------------------------
turtles = []
turtles.append(wavelength_plus_turtle)
turtles.append(wavelength_minus_turtle)
turtles.append(length_plus_turtle)
turtles.append(length_minus_turtle)
turtles.append(initial)
turtles.append(first)
turtles.append(second)
turtles.append(third)
turtles.append(sum_turtle)
turtles.append(total)
turtles.append(albert)
turtles.append(beatrice)
turtles.append(clyde)
turtles.append(dave)

# --------------------------------
#       Hide Turtles
# --------------------------------
for turtle in turtles:
    turtle.hideturtle()

# --------------------------------
#       Set Colors
# --------------------------------

# Waves
initial.color("blue")
first.color("red")
second.color("green")
third.color("purple")

# Sum
sum_turtle.color("black")
total.color("black")

# ABCD
albert.color("blue")
beatrice.color("red")
clyde.color("green")
dave.color("purple")

# --------------------------------
#       Initialize Values
# --------------------------------

# ABCD
albertvalues = []
beatricevalues = []
clydevalues = []
davevalues = []

# SUM
totalvalues = []


# --------------------------------
#       Get Position
# --------------------------------
def getposition(x, y):
    global mousex
    global mousey
    mousex = x
    mousey = y


# --------------------------------
#       Button
# --------------------------------
def button(loc, action, turt):
    turt.penup()
    turt.clear()
    turt.setposition(loc)
    turt.setheading(0)
    turt.pendown()
    for i in range(2):
        turt.forward(30)
        turt.left(90)
        turt.forward(30)
        turt.left(90)
    turt.penup()
    action


# --------------------------------
#       Change Wavelength
# --------------------------------
def change_wavelength(change, loc):
    global mousex
    global mousey
    global wavelength
    if loc[0] < mousex < loc[0] + 30 and loc[1] < mousey < loc[1] + 30:
        wavelength += change
        if wavelength > 200:
            wavelength = 200
        if wavelength < 60:
            wavelength = 60
        mousex = 0
        mousey = 0


# --------------------------------
#       Change Length
# --------------------------------
def change_length(change, loc):
    global mousex
    global mousey
    global length
    if loc[0] < mousex < loc[0] + 30 and loc[1] < mousey < loc[1] + 30:
        length += change
        if length > 200:
            length = 200
        if length < 50:
            length = 50
        mousex = 0
        mousey = 0


# --------------------------------
#       Change Correction
# --------------------------------
def change_correction(change, loc):
    global mousex
    global mousey
    global correction
    if loc[0] < mousex < loc[0] + 30 and loc[1] < mousey < loc[1] + 30:
        correction += change
        mousex = 0
        mousey = 0


# --------------------------------
#       Toggle Initial State
# --------------------------------
def toggle_initial_state(loc):
    global mousex
    global mousey
    global initial_state
    if loc[0] < mousex < loc[0] + 30 and loc[1] < mousey < loc[1] + 30:
        if initial_state == True:
            initial_state = False
        else:
            initial_state = True
        mousex = 0
        mousey = 0


# --------------------------------
#       Toggle First Reflection
# --------------------------------
def toggle_first_reflection(loc):
    global mousex
    global mousey
    global first_state
    if loc[0] < mousex < loc[0] + 30 and loc[1] < mousey < loc[1] + 30:
        if first_state == True:
            first_state = False
        else:
            first_state = True
        mousex = 0
        mousey = 0


# --------------------------------
#       Toggle Second Reflection
# --------------------------------
def toggle_second_reflection(loc):
    global mousex
    global mousey
    global second_state
    if loc[0] < mousex < loc[0] + 30 and loc[1] < mousey < loc[1] + 30:
        if second_state == True:
            second_state = False
        else:
            second_state = True
        mousex = 0
        mousey = 0


# --------------------------------
#       Toggle Third Reflection
# --------------------------------
def toggle_third_reflection(loc):
    global mousex
    global mousey
    global third_state
    if loc[0] < mousex < loc[0] + 30 and loc[1] < mousey < loc[1] + 30:
        if third_state == True:
            third_state = False
        else:
            third_state = True
        mousex = 0
        mousey = 0


# --------------------------------
#       Toggle Sum
# --------------------------------
def toggle_sum(loc):
    global mousex
    global mousey
    global sum_state
    if loc[0] < mousex < loc[0] + 30 and loc[1] < mousey < loc[1] + 30:
        if sum_state == True:
            sum_state = False
        else:
            sum_state = True
        mousex = 0
        mousey = 0


# turtle.tracer(0, 0)

# ================================
#       Handle Button Clicks
# ================================
tim = 0
while tim < 1000:
    screen.onscreenclick(getposition)

    # Place Buttons
    button([screenMaxX - 50, 150], change_wavelength(-0.5, [screenMaxX - 50, 150]), wavelength_minus_turtle)
    button([screenMaxX - 100, 150], change_wavelength(0.5, [screenMaxX - 100, 150]), wavelength_plus_turtle)
    button([screenMaxX - 50, 80], change_length(-1, [screenMaxX - 50, 80]), length_minus_turtle)
    button([screenMaxX - 100, 80], change_length(1, [screenMaxX - 100, 80]), length_plus_turtle)
    button([screenMaxX - 50, 30], toggle_initial_state([screenMaxX - 50, 30]), initial)
    button([screenMaxX - 50, -10], toggle_first_reflection([screenMaxX - 50, -10]), first)
    button([screenMaxX - 50, -50], toggle_second_reflection([screenMaxX - 50, -50]), second)
    button([screenMaxX - 50, -90], toggle_third_reflection([screenMaxX - 50, -90]), third)
    button([screenMaxX - 50, -130], toggle_sum([screenMaxX - 50, -130]), sum_turtle)

    # Write Button Text
    pen.clear()
    pen.setposition(screenMaxX - 127, 190)
    pen.write("Wavelength = " + str(wavelength), font=font_12)

    pen.setposition(screenMaxX - 92, 120)
    pen.write("Length = " + str(length), font=font_12)

    pen.setposition(screenMaxX - 93, 155)
    pen.write("+", font=font_24)

    pen.setposition(screenMaxX - 40, 155)
    pen.write("-", font=font_24)

    pen.setposition(screenMaxX - 93, 85)
    pen.write("+", font=font_24)

    pen.setposition(screenMaxX - 40, 85)
    pen.write("-", font=font_24)

    # Incident Wave
    pen.setposition(screenMaxX - 115, 47)
    pen.write("Incident", font=font_12)
    pen.setposition(screenMaxX - 105, 32)
    pen.write("Wave", font=font_12)

    # First Reflection
    pen.setposition(screenMaxX - 108, 8)
    pen.write("First", font=font_12)
    pen.setposition(screenMaxX - 120, -7)
    pen.write("Reflection", font=font_12)

    # Second Reflection
    pen.setposition(screenMaxX - 115, -35)
    pen.write("Second", font=font_12)
    pen.setposition(screenMaxX - 120, -50)
    pen.write("Reflection", font=font_12)

    # Third Reflection
    pen.setposition(screenMaxX - 108, -75)
    pen.write("Third", font=font_12)
    pen.setposition(screenMaxX - 120, -90)
    pen.write("Reflection", font=font_12)

    # Total Interference
    pen.setposition(screenMaxX - 108, -115)
    pen.write("Total", font=font_12)
    pen.setposition(screenMaxX - 133, -130)
    pen.write("Interference", font=font_12)

    # Dot?
    pen.setposition(length - 150, -60)
    pen.pendown()
    pen.setposition(length - 150, 60)
    pen.penup()

    # Clear Turtles

    for turtle in turtles[-5:]:
        turtle.clear()

    # Albert
    if initial_state != False:
        for i in range(1, length):
            y = albert.setposition(i - 150, 50 * np.sin(1 / wavelength * 2 * np.pi * i - 0.25 * tim))
            albert.pendown()

    # Beatrice
    if first_state != False:
        for i in range(1, length):
            y = beatrice.setposition(i - 150, 50 * np.sin(
                1 / wavelength * 2 * np.pi * i + 0.25 * (tim - length * (50.3 / wavelength) + 13.2)))
            beatrice.pendown()
    # Clyde
    if second_state != False:
        for i in range(1, length):
            y = clyde.setposition(i - 150, 50 * np.sin(
                1 / wavelength * 2 * np.pi * i - 0.25 * (tim - length * (50.3 / wavelength) + 1.2)))
            clyde.pendown()

    # Dave
    if third_state != False:
        for i in range(1, length):
            y = dave.setposition(i - 150, 50 * np.sin(1 / wavelength * 2 * np.pi * i + 0.25 * (
                tim - (length * (50.3 / wavelength) + length * (50.3 / wavelength) + 10.7))))
            dave.pendown()

    # Total
    if sum_state != False:
        for i in range(1, length):
            y = total.setposition(i - 150, 50 * np.sin(1 / wavelength * 2 * np.pi * i - 0.25 * tim) +
                                  50 * np.sin(1 / wavelength * 2 * np.pi * i + 0.25 * (
                                      tim - length * (50.3 / wavelength) + 13.2)) +
                                  50 * np.sin(1 / wavelength * 2 * np.pi * i - 0.25 * (
                                      tim - length * (50.3 / wavelength) + 1.2)) +
                                  50 * np.sin(1 / wavelength * 2 * np.pi * i + 0.25 * (
                                      tim - (length * (50.3 / wavelength) + length * (50.3 / wavelength) + 10.7))))
            total.pendown()

    for turtle in turtles[-5:]:
        turtle.penup()
        turtle.setposition(-150, 0)

    albert.update()
    beatrice.update()
    clyde.update()
    dave.update()
    total.update()

    time.sleep(0.05)
    tim += 1
    if tim >= np.pi * 100:
        tim = 0
