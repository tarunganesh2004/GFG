# Activity Selection



start=[1,3,0,5,8,5]
end=[2,4,6,7,9,9]

def activitySelection(start,end):
    activities=sorted(zip(end,start))
    count,last_end=0,-1
    for end,begin in activities:
        if begin>last_end:
            count+=1
            last_end=end
    return count
            
print(activitySelection(start,end)) # 4