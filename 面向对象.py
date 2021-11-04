# 类与对象
# 类
# 类是泛指，是由对象抽象而来
# 在代码中，使用过关键字class定义

# 对象
# 对象是特指，是具体存在的
# 在代码中，对象是由类创建的

# 类的构成：名称、属性-特性、方法-行为、函数
# 类的抽象：名词提炼法、所见即所得

# 类的定义 - class
'''
class 类名(object): - 新式类，继承object类
    类中的代码

class 类名(): - 旧式类
    类中的代码

class 类名: - 旧式类
    类中的代码
'''

'''
class Dog(object):
    # 在类中定义的函数，称为方法，函数的所有的知识都可以用
    def play(self):
        print('小狗快乐的啃骨头～')


# 创建对象 变量 = 类名()
dog = Dog() # 创建一个对象，dog


# 可使用对象调用类中的方法 - 对象.方法名()
dog.play()

my_list = list()
'''


'''
# 类外部添加和获取对象属性
class Dog(object):
    def play(self):
        print('小狗快乐的啃骨头～')


# 创建对象、调用方法
dog = Dog() # 创建一个对象，dog


# 给对象添加属性 - 对象.属性名 = 属性值
dog.name = '大黄'  # 给dog 对象添加name属性，属性值为 大黄
dog.age = 2  # 给dog 对象添加age属性，属性值为 2


# 获取对象的属性值 - 对象.属性名
print(dog.name)
print(dog.age)

# 修改属性值，和添加一样，存在就是修改，不存在，就是添加
dog.age = 3  # age属性已经存在，所以是修改属性值
print(dog.age)

dog1 = Dog()  # 新创建一个对象 dog1
dog1.name = '小白'
print(dog1.name)
'''

'''
# 类内部添加和获取对象属性 - self就是一个形参的名字，可以书写成其他
class Dog(object):
    # self 作为类中方法的第一个形参，在通过对象调用方法的时候，不需要手动的传递实参值，是python解释器
    # 自动将调用该方法的对象传递给self，所以self这个形参代表的是对象
    def play(self):
        print(f'self:{id(self)}')
        print(f'一只流浪的小狗🐶 {self.name} 在快乐的玩耍～')


# 创建对象、调用方法
dog = Dog()  # 创建一个对象，dog
dog.name = '大黄'
print(f'dog:{id(dog)}')
dog.play()

dog1 = Dog()
dog1.name = '小白'
dog1.play()print(f'dog:{id(dog)}')
'''



# 魔法方法
# 在python的类中，有一类方法，这类方法以两个下划线开头，和两个下划线结尾
# 且在满足某个特定条件的情况下，会自动调用，这类方法称为魔法方法

# __init__()   C++中构造函数
# 调用时机：在创建对象后，会立即调用
# 作用：
#   1、用来给对象添加属性，给对象属性一个初始值（构造函数）
#   2、代码的业务需求，每创建一个对象，都需要执行的代码可以写在 __init__ 中

'''
# 不带参
class Dog(object):
    def __init__(self):  # self 是对象
        print('我是__int__方法，我被调用了')
        # 对象.属性名 = 属性值
        self.name = '小狗'


# 创建对象
dog = Dog()
print(dog.name)

dog1 = Dog()
print(dog1.name)
'''


# 注意点：如果 __init__ 方法中，有除self之外的形参，那么在创建对象的时候
# 需要给额外的形参传递实参值 类名(实参)

# 带参
class Dog(object):
    def __init__(self, name):  # self 是对象
        print('我是__int__方法，我被调用了')
        # 对象.属性名 = 属性值
        self.name = name

    def play(self):
        print(f'小狗🐶{self.name}快乐的拆家中...')


# 创建对象 类名(实参值)
dog = Dog('大黄')
print(dog.name)

dog1 = Dog('小白')
print(dog1.name)

dog1.play()












































































