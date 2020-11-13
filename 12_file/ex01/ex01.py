# 2번째 파라미터 옵션
# w: 새로 쓰기
# a: 기존 내용에 쓰기
f = open("test2.txt", 'a', encoding='utf8')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    print(data)
    f.write(data)

f.close()
