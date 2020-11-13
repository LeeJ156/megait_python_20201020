num = int(input("수를 입력하세요: "))

is_prime = True
if num != 2:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("소수입니다.")
else:
    print("소수가 아닙니다.")
