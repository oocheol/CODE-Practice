def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    count = 1

    while True:
        num = int(input(f"{count}번째 숫자를 입력하세요:"))
        if num > 10 :
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        
        elif num in new_guess :
            print("중복되는 숫자입니다. 다시 입력하세요.")
            continue
        
        new_guess.append(num)
        count += 1
        
        if len(new_guess) == 3:
            break
        

    return new_guess

print(take_guess())