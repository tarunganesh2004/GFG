# Last Digit of a^b 

a="3"
b="10"

# brute force is to convert to int and directly use a**b 

def getLastDigit(a,b):
    if b=='0':
        return 1
    cycles={
        0:[0],
        1:[1],
        2:[2,4,8,6],
        3:[3,9,7,1],
        4:[4,6],
        5:[5],
        6:[6],
        7:[7,9,3,1],
        8:[8,4,2,6],
        9:[9,1]
    }
    last=int(a[-1])
    cycle=cycles[last]

    m=len(cycle) # length of cycle
    # now last digit^b , now for each m, this repeats so b%m 
    rem=0
    for ch in b:
        rem=(rem*10+int(ch))%m 
    
    # if rem is 0, return last element
    if rem==0:
        return cycle[-1]
    
    # rem=1-> cycle[0], rem=2-> cycle[1]
    return cycle[rem-1]

print(getLastDigit(a,b))