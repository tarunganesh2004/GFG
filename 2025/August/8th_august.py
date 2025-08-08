# Longest Prefix Suffix

s="aabcdaabc"

def getLPSLength(s):
    n=len(s)
    lps=[0]*n
    length=0
    i=1
    lps[0]=0  
    while i<n:
        if s[i]==s[length]:
            length+=1
            lps[i]=length
            i+=1
        else:
            if length!=0:
                length=lps[length-1]
            else:
                lps[i]=0
                i+=1
    return lps[n-1]

print(getLPSLength(s))

"""Java Snippet:
public static int getLPSLength(String s) {
    int n = s.length();
    int[] lps = new int[n];
    int length = 0; // Length of the previous longest prefix suffix
    int i = 1; // Current index in the string

    lps[0] = 0; // LPS for the first character is always 0

    while (i < n) {
        if (s.charAt(i) == s.charAt(length)) {
            length++;
            lps[i] = length;
            i++;
        } else {
            if (length != 0) {
                length = lps[length - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps[n - 1];
}
"""