# Remove duplicates in array

l=[2,2,3,3,7,5]

def remove(l):
    insert_idx=0
    for i in range(len(l)):
        if l[i] not in l[:insert_idx]:
            l[insert_idx]=l[i]
            insert_idx+=1
    del l[insert_idx:]
    return l # TC O(n) SC O(1)


def remove1(l):
    # using set
    # return list(set(l)) # TC O(n) SC O(n) (output may be wrong as set is unordered)
    r=[]
    s=set()
    for i in l:
        if i not in s:
            r.append(i)
            s.add(i)
    return r # TC O(n) SC O(n)

def remove2(l):
    # using map
    m={}
    for i in l:
        m[i]=1
    return list(m.keys()) # TC O(nlogn) SC O(n)

def remove3(l):
    # using two pointers
    # l.sort()
    i=0
    for j in range(1,len(l)):
        if l[i]!=l[j]:
            i+=1
            l[i]=l[j]
    return l[:i+1]

print(remove(l))
print(remove1(l))
print(remove2(l))
print(remove3(l))