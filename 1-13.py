print("+-를 번갈아 출력하는 프로그램을 시작합니다.")
n = int(input("몇 번 출력할까요?:"))

for i in range(n//2):
    print("+-", end='')

if i%2:
    print('+', end='')