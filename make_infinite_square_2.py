import turtle as t

def spiral (n):

    start_line = n * 10



    if n <= 1:
        return

    t.forward(start_line)
    t.right(90)
    t.forward(start_line)
    t.right(90)
    t.forward(start_line - 5)
    t.right(90)
    t.forward(start_line - 5)
    t.right(90)

    spiral(n-1)


t.speed(1)
spiral(30)
t.hideturtle()
t.done()
