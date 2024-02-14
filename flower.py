import turtle

pen = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("black")
pen.speed(0.5)

colors = (
"chartreuse",
"darkred",
"deeppink",
"cyan2",
"light green",
"deepskyblue")

for idx in range(160):
    pen.pencolor(colors[idx % 6])
    pen.circle(160 - idx / 2, 90)
    pen.lt(90)
    pen.circle(160 - idx / 3, 90)
    pen.lt(60)

screen.exitonclick()    