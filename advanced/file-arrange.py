def solution(files):
    for idx, file in enumerate(files):
        head=None
        number=None
        tail=None
        
        i = 0
        while file[i].isdigit() == False:
            i += 1
        head=file[:i]
        
        
        j=i
        while file[j].isdigit() == True:
            if j+1 < len(file):
                j+=1
            else: j+=1;break
        number=file[i:j]
            
        try:
            tail = file[j:]
        except: tail = ""
            
        print("head:",head,"number:",number,"tail:",tail)
        print(head+number+tail)
        
        files[idx] = (head, number, tail)
        
    files.sort(key=lambda x : (x[0].lower(), int(x[1])))
    
    return [file[0]+file[1]+file[2] for file in files]