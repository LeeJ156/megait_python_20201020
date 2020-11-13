# 2번째 파라미터 옵션
# r: 읽기
f = open("test2.txt", 'r', encoding='utf8')
# 한 줄 읽기
line = f.readline()
print(line)

f.seek(0) # 커서를 맨 앞으로
f.seek(1) # seek 함수는 글자 하나씩 이동
while True:
    # 더이상 읽을 내용이 없으면 반복문 종료
    if not line:
        break
    line = f.readline() ## 한 번 읽으면 읽은 줄이 소비된다.(커서)
    line = line.replace('\n', '') # 줄바꿈 제거

    print(line)

f.close()

# readlines 함수를 사용하면 여러줄을 한번에 읽을 수 있으나 파일이 클 수 있기때문에
# 한 줄 씩 읽는 것이 좋다
f = open("test2.txt", 'r', encoding='utf8')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
