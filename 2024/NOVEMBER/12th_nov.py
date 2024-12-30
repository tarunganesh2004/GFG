# Meeting rooms
# https://www.geeksforgeeks.org/problems/attend-all-meetings/1

l=[[1,4],[10,15],[7,10]]

def isPossible(l):
    l.sort(key =lambda x:x[0])

    for i in range(1,len(l)):
        if l[i][0]<l[i-1][1]:
            return False
    return True

print(isPossible(l)) # True