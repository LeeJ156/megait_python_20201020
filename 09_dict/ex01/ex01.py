dict1 = {'이름':'신보람', '생년월일':19990101, '성별':'여자'}
print(dict1)

dict1['나이'] = 22
print(dict1)

dict1['나이'] = 30
print(dict1)

#dict1[[1, 2, 3]] = 123  => list는 변하는 값이라 키로 넣을 수가 없다.
#print(dict1)

dict1[(1, 2, 3)] = 123  # => tuple은 변경되지 않는 속성이라 키로 넣을 수 있다.
print(dict1)

# 요소 삭제하기
del dict1['나이']
print(dict1)

# 값 얻기
print(dict1['이름'])
print(dict1['생년월일'])
print(dict1['성별'])
print(dict1[(1, 2, 3)])

print(dict1.get('이름'))
print(dict1.get('생년월일'))
print(dict1.get('성별'))
print(dict1.get((1, 2, 3)))

# key를 모아서 List로 만들기
keys = list(dict1.keys())
print(keys)
print(keys[0])
print(dict1.get(keys[0]))

# value들을 모아서 List로 만들기
print(set(dict1.values()))

# [ (key, value), (key, value) ]
print(list(dict1.items()))

# dict에 key가 존재하는지 여부
if '나이' in dict1:
    print("나이라는 키가 있다.")
else:
    print("나이라는 키가 없다.")

# dict의 모든 값 지우기
dict1.clear()
print(dict1)
