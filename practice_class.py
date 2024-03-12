class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()
# 다중 상속을 할 때 super 를 쓰게 되면, 첫번째만 받게 된다.
# super를 쓰지 않고 하나씩 호출 하게 되면 둘다 적용이 됨
dropship = FlyableUnit()