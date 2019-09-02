def solution(m, musicinfos):
    res = []
    
    for music in musicinfos:
        (start,end,title,code) = music.split(",")
        (s_hh, s_mm) = start.split(":")
        (e_hh, e_mm) = end.split(":")
        start = int(s_hh)*60 + int(s_mm)
        end = int(e_hh)*60 + int(e_mm)
        during = end - start
        
        c = []
        for i in code:
            if i == "#": c[-1]+=i
            else: c.append(i)
        code_count = len(c)
        
        if during > code_count:
            re_play = during//code_count
            remain = during%code_count
            
            code = code*re_play + ''.join(c[:remain])
            
        if code.find(m) != -1 :
            if code.find(m)+len(m)==len(code): res.append([title, during])
            elif code[code.find(m)+len(m)] != "#": res.append([title, during])
                
    if len(res) == 0: return None
    elif len(res) == 1: return res[0][0]
    else:
        max = res[0]
        for r in res:
            if r[1] > max[1]: max = r
                
        return max[0]