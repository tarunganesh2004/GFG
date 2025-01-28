# Permutations of a String

s="ABC"
# output: ABC, ACB, BAC, BCA, CAB, CBA

def find_permutation(s): # Time complexity: O(n*n!) Space complexity O(n*n!)
    res=[]
    if len(s)==1:
        return [s]
    
    def backtrack(s,per,res,depth):
        print(
            f"{'  ' * depth}Level {depth}: Current string = {s}, Current permutation = {per}"
        )
        if len(s)==0:
            res.append(per)
            print(f"{'  ' * depth}Adding to results: {per}")
            return
        seen=set()
        for i in range(len(s)):
            if s[i] not in seen:
                remaining=s[:i]+s[i+1:]
                print(
                    f"{'  ' * depth}Using character '{s[i]}' -> Remaining string = {remaining}"
                )
                backtrack(remaining,per+s[i],res,depth+1)
                seen.add(s[i])
                print(f"{'  ' * depth}Backtracking from character '{s[i]}'")
                
    backtrack(s,"",res,0)
    return res

print(find_permutation(s))