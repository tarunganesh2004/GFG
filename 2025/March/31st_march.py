# Maximize partitions in a String

s="acbbcc"

def maxPartitions(s):
    last_position={}
    for i,char in enumerate(s):
        last_position[char]=i
    res=[]
    start=0
    end=0
    for i,char in enumerate(s):
        end=max(end,last_position[char])
        if i==end:
            res.append(end-start+1)
            start=end+1
    return len(res)

print(maxPartitions(s)) 