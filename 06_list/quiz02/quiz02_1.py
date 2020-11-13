def get_index(li, value):  # 리스트를 받고, 어떤 값을 받고
    index = li.index(83)
    return index   # 리스트를 받고, 값의 index를 반환

numbers = [89, 70, 83, 89, 92, 100, 64]

print("index는 %d번째이며 값은 83입니다." % get_index(numbers, 83))
