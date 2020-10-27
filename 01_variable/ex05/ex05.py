# 사용자로부터 입력을 받는 함수 - 입력 받은 모든 값은 문자열 형태로 받아진다.
noodle_cup = input("육개장 가격 : ")
print(noodle_cup)

# 자료형(data type) 확인 방법
type(noodle_cup)

# 문자 -> 정수로 자료형(Data type) 변환: casting
noodle_cup = int(noodle_cup)
type(noodle_cup)

print("육개장 가격은 %d 입니다." % noodle_cup);


# 입력받은 문자를 숫자로 한번에 변환
count = int(input("육개장 개수 :"))

sum = noodle_cup * count;
print("육개장 %d개의 가격은 %d 입니다." % (count, sum))
