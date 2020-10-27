n = int(input("입력: "))
n2 = n

# 1234 / 1000  => 1.234
print(int(n / 1000))
# 1234 % 1000  => 234
n = int(n % 1000)

# 234 / 100 => 2.34
print(int(n / 100))
# 234 % 100 => 34
n = int(n % 100)

# 34 / 10  => 3.4
print(int(n / 10))
# 34 % 10  => 4
n = int(n % 10)
print(n)


# 다른 방법
print("=" * 50)

q, r = divmod(n2, 1000)
print(q)
q, r = divmod(r, 100)
print(q)
q, r = divmod(r, 10)
print(q)
print(r)
