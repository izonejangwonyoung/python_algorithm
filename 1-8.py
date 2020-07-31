# 1부터 n까지 정수의 합 구하기(for문)



print("\n'1부터 n까지 정수의 합 구하기'를 시작합니다.")
n=int(input('n값을 입력하세요:'))

sum=0
for i in range(1,n+1):
    sum += i


print('1부터',n,'까지 정수의 합은',sum,'입니다.')
