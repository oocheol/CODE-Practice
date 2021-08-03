#약수구하기

x = []
n = int(input("숫자입력 : "))

for i in range(1,n+1) :
    if n % i == 0 :
        x.append(i)
    
print(x)