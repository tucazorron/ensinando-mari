n1, n2, n3, n4, n5 = map(int, input().split())
media = (n1 + n2 + n3 + n4 + n5) / 5
if media >= 5:
    print('Aprovado!')
    if media >= 9:
        print('SS')
    elif media >= 7:
        print('MS')
    else:
        print('MM')
else:
    print('Reprovado!')
    if media >= 3:
        print('MI')
    elif media >= 1:
        print('II')
    else:
        print('SR')
