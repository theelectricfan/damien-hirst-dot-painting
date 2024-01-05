import turtle
import random

tom = turtle.Turtle()
tom.speed(0)
tom.width(1)
tom.hideturtle()
screen = turtle.Screen()
screen.colormode(255)


color_palette = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99),
                 (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64),
                 (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77),
                 (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90),
                 (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84), (164, 203, 208), (183, 190, 204),
                 (83, 70, 40), (11, 112, 106)]

tom.penup()
tom.right(90)
tom.forward(50*5)
tom.right(90)
tom.forward(50*5)
tom.right(90)
tom.right(90)

for n in range(10):
    tom.setpos(- 50 * 5, - 50 * 5 + 50 * n)
    for m in range(10):
        used_color=random.choice(color_palette)
        tom.color(used_color)
        tom.fillcolor(used_color)
        tom.pendown()
        tom.begin_fill()
        tom.circle(10)
        tom.end_fill()
        tom.penup()
        tom.forward(50)

screen.exitonclick()