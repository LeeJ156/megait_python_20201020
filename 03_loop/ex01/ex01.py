print("안녕하세요")
print("안녕하세요")
print("안녕하세요")

print("=" * 50)

i = 0 # 카운팅을 하기 위한 변수
while i < 3:  # 참일 때 수행된다.    0  1  2  3
    print("안녕하세요 i: %d" % i)
    i = i + 1
    i += 1  # 복합 대입 연산자

# 5번 출력하기: 0 ~ 4      0 1 2 3 4
i = 0
while i < 5:
    print("Hello world i: %d" % i)
    i += 1

# 5번 출력하기: 1 ~ 5      1 2 3 4 5
i = 1
while i <= 5:
    print("안녕하세요 i:%d" % i)
    i += 1

# 5번 출력하기: 5 1       5 4 3 2 1
i = 5
while i >= 1:  # i > 0
    print("Hello world %d" % i)
    i -= 1

# 합계 구하기 1 2 3 4 5 6 7 8 9 10
sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1

print(sum)

# 무한루프
# 1. i의 증감값을 변화시키지 않는 경우
# i = 0
# while i < 3:
#     print("Hello")

while 1:   # 0: 거짓 0아닌 수: 참
    print("무한루프")
