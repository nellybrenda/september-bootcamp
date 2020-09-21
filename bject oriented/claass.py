
class HumanBeings():
    #initialization of class

    def __init__(self, color, height, age):
        self.color =color
        self.height =height
        self.age  =age

        #creating methods-functions that are related

    def get_result(self):
        return f'this person is of {self.color}-color,{self.height}-height,{self.age}-age'

#instantiation
person1 =HumanBeings('black',170,28)
person2 =HumanBeings('white',130,32)

result1 = person1.get_result()
print(result1)
result2 = person2.get_result()
print(result2)