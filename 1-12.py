print("+-를 번갈아 출력하는 프로그램을 시작합니다.")
n= int(input("몇 번 출력할까요?:"))

for i in range(0,n):
    if i%2:
        print("-", end='')

    else:
        print("+",end='')

