a = [None, 2, 3, 4, 5, 6]
print(a)

new = []
idx = 0
for x in a:
    if str(x) != 'None':
        new.append(x)
        idx += 1

print(new)
print(idx)