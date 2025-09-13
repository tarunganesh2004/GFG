# Assign Mice Holes

mices=[4,-4,2]
holes=[4,0,5]

def assignHole(mices,holes):
    mices.sort()
    holes.sort()
    max_time=0
    for i in range(len(mices)):
        max_time=max(max_time,abs(mices[i]-holes[i]))
    return max_time

print(assignHole(mices,holes))