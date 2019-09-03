def convertM(m):
    newM = ""
    for idx, i in enumerate(m):
        if i.isalpha():
            tmp = i+"*"
            newM += tmp
        elif i=="#":
            newM = newM[:-1] + i
        
    return newM

def solution(m, musicinfos):
    m = convertM(m)
    
    res=[]
    
    for music in musicinfos:
        
        (ST,ET,TITLE,CODE) = music.split(",")
        
        (SH,SM) = ST.split(":")
        ST = int(SH)*60 + int(SM)
        (EH,EM) = ET.split(":")
        ET = int(EH)*60 + int(EM)
        
        #만약 음악이 00:00넘긴다는 조건이 들어가면 여기에 들어가야함
        if ET < ST:
            ET = 24*60
        
        DURING = ET-ST
        CODE = convertM(CODE)
        CODE_LENGTH = len(CODE)
        D_DURING = DURING*2
        
        RE = D_DURING//CODE_LENGTH
        END = D_DURING%CODE_LENGTH

        ALL_CODE = CODE*RE + CODE[:END]
        
        if m in ALL_CODE:
            if len(res)==0:
                res = [DURING, TITLE]
            else:
                if res[0]<DURING:
                    res = [DURING, TITLE]
        
    if len(res)==0:
        return "(None)"
    else: return res[1]

print(solution("ABCDEFGV", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))