
# csv 파일
# csv은 쉼표로 구분된 스프레드시트 파일

# csv 파일 만들기
# f = open('member.csv', 'w', encoding='utf8')
# f.write("유재석,49,01011112222\n")
# f.write("이효리,30,01012346666\n")
# f.write("강호동,55,01005053555\n")
# f.close()

# csv 파일 열기
f = open('member.csv', 'r', encoding='utf8')
while True:
    line = f.readline()
    if not line:
        break

    print(line)
    line = line.replace('\n', '') # 줄바꿈 제거
    member = line.split(',')  # 리스트로 저장됨
    print(member)
    name, age, phone = line.split(',')  # 각각의 변수에 저장됨
    print(name)

f.close()
