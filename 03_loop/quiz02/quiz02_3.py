for i in range(1, 51):  # 1 ~ 50, 1씩 증가
    if i % 3 == 0:   # i를 3으로 나누어 떨어지면 3의 배수
        print(i, end=" ")

# 다른 방법
for i in range(3, 51, 3): # 3 ~ 50, 3씩 증가
    print(i, end=" ")
