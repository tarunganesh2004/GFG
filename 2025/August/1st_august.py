# Balancing Consonants and Vowels

arr=["aeio","aa","bc","ot","cdbd"]

# brute force
def bruteForce(arr):
    n=len(arr)
    count=0
    vowels="aeiou"
    for i in range(n):
        for j in range(i,n):
            sub="".join(arr[i:j+1]) # concatenate arr[i] to arr[j]
            # print(sub)
            v=0
            c=0
            for char in sub:
                if char in vowels:
                    v+=1
                else:
                    c+=1
            if v==c:
                count+=1
    return count

# optimized is to use prefix sum
# create a balances array to represent the difference between vowels and consonants
# then build prefix sum of the balances
# if prefix[i]==prefix[j], then the subarray arr[i:j-1] is balanced
def countBalancedOptimized(arr): # O(n*l)
    vowels="aeiou"

    def get_balance(s):
        v=sum(1 for ch in s if ch in vowels)
        c=len(s)-v
        return v - c
    
    # convert arr to balance
    balances=[get_balance(s) for s in arr]

    # build prefix sums
    prefix_sum=0
    freq={0:1}
    count=0
    for b in balances:
        prefix_sum+=b
        if prefix_sum in freq:
            count+=freq[prefix_sum]
            freq[prefix_sum]+=1
        else:
            freq[prefix_sum]=1
    return count



print(bruteForce(arr))
print(countBalancedOptimized(arr))


"""
Java Snippet:
    public static int optimized(String[] s) {
        int n= s.length;
        int[] balanced = new int[n];
        for (int i = 0; i < s.length; i++) {
            balanced[i] = getBalance(s[i]);
        }
        int count = 0;
        Map<Integer, Integer> map = new HashMap<>();
        int prefixSum = 0;
        map.put(0, 1);
        for (int i = 0; i < n; i++) {
            prefixSum += balanced[i];
            if (map.containsKey(prefixSum)) {
                count += map.get(prefixSum);
                map.put(prefixSum, map.get(prefixSum) + 1);
            } else {
                map.put(prefixSum, 1);
            }
        }
        return count;

    }

    public static int getBalance(String s) {
        int vowels = 0, consonants = 0;
        for (char ch : s.toCharArray()) {
            if ("aeiou".indexOf(ch) != -1) {
                vowels++;
            } else {
                consonants++;
            }

        }
        return vowels - consonants;
    }
"""