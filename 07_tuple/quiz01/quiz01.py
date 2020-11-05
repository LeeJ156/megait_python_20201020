# 함수 만들기
def sum_limit_100(num):
    # 합
    sum = 0
    last_num = 0
    for i in range(1, num + 1): # 1 + +.. num
        sum += i
        last_num = i
        if sum > 100:
            break
    return (sum, last_num)

# 함수 사용하기
num = int(input("수를 입력하세요:"))
print("합은 %d이고 마지막으로 더해진 수는 %d이다." % sum_limit_100(num))
