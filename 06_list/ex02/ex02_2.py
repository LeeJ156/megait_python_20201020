a = [10, 1, 8, 2, 5]

print("# 1")
a.sort() # 저장까지 된다.
print(a)

print("# 2: 역순 정렬")
a.reverse()
print(a)

print("# 3: 슬라이싱")
a = [10, 1, 8, 2, 5]
# [10, 1, 8]로 자를 것이다.
# index : 0, 1, 2
slice_a = a[0:3]   # 0, 1, 2
print(slice_a)
print(a)

# [8, 2, 5]로 자를 것이다.
# index : 2, 3, 4
slice_a = a[2:5]
print(slice_a)

print("# 4: 어떤 값이 리스트에 포함되었는지 확인")
if 5 in a:
    print("a 리스트에 5가 들어있다.")
else:
    print("a 리스트에 5가 들어있지 않다.")
