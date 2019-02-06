def make_infinite_square(n):

    start_line = 2*n

    print("go {} centimeter".format(start_line))
    print("turn Left")
    print("go {} centimeter".format(start_line))
    print("turn Left")
    print("go {} centimeter".format(start_line - 1))
    print("turn Left")
    print("go {} centimeter".format(start_line - 1))
    print("turn Left")

    if n == 1:

        return

    make_infinite_square(n-1)


make_infinite_square(2)
