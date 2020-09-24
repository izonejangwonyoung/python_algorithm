
# 문제

# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
# 입력

# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
# 출력

# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
# 예제 입력 1

# 110

# 예제 출력 1

# 99


import sys
def find_hansu():

    N=int(sys.stdin.readline())
    cnt=0
    for i in range(1,N+1):
        if i<=99:
            cnt+=1

        else:
            list1=list(map(int,str(i)))
            if list1[0]-list1[1] ==  list1[1] -list1[2]  :
                cnt+=1

    print(cnt)


find_hansu()



# num = int(input())
# hansu = 0

# for n in range(1, num+1) :
#     if n <= 99 : # 1부터 99까지는 모두 한수
#         hansu += 1 
    
#     else :     
#         nums = list(map(int, str(n))) # 숫자를 자릿수대로 분리 
#         if nums[0] - nums[1] == nums[1] - nums[2] : #등차수열 확인
#             hansu+=1


