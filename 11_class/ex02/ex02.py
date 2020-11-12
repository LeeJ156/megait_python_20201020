# 설계도
class Person:
    # 생성자: 객체가 생성될 때 불려진다.
    #def __init__(self):
    def __init__(self, name='홍길동', birth='19000101', gender='남자'):
        self.name = name
        self.birth = birth
        self.gender = gender

    # 소멸자: 객체가 소멸될 때 불려진다.
    def __del__(self):
        print("내 돈을 사회에 기부하겠다.")

    def greet(self):
        print("안녕하세요")

    def walk(self):
        print("뚜벅뚜벅")

    def introduce(self):
        print("내 이름은 %s이고 성별은 %s이다." % (self.name, self.gender))

    def age(self):
        # '19990101'
        # 변수 앞에 self가 없는 이유: age 메소드에서만 사용하기 위한 일반 변수이다.
        #   여기서 만들어진 일반 변수는 외부(다른메소드나 클래스 밖에서)에서 사용 불가.
        year = int(self.birth[0:4])
        age = 2020 - year + 1
        print("나이는 %d세이다." % age)

boram = Person("신보람", "19990101", "여자")  # 객체 생성
boram.greet()
boram.walk()
boram.introduce()
boram.age()

bada = Person() # 객체 생성
bada.introduce()
