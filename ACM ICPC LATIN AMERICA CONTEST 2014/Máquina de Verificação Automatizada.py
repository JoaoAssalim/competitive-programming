a = list(map(int, input().split()))
b = list(map(int, input().split()))
ver = True
for i in range(5):
    if a[i] == b[i]:
        ver = False
        break

if ver:
    print("Y")
else:
    print("N")