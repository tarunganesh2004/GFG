# Longest Periodic Proper Prefix

s="abcab"

def getLongestPrefix(s):
    n=len(s)
    fail_table=[0]*n
    pattern_i=0
    for i in range(1,n):
        while s[i]!=s[pattern_i]:
            if pattern_i==0:
                break
            pattern_i=fail_table[pattern_i-1]
        else:
            pattern_i+=1
        fail_table[i]=pattern_i
    
    if fail_table[-1]==0:
        return -1
    shortest=fail_table[-1]
    while f:= fail_table[shortest-1]:
        shortest=f
    return n-shortest

print(getLongestPrefix(s))

"""
Java Snippet:
public static int getLongestPrefix(String s) {
    int n = s.length();
    int[] failTable = new int[n];
    int patternIndex = 0; // Index in the pattern

    for (int i = 1; i < n; i++) {
        while (s.charAt(i) != s.charAt(patternIndex)) {
            if (patternIndex == 0) {
                break;
            }
            patternIndex = failTable[patternIndex - 1];
        }
        if (s.charAt(i) == s.charAt(patternIndex)) {
            patternIndex++;
        }
        failTable[i] = patternIndex;
    }

    if (failTable[n - 1] == 0) {
        return -1; // No proper prefix found
    }

    int shortest = failTable[n - 1];
    while ((shortest = failTable[shortest - 1]) > 0) {
        // Keep finding the shortest prefix
    }
    
    return n - shortest;
}
"""