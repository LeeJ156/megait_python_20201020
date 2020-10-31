# 바깥쪽 반복문: 2단 ~ 9단
# 안쪽 반복문: 곱해지는 숫자 1 ~ 9

for i in range(2, 10):  # 2 ~ 9
    for j in range(1, 10):  # 1 ~ 9
        print("%d X %d = %d" % (i, j, i*j))
