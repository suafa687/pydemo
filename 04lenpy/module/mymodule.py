class Man:

    # 私有变量，只能在本类内部访问
    __privateProp=1

    # 保护变量，只能被自己和子类访问
    _protectProp=2

    # 公有变量，可以在外部访问
    age=10
    name='initName'

    # 构造函数
    def __init__(self, a):
        self.age = a
        print("create this")

    # 析构函数
    def __del__(self):
        print("del this")

    def setAge(self, a):
        self.age = a

    def getAge(self):
        return self.age
    
    # 类方法，可以通过类名或者对象访问
    # 不能访问对象属性，可以访问类属性
    @classmethod
    def setName(cls, nm):
        cls.name = nm

    # 静态方法，可以通过类名或者对象调用
    # 不能直接访问类属性和对象属性，可以通过类名引用类属性
    @staticmethod
    def printName():
        print("printName:",Man.name)

class SupperMan(Man):
    def __init__(self):
        super().__init__(1)
    # 上下文函数，通过使用with语句，在代码块调用前先调用本函数，可以管理资源的申请
    def __enter__(self):
        print("class SupperMan enter")
        return self
    # 上下问函数，通过使用with语句，在代码块调用后再调用本函数，可以管理资源的释放
    def __exit__(self, exc_type,exc_val, exc_tb):
        print("class SupperMan exit")