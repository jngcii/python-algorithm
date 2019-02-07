def x_func(n):

    non_overlap = []
    same_element = []

    for i in range(0, len(n)):

        if i > 0:

            if n[i] in non_overlap and n[i] not in same_element:

                same_element.append(n[i])

        if n[i] not in non_overlap:

            non_overlap.append(n[i])

    return same_element




arr1 = [1,2,1,4,5,2,3,7,7]
inst1 = x_func(arr1)
print(inst1)
