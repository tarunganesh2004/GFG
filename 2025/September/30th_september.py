# Generate All Binary Strings

n=2

def generateBinaryStrings(n):
    def backtrack(s):
        if len(s)==n:
            result.append(s)
            return
        backtrack(s+'0')
        backtrack(s+'1')
    result=[]
    backtrack('')

    return result

print(generateBinaryStrings(n))