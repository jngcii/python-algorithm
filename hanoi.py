def hanoi(n, beginning, ending, waypoint):

    if n == 1:

        print(beginning, "->", ending)

        return


    hanoi(n-1, beginning, waypoint, ending)

    print(beginning, "->", ending)

    hanoi(n-1, waypoint, ending, beginning)


hanoi(4, "Beginning Point", "Ending Point", "Way Point")
