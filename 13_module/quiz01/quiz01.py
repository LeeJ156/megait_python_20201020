import random

lotto = list()

while(len(lotto) < 6):
    num = random.randrange(1, 46)  # 1 ~ 45
    if num in lotto:  # 중복된 번호가 나오면
        continue  # 아래 내용 수행하지 않고 조건문 검사를 다시함

    lotto.append(num)

print(lotto)
