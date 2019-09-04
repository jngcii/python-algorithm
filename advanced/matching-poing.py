def solution(word, pages):
    d = {}
    
    for page in pages:
        
        name_idx = page.index("content=")
        name_idx += 8
        
        last_idx = name_idx
        while page[last_idx] != ">":
            last_idx += 1
            
        name = page[name_idx+1:last_idx-2]
        
        basic = 0
        
        for ii in range(len(page)-len(word)):
            if page[ii:ii+len(word)].lower() == word.lower():
                if ii <= 0:
                    if page[ii+len(word)].isalpha(): break
                else:
                    if ii+len(word) >= len(page)-1:
                        if page[ii-1].isalpha(): break
                    else:
                        if page[ii-1].isalpha(): break
                        elif page[ii+len(word)].isalpha(): break
                basic += 1
                    
            else: ii += 1
        
        out = page.count("<a href")
        link = []
        
        link_idx = page.index("<a href=")
        link_idx += 9
        
        while link_idx != -1:
            l_idx = link_idx
            l_idx += 10
            if l_idx >= len(page): break
            while page[l_idx] != ">":
                l_idx += 1
                if l_idx >= len(page): break
                
            lin = page[link_idx:l_idx-1]
            link.append(lin)
            
            if page[l_idx:].find("<a href=") == -1:
                link_idx = -1;
            else: link_idx = l_idx+1 + page[l_idx+1:].index("<a href=") + 9
        
        d[name] = [basic, out, 0, link]
        
    
    for key, val in d.items():
        for url in val[3]:
            if url in d.keys():
                d[url][2] += val[0]/val[1]
    
    for val in d.values():
        val.append(val[0]+val[2])
            
    asdf = list(d.values())
    
    maxim = -1
    res = -1
    for idx, asd in enumerate(asdf):
        if asd[4] > maxim:
            maxim = asd[4]
            res = idx
            
    return res