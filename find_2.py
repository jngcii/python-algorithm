def find_students(n):

    stu_no = [39, 14, 67, 105]
    stu_name = ["Justin", "John", "Mike", "Summer"]

    for i in range(len(stu_no)):

        if stu_no[i] == n:

            return stu_name[i]

    return "?"




print(find_students(105))
