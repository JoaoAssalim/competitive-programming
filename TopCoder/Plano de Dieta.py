alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(int(input())):
    trap = 0
    letras = set()
    for i in range(3):
        l = input()
        
        if i == 0:
            for y in l:
                letras.add(y)
        else:
            for y in l:
                if y not in letras:
                    trap += 1
                else:
                    letras.remove(y)
    letras = list(letras)
    letras.sort()
    nova = ''
    for i in letras:
        nova += i
    
    if trap == 0:
        print(nova)
    else:
        print('CHEATER')
