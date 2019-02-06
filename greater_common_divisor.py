def gcd(num1, num2):

    for i in range(num1+1, 1, -1):

        if num1%i == 0 and num2%i == 0:

            return i

inst1 = gcd(27, 12)
print(inst1)
