from max import max_of


print("배열의 최댓값을 구하는 프로그램을 시작합니다.")
print("**** 주의: '종료' 를 입력할 시 프로그램이 종료됩니다. ****")

number=0
x=[]

while True:
    s=input(f'x[{number}]값을 입력하십쇼')
    if s=='종료':
        break

    x.append(int(s))
    number += 1


print(f'{number}개의 값을 입력하셨습니다.')
print(f'최댓값은 {max_of(x)}입니다.')