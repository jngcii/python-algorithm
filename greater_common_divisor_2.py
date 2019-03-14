def gcd(num1, num2):

    if num2 == 0:

        return num1

    return gcd(num2, num1%num2)

inst1 = gcd(60, 24)
print(inst1)
