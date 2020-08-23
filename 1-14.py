print("*를 n개 출력하되 w개마다 줄바꿈하기")
n=int(input("*를 몇 개 출력할까요?:"))
w=int(input('몇 개마다 줄바꿈할까요?:'))

for i in range(n):


    if i%w==1:
        print("*", end='')
        print('')

    else:
        print("*", end='')

