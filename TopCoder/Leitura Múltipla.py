while True:
    try:
        letras = input()
        max = int(input())
        read = letras.split('W')
        total = letras.count('W')
        
        for i in read:
            if len(i) <= max and len(i) > 0:
                total += 1
            else:
                comp = len(i)
                tot = comp // max
                comp -= tot*max
                
                total += tot
                if comp > 0:
                    total += 1
                 
        print(total)
    except EOFError:
        break