
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 1 초	256 MB	90010	31437	27171	36.358%
# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

# import sys



# def plus_number():

    

#     while True:
#         a,b=list(map(int,sys.stdin.readline().split()))
#         try (0 < a,b < 10):
            
#             print(f'{a+b}')

#         except:
#             break


# plus_number()


while True:

    try:

        a,b = input().split()

        a = int(a)

        b = int(b)

        print(a+b)

    except:

       

        break










