from slist import SList


def stack(s):

    brackets = SList()

    while s :

        p = s.pop(0)

        if brackets.is_empty():

            if p == "}" or p == ")":

                print("Wrong brackets.")

                return

            elif p == "{" or p == "(":

                brackets.push(p)
                print(p)

        else:

            if p == '}':

                pop = brackets.pop()
                print(p)

                if pop != '{':

                    print("Wrong brackets.")

                    return


            elif p == ')':

                pop = brackets.pop()
                print(p)

                if pop != '(':

                    print("Wrong brackets.")

                    return

            elif p == "{" or p == "(":

                brackets.push(p)
                print(p)


    if brackets.is_empty():

        print("Good brackets.")

        return

    else:

        print("Wrong brackets.")

        return



b = ["{", "{", ")", "{", "(", ")", "}", "}", "}"]
stack(b)
