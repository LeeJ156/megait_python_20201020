# 217p
# 파일 쓰기
#open(file_path, mode, encoding)
f = open('test1.txt', 'a', encoding='utf8')
for i in range(1, 11): # 1 ~ 10
    data = "%d번째 줄입니다.\n" % i
    print(data)
    f.write(data)

f.close()
