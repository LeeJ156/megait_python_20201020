# index로 접근하기
t0 = (1, )  # 값 하나 저장
print(t0)

t1 = (1, 2, 3)
print(t1[0])
print(t1[1])
print(t1[2])

# 값 변경 시도
#t1[0] = 100

# 튜플끼리 더하기
# 튜플 값이 변경된게 아니라 새로운 튜플이 만들어진 것이다.
t2 = ('a', 'b', 'c')
print(t1 + t2)

# 곱하기
print(t2 * 3)

# 길이 구하기
print(len(t2))

# 슬라이싱 하기
# t2의 값에서 'b', 'c'만 남기기
print(t2[1:])

# t2에서 'b'만 남기기
print(t2[1:2])

# divmod 사용하기

#q, r = divmod(100, 7)
(q, r) = divmod(100, 7)
print("몫은 %d이고 나머지는 %d이다." % (q, r))

result_tuple = divmod(100, 7)
print("몫은 %d이고 나머지는 %d이다." % result_tuple)
