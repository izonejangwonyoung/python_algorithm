#세 정수의 중간값 구하기
def med3(a,b,c):
    if a>=b:
        if b>=c:
            return b

        elif c>=a:
            return a

        else:
            return c

    elif a>c:
        return a
    elif b>c:
        return c

    else:
        return b



print("제시된 라인에 중간값을 구할 세 정수를 입력하세요")
a=int(input("정수 a의 값을 입력하세요:"))
b=int(input("정수 b의 값을 입력하세요:"))
c=int(input("정수 c의 값을 입력하세요:"))

print("입력하신 정수들의 중간값은",med3(a,b,c),"입니다.")