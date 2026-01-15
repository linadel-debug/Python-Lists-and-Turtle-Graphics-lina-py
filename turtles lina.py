import turtle
sideLength = int(input("Enter the size of each side: "))
screen = turtle.Screen()
screen.clearscreen()
hexagon = turtle.Turtle()
colors = ["#7209B7", "#FEE440","#FF37A6", "#A7C957", "#4CC9F0", "#D67316"]
hexagon.speed(1)
hexagon.fillcolor("#FFCAE9")
hexagon.pensize(2)
hexagon.begin_fill()
for i in range(6):
    hexagon.pencolor(colors[i])
    hexagon.forward(sideLength)
    hexagon.right(60)

hexagon.end_fill()
turtle.done()

