# Shopping cart 클래스 생성
class Shoppingcart:             # 클래스 생성
    def __init__(self):
        self.bucket = []        # 상품목록 저장

    # 장바구니 담기
    def add_item(self, item):   
        self.bucket.append(item)
    
    # 장바구니 뺴기
    def remove_item(self, item):
        self.bucket.remove(item)
    
    # 상품 목록 조회
    def show_item(self):
        return self.bucket

# 상품 클래스
# 속성
# - 제품명
# - 가격
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
# 상품 3개 생성
cart = Shoppingcart()

# 쇼핑 카트 생성
item_a = Item("초코파이", 12000)
item_b = Item("엄마손파이", 7000)
item_c = Item("마우스", 6000)

# 상품 1개 장바구니 담기
cart.add_item(item_a)
# 상품 1개 장바구니 담기
cart.add_item(item_b)
# 상품 1개 장바구니에서 빼기
cart.remove_item(item_b)
# 장바구니에 담긴 상품 목록 조회
for item in cart.show_item():
    print(item.name, item.price)
