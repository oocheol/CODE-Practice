import random

i = 4
num = random.randint(1, 20)
while True :
    guess = int(input(f"기회가 {i}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
    if num == guess :
        print(f"축하합니다. {5-i}번 만에 숫자를 맞히셨습니다.")
        break
    elif num < guess :
        print("Down")
        i -= 1
    elif num > guess :
        print("Up")
        i -= 1
    if i == 0 :
        print(f"아쉽습니다. 정답은 {num}이었습니다.")
        break