import turtle

# Setup The Screen

screen = turtle.Screen()

screen.bgcolor("black")
screen.title("Mandala Project")

# Create The Turtle

mandala_turtle = turtle.Turtle()
mandala_turtle.speed(0)

# Function To Draw A Circle With A Given Radius And Color

def draw_circle(turtle, radius, color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Function To Draw A Petal

def draw_petal(turtle, color):
    turtle.color(color)
    turtle.begin_fill
    for _ in range(2):
        turtle.circle(50, 60)
        turtle.left(120)
        turtle.circle(50, 60)
        turtle.left(120)
    turtle.end_fill()

# Function To Draw A Layer Of Petals

def draw_layer_of_petals(turtle, num_petals, color):
    angle = 360 / num_petals
    for _ in range(num_petals):
        draw_petal(turtle, color)
        turtle.right(angle)

# Draw The Mandala

colors = ["red", "orange", "yellow", "green", "blue", "purple", "violet", "magenta"]

# Draw The Inner Circles

mandala_turtle.penup()
mandala_turtle.goto(8, -50) # Move The Red Circle Down
mandala_turtle.pendown()
draw_circle(mandala_turtle, 50, "red")
mandala_turtle.penup
mandala_turtle.goto(0, -35) # Adjust Subsequent Circle Positions
mandala_turtle.pendown
draw_circle(mandala_turtle, 35, "orange")
mandala_turtle.penup
mandala_turtle.goto(0, -20)
mandala_turtle.pendown()
draw_circle(mandala_turtle, 20, "yellow")

# Draw Layers Of Petals

mandala_turtle.penup()
mandala_turtle.goto(0, 0)
mandala_turtle.pendown()
for i in range(6):
    draw_layer_of_petals(mandala_turtle, 6 + i, colors [i % len(colors)])
    mandala_turtle.right(30)

# Hide The Turtle And Finish

mandala_turtle.hideturtle()
turtle.done()