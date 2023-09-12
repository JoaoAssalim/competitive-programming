A,B,C = list(map(int, input().split()))
x = []
y = []

for i in range(B):
    n = int(input())
    x.append(n)

for i in range(C):
    n = int(input())
    y.append(n)

c = C

idx = 0
idy = 0
while True:
    if x[idx] <= A:
        c += 1
        A -= x[idx]
        idx += 1
    else:
        if idy < C:
            A += y[idy]
            idy += 1
        else:
            break
    
    if idx == B:
        break

print(c)