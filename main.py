#python 101
class user_info:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        return f'Name: {self.name}, Age: {self.age}'

test = user_info('Beer', 21)

info_string = test.info()
print(info_string)
