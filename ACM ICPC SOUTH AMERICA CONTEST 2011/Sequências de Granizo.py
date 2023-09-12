while True:
    n = int(input())
    if n == 0:
        break

    qt = n
    while n != 1:
        if n % 2 == 0:
            n  =1/2 * n
        else:
            n = 3 * n + 1
        
        if n > qt:
            qt = n
    print(int(qt))