#1000 이하의 소수를 나열하기


import time
print('1000 이하의 소수를 나열하는 프로그램을 시작합니다.')
time.sleep(1)
print('')



counter=0
for n in range(2,1001):
    for i in range(2,n):
        counter +=1
        if n % i ==0:
            break
        
        else:
            print(n)
        
print(f'나눗셈을 실행한 횟수:{counter}')