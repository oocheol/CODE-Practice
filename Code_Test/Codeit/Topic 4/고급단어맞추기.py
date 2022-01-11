import random

dictionary = {}
with open("vocabulary.txt", "r", encoding="utf-8") as f :
    for word in f :
        question = word.split(": ")[1].strip()
        answer = word.split(": ")[0].strip()
        dictionary[question] = answer
    


while True :
    rand = random.randint(0, len(list(dictionary.values()))-1)

    new_question = list(dictionary.keys())
    new_answer = list(dictionary.values())[rand]

    guess = input(f"{new_question[rand]}: ")

    if guess == new_answer :
        print("맞았습니다!\n")
    if guess == "q":
        break
    elif guess != new_answer:
        print(f"아쉽습니다. 정답은 {new_answer}입니다.\n")
