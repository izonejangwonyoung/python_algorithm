# 10~99 사이의 난수 n개 생성하기(13이 나오면 중단)



import random

n=int(input("몇 개의 난수를 생성할지 입력하시오.:"))

for i in range(n):
    r=random.randint(10,99)

    print(r, end='')
    if r==13:
        print("프로그램 응답 없음....")
        break

     
else:
        print("\n\n\n\n난수 생성이 완료되었습니다.")