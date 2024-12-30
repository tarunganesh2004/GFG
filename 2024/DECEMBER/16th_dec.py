# k-th element of two arrays

a=[2, 3, 6, 7, 9]
b=[1, 4, 8, 10]
k=5

def kthElement(a,b,k):
    return sorted(a+b)[k-1]