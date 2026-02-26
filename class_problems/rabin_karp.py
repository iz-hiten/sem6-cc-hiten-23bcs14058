def rabin_karp(txt, pat):
    n=len(txt)
    m=len(pat)
    if m>n:
        return []
    
    d=256
    q=10**9+7
    
    h=1
    for _ in range(m-1):
        h=(h*d)%q
    
    p=0
    t=0
    for i in range(m):
        p=(d*p+ord(pat[i]))%q
        t=(d*t+ord(txt[i]))%q
    
    res=[]
    for i in range(n-m+1):
        if p==t:
            if txt[i:i+m]==pat:
                res.append(i)
        
        if i<n-m:
            t=(d*(t-ord(txt[i])*h)+ord(txt[i+m]))%q
            if t<0:
                t+=q
    
    return res

txt="nwjfnwofnoacd"
pat="acd"
print(rabin_karp(txt,pat))
