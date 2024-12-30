# KMP Algorithm

def KMPSearch(pat,txt):
    ind=[]
    for i in range(len(txt)-len(pat)+1):
        if txt[i:i+len(pat)]==pat:
            ind.append(i)
    return ind

txt="abcab"
pat="ab"

print(KMPSearch(pat,txt))