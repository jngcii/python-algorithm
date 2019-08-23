def palindrome(s):

    que = []
    stk = []

    for x in s:

        if x.isalpha():
            que.append(x.lower())
            stk.append(x.lower())

    while que:
        if que.pop(0) != stk.pop(): return False

    return True


print(palindrome("wow"))
print(palindrome("Madam, I'm Adam"))
print(palindrome("Madam, I am Adam"))