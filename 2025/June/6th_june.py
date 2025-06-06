# Search Pattern (Rabin-Karp Algorithm)



text="geeksforgeeks"
pattern="geek"

def rabin_karp_search(text, pattern):
    d=256
    q=101
    M = len(pattern)
    N = len(text)
    p = 0  # hash value for pattern
    t=0 # hash value for current window of text
    h=1 # higher order digit multiplier
    res=[]
    # precompute h= pow(d, M-1) % q
    for i in range(M-1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window of text
    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    # Slide the pattern over text one by one
    for i in range(N-M+1):
        # if has values match then check for characters one by one
        if p==t:
            match= True
            for j in range(M):
                if text[i+j] != pattern[j]:
                    match = False
                    break
            if match:
                res.append(i+1)
        # Calculate hash value for next window of text
        if i < N-M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            # We might get negative value of t, converting it to positive
            if t < 0:
                t += q
    return res

print(rabin_karp_search(text, pattern))  # Output: Pattern found at index 0