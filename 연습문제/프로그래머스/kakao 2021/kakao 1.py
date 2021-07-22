# 카카오 2021 신입공채 1번문제

# lower : 대문자 > 소문자 치환
# upper : 소문자 > 대문자 치환
# isalnum() : 문자열이 알파벳과 숫자로만 
#             이루어졌으면 True, 그렇지 않으면 False

#id = list(input())

id1 = "...!@BaT#*..y.abcdefghijklm"
id2 = "z-+.^."
id3 = "=.="
id4 = "123_.def"
id5 = "abcdefghijklmn.p"

def solution(input_id):
    temp_id = []
    # 1,2 단계
    for s in input_id :
        if s.isalnum() :  # 알파벳 & 숫자판별
            temp_id.append(s.lower())
        elif s == '-' or s == '_' or s == '.':
            temp_id.append(s.lower())
    new_id = ''.join(temp_id)
    
    # 3단계
    for x in range(len(temp_id)+1,0,-1) :
        new_id = new_id.replace("."*x,".")
    
    # 4단계
    if len(new_id) > 0 :
        if new_id[0] == "." or new_id[-1] == "." :
            new_id = new_id.strip('.')
        
        if len(new_id) == 0 :
            new_id = 'a' 
    
    if len(new_id) == 0 :
        new_id = 'a'    

    # 6단계
    if len(new_id) >= 16 :
        new_id = new_id[:15]

        if new_id[-1] == "." :
            new_id = new_id.strip('.')
             
    # 7단계
    if len(new_id) <= 2 :
        while len(new_id) < 3 :
            new_id = new_id + new_id[-1]


    return new_id

print(solution(id1))
print(solution(id2))
print(solution(id3))
print(solution(id4))
print(solution(id5))