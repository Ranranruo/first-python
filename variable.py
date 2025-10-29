# 문자열 타입
str = "string type"

# 숫자 타입
number = 0
# possible
number = "change string"


# function
def add(a: int, b: int) -> int:
    return a + b

print(add(1,2))

# classes
class Person: 
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def introduce(self): #self는 무조건 받아야함
        print(f"Hi, I'm {self.name}, {self.age} years old.")
p1 = Person("Alice", 30)
p1.introduce()
