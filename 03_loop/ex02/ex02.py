# 0 ~ 4 : 5번
# i >= 0 and i < 5
for i in range(5): # 1개의 값을 넣는 것은 n번 돌리겠다는 의미
    print("Hello world i: %d" % i)

# 1 ~ 5 : 5번    1 2 3 4 5
# i >= 1 and i < 6
for i in range(1, 6): # 시작값, 끝값 + 1
    print("안녕하세요 i: %d" % i)

# 1 ~ 5 : 5번    1 2 3 4 5 / 6
# i >= 1 and i < 6
for i in range(1, 6, 2): # 시작값, 끝값 + 1, n만큼 증감 시키겠다.
    print("%d" % i)

# 5 ~ 1 : 5번   5 4 3 2 1 / 0
# i <= 5 and i > 0
for i in range(5, 0, -1):
    print("안녕하세요 i:%d" % i)
