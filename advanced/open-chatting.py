def solution(records):

    users = dict()

    history = []

    for idx, record in enumerate(records):
        try:
            (action, uid, username) = record.split(" ")
            record = [action, uid, username]
        except:
            (action, uid) = record.split(" ")
            record = [action, uid]
        records[idx] = record

    for record in records:
        if record[0] == "Enter":
            users[record[1]] = record[2]
        elif record[0] == "Change":
            users[record[1]] = record[2]

    for record in records:
        act = ""
        if record[0] == "Change":
            continue
        elif record[0] == "Enter":
            act = "님이 들어왔습니다."
        elif record[0] == "Leave":
            act = "님이 나갔습니다."
        history.append(users[record[1]]+act)

    return history