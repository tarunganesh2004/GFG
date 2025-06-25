# Check if frequencies can be equal



s="xyyz"

def sameFreq(s):
    freq={}
    for i in s:
        freq[i]=freq.get(i,0)+1
    
    counts=list(freq.values())
    max_count=max(counts)
    min_count=min(counts)

    if max_count== min_count:
        return True
    
    if (max_count-min_count==1) and counts.count(max_count)==1:
        return True
    
    if counts.count(1)==1 and len(set(counts))==2 and counts.count(min_count)==1:
        return True
    
    return False

print(sameFreq(s))  # Output: True