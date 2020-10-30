# break문 예제
# 무한루프에서 hello World 다섯번 찍기
i = 0;
while 1:
    if i == 5:
        break     # break가 써진 곳의 가장 가까운 반복문에서 빠져나온다.
    
    print("Hello World!! %d" % i)
    i += 1

print("=" * 50)


# continue문 예제

# 1~10까지의 수 중에서 4의 배수일 때는 숫자를 출력하지 않기 

# 1. if-else문으로 처리
for i in range(1, 11):
    if i % 4 == 0:
        pass
    else:
        print(i, end = " ")

# 2. continue문 사용

for i in range(1, 11):

    if i % 4 == 0:
        continue   # 아래 코드들을 수행하지 않고 continue가 써진 가장 가까운 반복문 조건을 다시 본다.
    
    print(i, end = " ")

