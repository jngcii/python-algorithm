def hanoi(f, w, t, n):

    if n>1: hanoi(f, t, w, n-1)

    print("move tray", n, " from ", f, " to ", t)

    if n>1: hanoi(w, f, t, n-1)




hanoi("c1", "c2", "c3", 4)