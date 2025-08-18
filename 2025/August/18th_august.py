# Find H-Index 

citations=[3,0,5,3,0]

def bruteForce(citations):
    n=len(citations)
    maxH=0
    # try all values of h from 1 to n
    for h in range(1,n+1):
        count=0
        for c in citations:
            if c >= h:
                count += 1
        if count >= h:
            maxH = h
    return maxH

# sorting
def optimized(citations):
    citations.sort(reverse=True)
    n = len(citations)
    h=0
    for i in range(n):
        if citations[i] >= i + 1:
            h = i + 1
        else:
            break
    return h

print(bruteForce(citations))
print(optimized(citations))


"""
# Java Snippet:
# import java.util.Arrays;
#
# public class HIndex {
#     public static int hIndex(int[] citations) {
#         Arrays.sort(citations);
#         int n = citations.length;
#         int h = 0;
#         for (int i = n - 1; i >= 0; i--) {
#             if (citations[i] >= n - i) {
#                 h = n - i;
#             } else {
#                 break;
#             }
#         }
#         return h;
#     }
# }
# """