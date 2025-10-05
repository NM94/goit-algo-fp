import turtle

def draw_branch(t, length, level, angle):
    if level == 0:
        return
    
    
    t.forward(length)
    t.left(angle)
    draw_branch(t, length * 0.9, level - 1, angle)
    t.right(2 * angle)
    draw_branch(t, length * 0.9, level - 1, angle)
    t.left(angle)
    t.backward(length)


screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

t.penup()
t.goto(0, -250)  
t.pendown()
t.left(90)  

level = 8
draw_branch(t, length=100, level=level, angle=30)

screen.mainloop()


