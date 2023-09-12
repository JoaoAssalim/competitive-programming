alfa = 'abcdefghijklmnopqrstuvwxyz'
while True:
    try:
        nova = ''
        texto = input()
        
        for i in texto:
            if i in alfa and i not in nova:
                nova += i
        nova = sorted(nova)
        rum = []
        if len(nova) > 0:
            #print(nova)
            stt = 0
            c = alfa.index(nova[0])
            id = alfa.index(nova[0])
            
            for i in range(1, len(nova)):
                if alfa.index(nova[i]) == id + 1:
                    id += 1
                else:
                    rum.append(f'{nova[stt]}:{nova[i-1]}')
                    stt = i
                    id = alfa.index(nova[i])
                    c = alfa.index(nova[i])
            rum.append(f'{alfa[c]}:{alfa[id]}')
            print(", ".join(rum))
        else:
            print()
    except EOFError:
        break