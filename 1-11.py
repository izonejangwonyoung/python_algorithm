print("정수 a와 b의 값을 입력해 주세요")
a=int(input("정수 a를 입력해주세요:"))
b=int(input("정수 b를 입력해주세요:"))
if a>b:
    a,b=b,a
sum=0
for i in range(a,b):
    print(i,'+',end='')
    sum+=i


print(b,'=',end='')
sum+=b

print(sum)