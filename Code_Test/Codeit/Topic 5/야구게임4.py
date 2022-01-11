from random import randint


def generate_numbers():
    numbers = []

    while True :
        numbers.append(randint(0,9))
        if len(set(numbers)) == 3:
            numbers = list(set(numbers))
            break

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers



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



def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for user, com in zip(guesses, solution):
        if user == com:
            strike_count += 1
    
    for user in guesses:
        for com in solution:
            if user == com:
                ball_count += 1
    
    ball_count = ball_count - strike_count
        

    return strike_count, ball_count



# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True :
    tries += 1
    guesses = take_guess()
    strike, ball = get_score(guesses, ANSWER)
    print(f"{strike}S {ball}B")

    if get_score(guesses, ANSWER) == (3,0) :
        break

    


print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
