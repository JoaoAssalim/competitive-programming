s = {1: ["*.", "..", ".."], 2: ["*.", "*.", ".."], 3: ["**", "..", ".."], 4: ["**", ".*", ".."], 5: ["*.", ".*", ".."], 6: ["**", "*.", ".."], 7: ["**", "**", ".."], 8: ["*.", "**", ".."], 9: [".*", "*.", ".."], 0: [".*", "**", ".."]}

while True:
    n = int(input())
    if n == 0:
        break
    op = input()
    
    if op == 'S':
        num = input()
        l = ''
        for i in range(3):
            for j in range(n):
                l += s[int(num[j])][i]
                if j < n-1:
                    l += " "
            l += "\n"
        print(l[:-1])
    else:
        a = input().split()
        b = input().split()
        c = input().split()
        
        l = ''
        for x in range(len(a)):
            for i in s:
                if s[i][0] == a[x] and s[i][1] == b[x] and s[i][2] == c[x]:
                    l += str(i)
        print(l)
        