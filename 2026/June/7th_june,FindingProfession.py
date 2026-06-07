# # Finding Profession

# Consider a special family of Engineers and Doctors with following rules :

# Everybody has two children.
# First child of an Engineer is an Engineer and second child is a Doctor.
# First child of an Doctor is Doctor and second child is an Engineer.
# All generations of Doctors and Engineers start with Engineer.

def profession(level,pos):
    if level==1:
        return "Engineer"
    
    parent=profession(level-1,(pos+1)//2)

    if pos%2==1: # left
        return parent 
    
    # right child(opposite)
    if parent=="Engineer":
        return "Doctor"
    else:
        return "Engineer"
    
# optimized
# Engineer = 0
# Doctor   = 1

# Then:

# Left child  -> same
# Right child -> flip

# Whenever we take a right move, profession changes.

# So we only need to count how many times we take a right child while moving from node to root.
def optimized(level,pos):
    flips=bin(pos-1).count("1")
    return "Doctor" if flips%2 else "Engineer"
    
level=4
pos=2
print(profession(level,pos))