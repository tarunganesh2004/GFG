# Possible Words from Phone Digits

arr=[2,3]

def possibleWords(arr):
    mapping={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
    res=[]

    def backtrack(index,path):
        if index==len(arr):
            res.append("".join(path))
            return
        # possible_chars=mapping[arr[index]]
        digit=arr[index]
        if digit not in mapping:
            # skip 0 & 1
            backtrack(index+1,path)
            return
        possible_chars=mapping[digit]
        for char in possible_chars:
            path.append(char)
            backtrack(index+1,path)
            path.pop()
    backtrack(0,[])
    return res

print(possibleWords(arr))