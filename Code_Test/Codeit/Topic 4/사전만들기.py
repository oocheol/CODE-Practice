with open("vocabulary.txt", "a", encoding="utf-8") as f :
    while True :
        english = input("영어 단어를 입력하세요: ")
        if english == "q" :
            break
        else :
            f.write(english +": ")
        korean = input("한국어 뜻을 입력하세요: ") + "\n"
        if korean == "q" :
            break
        else :
            f.write(korean)