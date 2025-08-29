# Smallest Window Containing All Characters

s="timetopractice"
p="toc"

def smallestWindow(s,p):
    from collections import Counter 

    need=Counter(p)
    need_count=len(need) # no of distinct characters we need
    have=0
    window={}

    res=[-1,-1]
    res_len=float("inf")
    left=0
    
    for right,ch in enumerate(s):
        window[ch]=window.get(ch,0)+1

        if ch in need and window[ch]==need[ch]:
            have+=1

        # shrink from left if valid
        while have==need_count:
            if (right-left+1)<res_len:
                res=[left,right]
                res_len=right-left+1

            window[s[left]]-=1
            if window[s[left]]<need[s[left]]:
                have-=1
            left+=1
    i,j=res
    return s[i:j+1] if res_len!=float("inf") else ""

print(smallestWindow(s,p))
