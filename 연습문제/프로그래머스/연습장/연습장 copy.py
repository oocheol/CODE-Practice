new_id = 'a'


if len(new_id) <= 2 :
    n = 0
    while len(new_id) < 3 :
        new_id = new_id + new_id[-1]
        print(len(new_id))
        n += 1
print(new_id)

