def solution(records):
    d = dict()
    result = []
    
    for idx, record in enumerate(records):
        if record[:5] == "Leave":
            (action, uid) = record.split(" ")
            action = "님이 나갔습니다."
        else:
            (action, uid, username) = record.split(" ")
            d[uid] = username
            if action=="Enter": action = "님이 들어왔습니다."
        records[idx] = [action, uid]
        
    for record in records:
        if record[0] != "Change":
            respones = d[record[1]] + record[0]
            result.append(respones)
            
    return result