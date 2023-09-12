for i in range(int(input())):
    a,b = list(map(str, input().split()))
    nova = ''
    
    if len(a) == len(b):
        for i in range(len(a)):
            nova += f'{a[i]}{b[i]}'
    else:
        for i in range(min(len(a), len(b))):
            nova += f'{a[i]}{b[i]}'
        if len(a) < len(b):
            nova += b[min(len(a), len(b)):]
        else:
            nova += a[min(len(a), len(b)):]
    print(nova)