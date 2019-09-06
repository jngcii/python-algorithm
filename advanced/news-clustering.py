from collections import Counter
import math

def solution(str1, str2):
    
    set1 = [str1[i].lower()+str1[i+1].lower() for i in range(len(str1)-1) if str1[i].isalpha() and str1[i+1].isalpha()]
    set2 = [str2[i].lower()+str2[i+1].lower() for i in range(len(str2)-1) if str2[i].isalpha() and str2[i+1].isalpha()]
    
    if not set1 and not set2: return 65536
    
    c1 = Counter(set1)
    c2 = Counter(set2)
    
    return math.floor(sum((c1 & c2).values())/sum((c1 | c2).values()) * 65536)
    