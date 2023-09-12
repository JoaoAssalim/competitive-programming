while True:
    try:
        num = input().split('.')
        cut = input().split('.')
        if num[0] == '':
            num[0] = '0'
        if len(num) == 1:
            num.append('0')
        if num[1] == '':
            num[1] = '0'
        if cut[0] == '':
            cut[0] = '0'
        if cut[1] == '':
            cut[1] = '0'

        if float(f'0.{num[1]}') >= float(f'0.{cut[1]}'):
            print(int(num[0]) + 1)
        else:
            print(int(num[0]))
        
        
    except EOFError:
        break