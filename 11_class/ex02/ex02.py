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
