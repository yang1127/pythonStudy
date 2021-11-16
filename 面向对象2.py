'''
# 继承：类与类之间的所属关系

基本语法：
class 类B(类A):  -- B继承A
    pass

特点：B类的对象可以使用A类的属性和方法
优点：代码复用

类A：父类、基类
类B：子类、派生类
'''

'''
# 单继承：如果一个类只有一个父类，把这种继承关系称为单继承
# 多继承：如果一个类有多个父类，把这种继承关系称为多继承
# 多层继承：C-B-A子类可以使用所有继承链中的类中的方法和属性


# 1、定义一个动物类 Animal
class Animal(object):  # 对于Animal、object类，单继承

    # 2、在动物类中，书写play方法
    def play(self):
        print('愉快的玩～')


# 3、定义Dog类继承Animal类
class Dog(Animal):  # Dog - Animal 单继承，Dog - Animal - object 多层继承
    def bark(self):
        print('汪汪🐶叫～')


class XTQ(Dog):  # XTQ - Dog 单继承，XTQ - Dog - Animal 多层继承
    pass


# 4、创建dog类对象，调用父方法
dog = Dog()
dog.play()  # 调用父类Animal中的方法
print('=================')
xtq = XTQ()
xtq.bark()  # 调用父类Dog中的方法
xtq.play()  # 调用爷爷类Animal中的方法
'''

'''
# 重写：子类定义和父类名字相同的方法
# 为什么重写：父类中的方法，不能满足子类对象的需求，所以重写
# 重写后的特点：子类对象调用子类自己的方法，不能调用父类的方法；父对象调用父类自己的方法


# 1、定义Dog类，书写bark方法，输出汪汪叫～
class Dog(object):
    def bark(self):
        print('汪汪叫～')


# 2、定义XTQ类，重写父类中bark方法，输出嗷嗷叫～
class XTQ(Dog):
    def bark(self):
        print('嗷嗷叫～')


# 创建Dog类对象
dog = Dog()
dog.bark()

# 创建XTQ类对象
xtq = XTQ()
xtq.bark()
'''

'''
# 重写后子类调用父类的方法
# 1、定义Dog类，书写bark方法，输出汪汪叫～
class Dog(object):
    def bark(self):
        print('汪汪叫～')


# 2、定义XTQ类，重写父类中bark方法，输出嗷嗷叫～
class XTQ(Dog):
    def bark(self):
        print('嗷嗷叫～')

    # 调用父类，输出汪汪叫～
    def see_host(self):
        # 方法一：父类名.方法名(self, 其他参数)，类型.方法() 需要手动给self形参传递实参值
        # 若通过实例对象.方法名() 调用方法，不需要给self传递实参值，python解释器会自动将对象作为实参值传递给self对象
        Dog.bark(self)
        print("～～～～～～～")

        # 方法二：super(当前类A, self).方法名(参数)
        super(XTQ, self).bark()  # 调用XTQ类父类中的bark方法
        print("～～～～～～～")

        # 方法三：法二的简写，super().方法名(参数)  <-- super(当前类, self).方法名()
        super().bark()


# 创建XTQ类对象
xtq = XTQ()
xtq.see_host()
'''
