while True :
    s = input()

    if s == 'END' :
        break
    else :
        print(''.join(reversed(s)))