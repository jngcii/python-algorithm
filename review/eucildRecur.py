def euclidRecur(a,b):

    if b == 0: return a

    return euclidRecur(b, a%b)



print(euclidRecur(120, 96))