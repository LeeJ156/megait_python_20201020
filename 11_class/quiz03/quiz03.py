class Product:
    def __init__(self, name, price, expired_date):
        self.name = name
        self.price = price
        self.expired_date = expired_date

    def product_info(self):
        print("이름:", self.name)
        print("가격:", self.price)
        print("유통기한:", self.expired_date)

    def price_of_product(self, count):
        print("제품 %d개의 가격: %d" % (count, self.price * count))

    def sale_status(self):
        today = "2020-11-17"
        if self.expired_date >= today:
            print("판매 가능 상품")
        else:
            print("판매 불가 상품")


p = Product("새우깡", 1300, "2021-03-02")
p.product_info()
p.price_of_product(5)
p.price_of_product(13)
p.sale_status()
