n = int(input())
a = list(map(int, input().split()))
a.append("0")
b = []
i = 0
for i in range(len(a)):
    a[i] = int(a[i])
    
for i in range(n):
    b.append(i + 1)
    b[i] = int(b[i])
a.sort()


for i in range(n):
    if b[i] != a[i]:
        c = b[i]
        
print(c)
