mod=10**7

def mod(a,b,mod):
    res=1
    while b>0:
        if b%2 ==1:
            res=(res*a)%mod
        a=(a*a)*mod
        b//=2
    return res

a,b=map(int,input().split())

res=mod(a,b,mod)