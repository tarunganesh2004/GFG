# Sum-string 

s="12243660"

def sum_string(s):
    n=len(s)
    def addStrings(num1, num2):
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        len1= len(num1)
        len2= len(num2)
        sum=""
        carry=0

        for i in range(len2):
            d1=ord(num1[len1-1-i])-ord('0')
            d2=ord(num2[len2-1-i])-ord('0')
            digit=(d1 + d2 + carry) % 10
            carry=(d1 + d2 + carry) // 10
            sum=chr(digit + ord('0')) + sum

        for i in range(len2, len1):
            d1=ord(num1[len1-1-i])-ord('0')
            digit=(d1 + carry) % 10
            carry=(d1 + carry) // 10
            sum=chr(digit + ord('0')) + sum
        
        if carry:
            sum=chr(carry + ord('0')) + sum
        return sum


    def checkSequence(s,start,i,j):
        part1=s[start:start+i]
        part2=s[start+i:start+i+j]
        expectedSum=addStrings(part1,part2)

        sumLen=len(expectedSum)
        if start+i+j+sumLen > n:
            return False
        
        if expectedSum == s[start+i+j:start+i+j+sumLen]:
            return True
        
        return checkSequence(s,start+i,j,sumLen)
    for i in range(1,n):
        for j in range(1,n-i):
            if checkSequence(s,0,i,j):
                return True
    return False

# another approach
def isSumString(s):
    n=len(s)
    def is_valid(prev1,prev2,start):
        if start>=n:
            return True
        
        if s[start] == '0':
            return False
        
        for end in range(start+1,n+1):
            cur=int(s[start:end])
            if cur == prev1 + prev2:
                if is_valid(prev2, cur, end):
                    return True
        return False
    for i in range(1, n-1):
        for j in range(i+1,n):
            first=int(s[:i])
            if s[i] == '0':
                continue
            second=int(s[i:j])
            if is_valid(first, second, j):
                return True
    return False

print(sum_string(s))  # Output: True
print(isSumString(s))  # Output: True