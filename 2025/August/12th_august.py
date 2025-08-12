# Shop in Candy Store

prices=[3,2,1,4]
k=2

def minMaxCandy(prices,k):
    prices.sort()
    n = len(prices)

    min_cost=0
    i,end= 0, n - 1
    while i<=end:
        min_cost += prices[i]
        i += 1
        end -= k
    
    max_cost=0
    i,start=n-1,0
    while i>=start:
        max_cost += prices[i]
        i -= 1
        start += k
    return [min_cost, max_cost]

print(minMaxCandy(prices, k))

"""Java Snippet:
public class CandyStore {
    public static int[] minMaxCandy(int[] prices, int k) {
        Arrays.sort(prices);
        int n = prices.length;

        int minCost = 0;
        int i = 0, end = n - 1;
        while (i <= end) {
            minCost += prices[i];
            i++;
            end -= k;
        }

        int maxCost = 0;
        i = n - 1;
        int start = 0;
        while (i >= start) {
            maxCost += prices[i];
            i--;
            start += k;
        }
        
        return new int[]{minCost, maxCost};
    }
}
"""