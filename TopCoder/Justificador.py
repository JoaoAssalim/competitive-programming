n1 = True
while True:
    n = int(input())


    if n == 0:
        break
    else:
        if n1 == False and n:
            print()
        lista = []
        len_lista = []
        for i in range(n):
            nome = input()
            lista.append(nome)

        for i in lista:
            len_lista.append(len(i))

        maximo = max(len_lista)

        for x in lista:
            if len(x) == maximo:
                print(x)
            else:
                sep = maximo - len(x)
                space = ' '
                print(f'{space*sep}{x}')
        if n1:
            n1 = False