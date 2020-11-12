# 핸드폰
class Cellphone:
    def __init__(self):
        print("객체가 생성됨")
        # 멤버변수
        self.model_name = "iPhonePro11"
        self.color = "gold"
        self.price = 1800000
        self.maker = "apple"

    # 메소드(멤버함수)
    def camera(self):
        print("찰칵")

    def call(self):
        print("전화하기")

    def introduce(self):
        print("제조사:%s, 모델명:%s, 색상:%s, 가격:%d"
              % (self.maker, self.model_name, self.color, self.price))

# 인스턴스 화  => 객체
c1 = Cellphone()
print(type(c1))

# 멤버변수 값 출력하기
print(c1.model_name)
print(c1.color)
print(c1.maker)
print(c1.price)

# 메소드 호출
c1.call()
c1.camera()
c1.introduce()

# 여러개의 객체를 만들기
cellphones = list()
for i in range(100):
    cellphones.append(Cellphone())

print(cellphones[0].model_name)  # 첫번째 객체의 모델명 출력

c1.maker = "삼성"   # 멤버변수 값 변경 가능
print(c1.maker)
c1.introduce()
cellphones[0].introduce() 
