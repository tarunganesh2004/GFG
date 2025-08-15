

intervals = [[1, 3], [4, 5], [6, 7], [8, 10]]
newInterval=[5,6]

def insertInterval(intervals, newInterval):

    intervals.append(newInterval)

    res=[]
    intervals.sort(key=lambda x: x[0])
    start, end = intervals[0]
    for i in range(1, len(intervals)):
        current_start, current_end = intervals[i]
        if current_start <= end:  # Overlapping intervals
            end = max(end, current_end)
        else:
            res.append([start, end])
            start, end = current_start, current_end
    res.append([start, end])  # Add the last interval
    return res

print(insertInterval(intervals, newInterval))

"""Java Snippet:
public class InsertInterval {
    public static List<int[]> insertInterval(List<int[]> intervals, int[] newInterval) {
        intervals.add(newInterval);
        Collections.sort(intervals, Comparator.comparingInt(a -> a[0]));
        
        List<int[]> res = new ArrayList<>();
        int start = intervals.get(0)[0];
        int end = intervals.get(0)[1];
        
        for (int i = 1; i < intervals.size(); i++) {
            int currentStart = intervals.get(i)[0];
            int currentEnd = intervals.get(i)[1];
            if (currentStart <= end) {  // Overlapping intervals
                end = Math.max(end, currentEnd);
            } else {
                res.add(new int[]{start, end});
                start = currentStart;
                end = currentEnd;
            }
        }
        res.add(new int[]{start, end});  // Add the last interval
        return res;
    }
}
"""