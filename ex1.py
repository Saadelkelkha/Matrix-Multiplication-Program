a = []
b = []
c = []

for i in range(3):
    l = []
    for j in range(4):
        n = int(input("Enter number: "))
        l.append(n)
    a.append(l)

for i in range(4): 
    l = []
    for j in range(2):
        n = int(input("Enter number: "))
        l.append(n)
    b.append(l)

for i in range(3):
    for j in range(2):
        l=[]
        p = 0
        for f in range(4):  
            p += a[i][f] * b[f][j]
        l.append(p)
        c.append(l)

print(c)