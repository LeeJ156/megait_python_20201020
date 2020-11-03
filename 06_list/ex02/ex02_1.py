print("### 1. 리스트끼리 더하기")
a = [1, 2, 3]
b = [5, 4, 3]
print(a + b)

print("### 2. 리스트 마지막에 요소 추가하기")
a.append(5)
a.append(4)
a.append(3)
print(a)

print("### 3. 원하는 위치에 값 넣기")
a = [1, 2, 3, 5, 4, 3]
a.insert(2, 100)  # n번째 index, 넣고싶은 값
print(a)

print("### 4. 리스트의 길이 구하기")
print(len(a))

print("### 5. 요소값 삭제하기 (1)")
# del 리스트명[인덱스]
del a[2]
print(a)

# remove 함수: 리스트 중에서 삭제하고 싶은 값 첫번째 삭제
# a.remove(3)
# a.remove(3)
#print(a)

print("### 6. 요소가 몇 개인지 확인")
print(a.count(3))

print("### 7. 값을 넣으면 index 위치를 알려준다.")
print(a.index(5))
