numbers = [3, 8, 9, 4, 2, 1, 7, 5]

# 1. 값 접근: List의 4번째 값을 6으로 바꾸고 전체를 출력
numbers[3] = 4
print(numbers, end=" ")

print()
print("=" * 50)

# 2. List 값 중 가장 큰 값 출력
max = numbers[0]
for number in numbers:
    if number > max:
        max = number

print("가장 큰 값은 %d입니다." % max)

print("=" * 50)

# 3. List의 모든 수 합계
sum = 0
for number in numbers:
    sum += number

print("합은 %d입니다." % sum) 
