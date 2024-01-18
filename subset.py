def issubset1(a1,a2):
    if a2.issubset(a1):
        print("Yes")
    else: 
        print("No")

a1 = set(map(int, input().split()))
a2 = set(map(int, input().split()))
issubset1(a1,a2)