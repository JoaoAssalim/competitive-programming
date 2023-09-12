alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(int(input())):
    h = 0
    L = int(input())
    
    for i in range(L):
        letra = input()
        for l in range(len(letra)):
            h += (alfabeto.index(letra[l]) + i + l)
    print(h)
    