# Tywin's War Strategy

arr=[5,6,3,2,1]
k=2

def minSoldiers(arr,k):
    import math
    n=len(arr)

    # find number of lucky troops
    lucky_count=0
    for x in arr:
        if x % k == 0:
            lucky_count += 1
    
    # target(required number of lucky troops)
    target=math.ceil(n/2)

    if lucky_count >= target:
        return 0
    
    # cost for each unlucky troop
    costs=[]
    for x in arr:
        if x%k!=0:
            costs.append(k-(x%k))
    
    costs.sort()

    needed= target - lucky_count
    total=sum(costs[:needed])
    return total

print(minSoldiers(arr, k))

"""Java Snippet:
public class TywinsWarStrategy {
    public static int minSoldiers(int[] arr, int k) {
        int n = arr.length;
        int luckyCount = 0;
        for (int x : arr) {
            if (x % k == 0) {
                luckyCount++;
            }
        }
        int target = (int) Math.ceil(n / 2.0);
        if (luckyCount >= target) {
            return 0;
        }
        List<Integer> costs = new ArrayList<>();
        for (int x : arr) {
            if (x % k != 0) {
                costs.add(k - (x % k));
            }
        }
        Collections.sort(costs);
        int needed = target - luckyCount;
        int total = 0;
        for (int i = 0; i < needed; i++) {
            total += costs.get(i);
        }
        return total;
    }
    
"""