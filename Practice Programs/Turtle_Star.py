import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
# Create a turtle object
star = turtle.Turtle()
star.color("yellow")

def draw_star(size):
    for _ in range(5):
        star.forward(size)
        star.right(144)  # angle for a star

draw_star(100)
turtle.done()
