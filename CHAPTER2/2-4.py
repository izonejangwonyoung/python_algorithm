#배열 원소의 최댓값을 구해서 출력하기(원솟값을 난수로 생성)


import random

from max import max_of


print('난수의 최댓값을 구합니다.')
num=int(input("난수의 개수를 입력하세요.:"))
min_padding=int(input("난수의 최솟값를 입력하세요:"))
max_padding=int(input("난수의 최댓값를 입력하세요:"))

x=[None]*num



for i in range(num):
    x[i]=random.randint(min_padding,max_padding)
    
    
print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_of(x)}입니다')

