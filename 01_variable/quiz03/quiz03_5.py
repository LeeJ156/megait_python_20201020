n = int(input("입력: "))
sum = 0

q = n / 1000
r = n % 1000
sum += q

q = r / 100
r = r % 100
sum += q

q = r / 10
r = r % 10
sum += q
sum += r
print("합계는 %d 입니다." % sum)


# 다른 방법
sum = 0

q, r = divmod(n, 1000)
sum += q
q, r = divmod(r, 100)
sum += q
q, r = divmod(r, 10)
sum += q
sum += r
print("합계는 %d 입니다." % sum)
