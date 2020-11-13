s1 = {1, 2, 3, 3}
print(s1)

s2 = set("hello")
print(s2)

s3 = set((1, 2, 3)) # set함수는 하나의 값만 받을 수 있다.
print(s3)

s4 = set([5, 6, 7])
print(s4)

# 값 한 개 추가하기(add)
s4.add(1)
print(s4)

# 값 n개 추가하기(update)
s4.update([100, 101, 102])
print(s4)

# 값 제거하기(remove)
s4.remove(100)
print(s4)

# 집합 연산
set1 = {1, 2, 3, 4}
set2 = set([2, 4, 6, 8])

# 합집합
print("합집합 1:", set1 | set2)
print("합집합 2:", set1.union(set2))

# 교집합
print("교집합 1:", set1 & set2)
print("교집합 2:", set2.intersection(set1))

# 차집합
print("차집합 1:", set1 - set2)
print("차집합 2:", set1.difference(set2))
