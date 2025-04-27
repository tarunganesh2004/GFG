# Multiply Two Strings

s1="0033"
s2="2"

def multiply_strings(a, b):
    if a=="0" or b=="0":
        return "0"
    
    negative=False

    if a[0]=="-":
        negative=not negative
        a=a[1:]
    
    if b[0]=="-":
        negative=not negative
        b=b[1:]

    product=[0 for _ in range(len(a)+len(b))]
    # Multiplying each digit of the second string with each digit of the first string
    for i in range(len(b) - 1, -1, -1):
        digit1 = int(b[i])
        carry = 0

        # Iterating over each digit of the first string
        for j in range(len(a) - 1, -1, -1):
            digit2 = int(a[j])

            # Adding the product of the digits with the carry
            product[i + j + 1] += digit1 * digit2 + carry
            carry = product[i + j + 1] // 10
            product[i + j + 1] %= 10
        
        # handling any remaining carry
        nextIdx=i
        while carry:
            product[nextIdx] += carry
            carry = product[nextIdx] // 10
            product[nextIdx] %= 10
            nextIdx -= 1
        
    res=''.join(str(x) for x in product)

    # Removing leading zeros
    zeroes=0
    while zeroes<len(res) and res[zeroes]=="0":
        zeroes+=1
    res=res[zeroes:]

    if negative:
        res="-"+res
    return res if res else "0"

print(multiply_strings(s1, s2))  # Output: "66"
