from math import floor
while True:
    try:
        s = input().split()
        tam, qt = 0, 0
        for i in s:
            if not any(dig.isdigit() for dig in i):
                if i.count('.') == 1:
                    if i[-1] == '.' and len(i) > 1:
                        tam += len(i)-1
                        qt += 1
                elif i.count('.') == 0:
                    tam += len(i)
                    qt += 1
        if qt > 0:
            qt = int(floor(tam/qt))
            if qt <= 3:
                print(250)
            elif qt <= 5:
                print(500)
            else:
                print(1000)
        else:
            print(250)

        
    except EOFError:
        break