l = []
s = input()

n = s[0]
for i in s[1:]:
    t = n+i
    if int(t) <= 10:
        n += i
    else:
        l.append(int(t[:-1]))
        n = t[-1]

if len(n) > 0:
    l.append(int(n))
print(f'{sum(l)/len(l):.2f}')