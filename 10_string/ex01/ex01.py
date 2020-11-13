# 1. 문자열 더하기
a = "I like"
b = " Python"
c = a + b
print(c)

# 2. 문자열 곱하기
print(b * 3)
print("=" * 50)

# 3. 문자열 길이 구하기
print(len(c))

# 4. 문자열 index
print(c[0])
print(c[-1])

# 5. 문자열 index로 값 넣기 시도
str = "abc"
#str[3] = 'd'   => 안된다!!!


# 6. 문자열 슬라이싱
# like만 뽑아내기
# [시작인덱스:원하는 인덱스 + 1]
# idx >= 2  idx < 6: 2~5
print(c[2:6])

# Python만 뽑아내기
# [시작인덱스:끝까지]
print(c[7:])

# 7. 특정 문자 개수 세기
print("i의 개수는", c.count('i'))

# 8. 찾는 문자의 첫 번째 index 1
print("y의 index는", c.find('y'))
print("y의 index는", c.find('a'))  # 없는 문자를 찾는 경우 -1

# 9. 찾는 문자의 첫 번째 index 2
print("y의 index는", c.index('y'))
#print("y의 index는", c.index('a'))  # 없는 문자를 찾는 경우 오류

# 10. 문자열 치환
# I like Python => You like Python
c = c.replace("I", "You")   # 변수에 꼭 다시 저장을 해주어야 한다
print(c)

# 11. 문자열 나누기
words = c.split()  # 파라미터를 넣지 않으면 기본으로 공백 기준으로 문자열 자름
print(words) # 잘린 문자들은 각각의 String List가 된다.

fruits = "grape, apple, orange, peach"
fruit_list = fruits.split(",")
print(fruit_list)


# 12. 문자 입력받기

#a, b = input("2개의 단어를 입력하세요: ").split()
#print(a, b)

# 리스트로 받기
words = input("2개의 단어를 입력하세요: ").split()
print(words)
