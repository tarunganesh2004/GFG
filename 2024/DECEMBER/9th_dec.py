# Insert Interval

intervals=[[1,3],[4,5],[6,7],[8,10],[12,16]]
newInterval=[5,6]

def insertInterval(intervals,newInterval):
    intervals.append(newInterval)
    intervals.sort(key=lambda x:x[0])

    res=[intervals[0]]
    for i in range(1,len(intervals)):
        if res[-1][-1]>=intervals[i][0]:
            res[-1][-1]=max(res[-1][-1],intervals[i][-1])
        else:
            res.append(intervals[i])

    return res

print(insertInterval(intervals,newInterval))