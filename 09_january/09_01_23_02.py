a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a%2==0 and b%2==0) or (a%2==1 and b%2==1):
    k="ч"
else:
    k="б"
if (c%2==0 and d%2==0) or (c%2==1 and d%2==1):
    v="ч"
else:
    v="б"
if v==k:
    print("YES")
else:
    print("NO")
    
