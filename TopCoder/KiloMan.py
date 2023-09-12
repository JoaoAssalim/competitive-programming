for i in range(int(input())):
    tiros = int(input())
    acertos = 0
    alt = list(map(int, input().split()))
    acao = input()
    
    for i in range(tiros):
        if alt[i] <= 2 and acao[i] == 'S' or alt[i] > 2 and acao[i] == 'J':
            acertos += 1
    print(acertos)