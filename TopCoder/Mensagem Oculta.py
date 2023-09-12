for i in range(int(input())):
    nova = ''
    frase = list(map(str, input().split()))
    
    for i in frase:
        if i != "":
            nova += i[0]
    print(nova)
    