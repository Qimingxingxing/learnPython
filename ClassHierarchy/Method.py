class Foo:
    def __init__(self, name = ""):
        self.name = name

    def ord_func(self):
        print("普通方法")

    @classmethod
    def class_func(cls):
        print("类方法")

    @staticmethod
    def static_func():
        print("静态方法")

foo = Foo()
foo.ord_func()
Foo.class_func()
Foo.static_func()
