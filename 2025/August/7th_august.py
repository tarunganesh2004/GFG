# Difference Check

arr=["12:30:15","12:30:45"]

def minDifference(arr):
    min_dif=float('inf')
    def time_to_seconds(str):
        h,m,s=map(int, str.split(':'))
        return h * 3600 + m * 60 + s
    
    times = [time_to_seconds(time) for time in arr]
    n = len(times)
    times.sort()
    for i in range(1,n):
        diff=times[i]-times[i-1]
        min_dif=min(min_dif,diff)
    
    # Check the circular difference
    wrap_around_diff=86400 - times[-1] + times[0]
    min_dif=min(min_dif, wrap_around_diff)
    return min_dif

print(minDifference(arr))

"""
Java Snippet:
public static int minDifference(String[] timePoints) {
    int minDiff = Integer.MAX_VALUE;
    
    // Convert time strings to seconds
    int[] times = new int[timePoints.length];
    for (int i = 0; i < timePoints.length; i++) {
        String[] parts = timePoints[i].split(":");
        int h = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);
        int s = Integer.parseInt(parts[2]);
        times[i] = h * 3600 + m * 60 + s;
    }
    
    Arrays.sort(times);
    
    // Calculate minimum difference
    for (int i = 1; i < times.length; i++) {
        minDiff = Math.min(minDiff, times[i] - times[i - 1]);
    }
    
    // Check the circular difference
    minDiff = Math.min(minDiff, 86400 - times[times.length - 1] + times[0]);
    
    return minDiff;
}
"""