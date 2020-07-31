#a부터 b까지 정수의 합 구하고 과정,최종값 모두 출력하기


import time



print("a부터 b까지 정수의 합을 구하는 프로그램을 시동중입니다....")

print("로딩중...")
time.sleep(1)
print("30% 완료")
time.sleep(4)
print("72% 완료")
time.sleep(2)
print("97% 완료")
time.sleep(2)
print("잠시만 기다려 주세요...")
time.sleep(5)
print("정수 a와 b의 값을 입력해 주세요")
a=int(input("정수 a를 입력해주세요:"))
b=int(input("정수 b를 입력해주세요:"))
if a>b:
    a,b=b,a
sum=0
for i in range(a,b+1):
    if i<b:
        print(i,'+',end='')

    else:
        print(i,'=',end='')


    sum += i



print(sum)
