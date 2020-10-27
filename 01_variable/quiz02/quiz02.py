# 1. 실수 연산
number1 = 33
number2 = 35.325

print("두 수의 곱은 %f 입니다." % (number1 * number2))

# 2. 날짜 구하기
hour = 943
day = hour / 24

print("%d시간은 %d일 입니다." % (hour, day))

# 3. 도형 넓이 구하기
width = 8
height = 9
rectangle = width * height
triangle = width * height / 2

print("사각형의 넓이: %d" % rectangle)
print("삼각형의 넓이: %d" % triangle)

# 4. 평균 구하기

korean = 93
math = 88
english = 94
average = (korean + math + english) / 3

print("국어 %d점, 수학 %d점, 영어 %d점" % (korean, math, english))
print("평균 %.2f 점 입니다." % average)

# 5. 화씨 구하기
c = 31
f = 9 / 5 * c + 32

# %g는 소수에서 0을 없앤다.
print("섭씨 %d도는 화씨 %g도 입니다." % (c, f))
