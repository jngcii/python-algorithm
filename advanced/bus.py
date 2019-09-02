def make_time(t):
    HH = t//60
    MM = t%60

    if HH < 10:
        HH = "0" + str(HH)
    else: HH = str(HH)
    if MM < 10:
        MM = "0" + str(MM)
    else: MM = str(MM)

    return HH+":"+MM


def solution(n, t, m, timetable):
    res = 0
    total = 0

    first_bus = 9*60

    table = []

    for ta in timetable:
        (hh,mm) = ta.split(":")
        x = int(hh)*60 + int(mm)
        table.append(x)

    table = sorted(table, reverse=True)

    for i in range(n):
        a_time = first_bus + i*t
        to = 0
        t_length = len(table)

        for j in range(t_length-1, -1, -1):
            if n*m - 1 == total:
                p = table.pop()

                if p <= a_time:
                    res = p-1
                else: res = a_time

                return make_time(res)

            if to == m: break
            if table[j] <= a_time:
                table.pop()
                to += 1
                total += 1

        # T.O가 남아있으면
        if to < m:
            if total + m == n*m:
                res = a_time
                return make_time(res)

        total = (i+1) * m

        if i == n-1:
            res = a_time
            return make_time(res)