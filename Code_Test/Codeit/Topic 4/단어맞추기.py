with open("vocabulary.txt", "r", encoding="utf-8") as f :
    for word in f :
        question = word.split(": ")[1].strip()
        answer = word.split(": ")[0].strip()
        guess = input(f"{question}: ")
        
        if guess == answer :
            print("맞았습니다!\n")
        else :
            print(f"아쉽습니다. 정답은 {answer}입니다.\n")
