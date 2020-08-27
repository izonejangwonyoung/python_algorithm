#왼쪽 아래가 직각인 이등변 삼각형으로 * 출력하기



n=int(input("왼쪽 아래 변의 길이를 입력하세요"))



for i in range(1,n+1):
    for j in range(i):
        print("*",end='')

    print()