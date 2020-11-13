# 설계도
class Person:
    # 생성자: 객체가 생성될 때 불려진다.
    def __init__(self):
        self.name = "신보람"
        self.birth = '19990101'
        self.gender = "여자"

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

boram = Person()  # 객체 생성
boram.greet()
boram.walk()
boram.introduce()
boram.age()


