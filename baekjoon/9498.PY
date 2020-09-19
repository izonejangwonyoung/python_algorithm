# 문제
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 시험 성적을 출력한다.

# 예제 입력 1 
# 100
# 예제 출력 1 
# A
# 출처
# 문제를 만든 사람: baekjoon
# 알고리즘 분류
# 보기

def grade():
    score=int(input())
    
    if 90<=score<=100:
        print('A')

    elif 80<=score<=89:
        print('B')

    elif 70<=score<=79:
        print('C')
    
    elif 60<=score<=69:
        print('D')
    
    else:
        print('F')
    
    return grade


grade()




# 안녕하세요.

# 구구단 ~ 2 X 9 = 18 은 multi_table() 함수안에 있는 print 문을 통해서 출력이 된 것입니다.

# None 은 print(multi_table(num)) 구문에서, multi_table() 함수의 리턴값이 print 문에 의해 출력이 된 것인데요.

# 해당 함수의 리턴값을 정해놓지 않앗기 때문에, None이 출력된 것이예요.

# 해당 함수에서의 출력만 해보시려 하신 듯 한데, 그렇다면, print 문 없이 다음과 같이만 작성하시면 될 것 같습니다.

# num = int(input())

# multi_table(num)

# 감사합니다.