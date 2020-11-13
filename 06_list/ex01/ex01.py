# 리스트 값 초기화(숫자)
numbers = [89, 98, 83, 70]
print(numbers)

print("=" * 50)

# 리스트 값 초기화(문자)
chars = ['a', 'b', 'c']
print(chars)

print("=" * 50)

# range 함수로 리스트 값 초기화
rlist = list(range(10))
print(rlist)

print("=" * 50)

# 리스트 값 동적으로 저장하기(list(), append())
animals = list()
animals.append("사자")
animals.append("고양이")
animals.append("개")
print(animals)

print("=" * 50)

# 요소값 출력
# 몇번째인지의 숫자를 index라고 한다.
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])

print("=" * 50)

# 2번째 요소값 변경하기
numbers[1] = 45
print(numbers)

print("=" * 50)

# 없는 요소값에 변경해보기(error)
# numbers[4] = 60

# 반복문으로 출력하기(index)
for i in range(len(numbers)):
    print(numbers[i])

print("=" * 50)

# 반복문으로 출력하기(값 자체)
for num in numbers:
    print(num)
