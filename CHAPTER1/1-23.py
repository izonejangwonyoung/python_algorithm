#오른쪽 아래가 직각인 이등변 삼각형으로 * print

n=int(input("변의 길이를 설정하세요:"))

for i in range(0, n):
    for _ in range(n-i):
        print(' ', end='')
    for _ in range(i+1):
        print('*', end='')
    print('')