for i in range(int(input())):
    n = int(input())
    alunos = input().split()
    presenca = input().split()
    
    f,p = 0,0
    rep = []
    for i in range(n):
        f = presenca[i].count('A')
        p = presenca[i].count('P')
        media = p/(f+p) * 100
        if media < 75:
            rep.append(alunos[i])
    print(" ".join(rep))