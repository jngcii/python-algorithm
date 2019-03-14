import turtle as t

def infinite_square(n):

    cycle = n*4

    if cycle <=4:
        return

    t.forward(cycle)
    t.left(90)
    t.forward(cycle)
    t.left(90)
    t.forward(cycle-2)
    t.left(90)
    t.forward(cycle-2)
    t.left(90)

    infinite_square(n-1)

t.speed(0)
infinite_square(200)
