while True:
    try:
        linha = input()
        b = 0
        i = 0
        nova = ''
        for y in linha:
            if y == '_':
                if i == 0:
                    i += 1
                    nova += '<i>'
                else:
                    nova += '</i>'
                    i = 0
            elif y == '*':
                if b == 0:
                    b += 1
                    nova += '<b>'
                else:
                    nova += '</b>'
                    b = 0
            else:
                nova += y
        
        print(nova)
    except EOFError:
        break