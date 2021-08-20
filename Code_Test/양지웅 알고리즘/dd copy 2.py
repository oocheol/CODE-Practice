#값 입력
N = int(input())
array = []
for i in range(N): #1
    start, end = map(int, input().split())
    array.append((start,end))

#시작 시간으로 sort 1번하고, 종료 시간으로 sort한다.
#예제는 시작 시간과 종료 시간으로 sort를 한 결과의 예제이다.
array = sorted(array, key=lambda a:a[0]) #2
array = sorted(array, key=lambda a:a[1]) #3

#알고리즘
end_time = 0
count = 0
for i in array: #4
    if i[0] >= end_time: #5
        end_time = i[1] #6
        count += 1 #7
print(count)
#1 : N개에 따라 입력을 받는데, 시작 시간과 종료 시간 변수를 두어 입력을 받은다음 합친다.

#2 : 시작 시간 기준으로 정렬한다.

#3 : 종료 시간 기준으로 정렬한다.

#4 : array에서 i 반복하는데,

#5 : 첫 시작을 0 기준으로 조건문을 만든다. 문제에서 시작 시간과 종료 시간이 같은 것도 있다했기 때문에 >= 표시를 한다.

#6 : i[0]이 end_time보다 크거나 같다면 end_time이 i[1]이 되고,

#7 : 회의 수는 count가 1이 증가 되어 결국 이 count를 출력한다.