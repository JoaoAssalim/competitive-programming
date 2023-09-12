for i in range(int(input())):
    s = input().split()
    for i in range(len(s)):
        s[i] = [len(s[i]), len(s)-i, s[i]]
    s.sort(reverse=True)
    l = []
    for i in s:
        l.append(i[-1])
    print(' '.join(l))