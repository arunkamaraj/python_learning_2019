import turtle

def draw(points, color):
    myTurtle.fillcolor(color)

    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()

    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()
    # pass

def midValue(p1,p2):
    return [(p1[0] + p2[0])/2, (p1[1] + p2[1])/2]

def my_try(degree, points):
    colormap = ['blue', 'red', 'green', 'white', 'yellow',
                'violet', 'orange']
    draw(points, colormap[degree])

    if degree > 0:
        my_try(degree - 1, [points[0], midValue(points[0],points[1]), midValue(points[0], points[2])])
        my_try(degree - 1, [points[1], midValue(points[1], points[2]), midValue(points[1], points[0])])
        my_try(degree - 1, [points[2], midValue(points[2], points[0]), midValue(points[2], points[1])])


if __name__ == '__main__':
    myTurtle = turtle.Turtle()
    win  = turtle.Screen()
    degree =3
    points = [[-100,-50],[0,100],[100,-50]]
    my_try(degree,points)
    win.exitonclick()

