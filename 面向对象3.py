# 面向对象三大特性：封装、继承、多态

# 封装：
# 将属性和方法放到一起做为一个整体，通过实例化对象来处理
# 隐藏内部实现细节，只需要和对象及其属性和方法交互就可
# 对类的属性和方法增加访问权限控制

# 私有权限：在方法和属性前加上两个下划线 __ ，就变为私有
#   1、不能在类外部通过对象直接访问和使用，只能在类内部访问和使用
#   2、不能被子类继承
#   3、想要访问和使用私有属性：定义一个公有的方法，通过这个方法使用
# 公有权限：除去私有的，就是公有的

'''
# eg: 定义一个people类，定义属性ICBC_money,钱不能随便被修改
class People(object):
    def __init__(self):
        # 在python中，私有本质是修改属性的名字，在创建对象的时候，会自动修改属性名
        # 在属性名的前面加上 _类名前缀
        self.__ICBC_money = 0

    # 定义公有的方法，提供接口，修改余额
    def get_money(self):
        return self.__ICBC_money

    def set_money(self,  money):
        self.__ICBC_money += money


# 创建对象
xy = People()
print(xy.__dict__)  # k：属性名，v：属性值 # {'_People__ICBC_money': 0}

# 修改钱数
xy.set_money(100)
print(xy.get_money())

xy.set_money(-50)
print(xy.get_money())
'''

'''
# 小狗生完孩子后，才能休息30天～
class Dog(object):
    def born(self):
        print("生了一只小狗，需要休息～")

    def __sleep(self):
        print("休息30天～")


# 创建对象
dh = Dog()
# dh.sleep()  # 报错
dh.born()  # 生了一只小狗，需要休息～
'''

"""
对象（实例对象）：通过class定义的类创建的，即通过类实例化来的，又称为实例，实例对象
实例对象定义的属性称为实例属性，通过实例对象（self）定义的属性都是实例属性
实例属性：每个实例属性对象都存在一份，并且值可以不一样

类（对象）：通过class定义的，又称类对象，是python解释器在创建类的时候自动创建的
作用：1、通过类对象，去定义实例对象  2、类对象可以保存一些属性，称为类属性
类属性定义：在类内部，方法外部定义的变量都是类属性
类属性，内存中只有一份

如何确定一个属性是该定义为实例属性还是类属性？
先假设这个属性是实例属性，查看这个属性对于不同的实例对象，属性值是否一样，并且需要同时变化
如果是，可以定义为类属性
如果不是，可以定义为实例属性
"""

"""
class Dog(object):
    # 定义类属性，类名
    class_name = '狗🐶类'

    def __init__(self, name, age):
        # 定义的都是实例属性
        self.name = name
        self.age = age


# 创建Dog类对象
dog = Dog('大黄', 2)
print(dog.__dict__)

# 类名.__dict__ 查看类对象具有的属性
# print(Dog.__dict__)

# 访问类属性 -- 类名.类属性
print(Dog.class_name)

# 修改类属性 -- 类名.类属性 = 属性值
Dog.class_name = '哺乳类'
print(Dog.class_name)
"""











