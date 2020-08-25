## 1부터 n까지 정수의 합 구하기(for문) -일때 오류 뿜지 않는 프로그램



print("\n'1부터 n까지 정수의 합 구하기'를 시작합니다.")
n=int(input('n값을 입력하세요:'))

while True:
    n=int(input('n값을 입력하세요:'))
    if n>0:
        break


sum=0

for i in range(n):
    sum +=i
    i+=1


print("1부터",n,"까지의 합은",sum,"입니다.")