# Non overlapping intervals
# we need to remove the minimum number of intervals to make the rest of the intervals non-overlapping.

intervals=[[1,2],[2,3],[3,4],[1,3]]

def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x:x[1])
    end=intervals[0][1]
    count=1

    for i in range(1,len(intervals)):
        if intervals[i][0]>=end:
            end=intervals[i][1]
            count+=1

    return len(intervals)-count

print(eraseOverlapIntervals(intervals))