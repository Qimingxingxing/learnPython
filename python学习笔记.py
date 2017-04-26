python

literal constants

Numbers: integer and float, no seperate long type. int can be 
any size of Integer.
Strings:
Triple Quotes: '''
multi-line Strings
'''
strings are immutable!  and no char type. single and double Quotes are the same

format method: 
age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
index 0, index 1
0和1可以省略

print without a newline
print('a', end='')
print('b', end='')
print without a newline, with a space
print('a', end=' ')
print('b', end=' ')
print('c')

escape sequence
\' \n \t

a single backslash at the end of the line indicates that the string is 
continued in the next line, but no newline is added. 
"This is the first sentence. \
This is the second sentence."

raw string: useful for regular expression
 r"Newlines are indicated by \n"

variables

Identifier Naming
1.The first character of the identifier must be a letter of the alphabet 
(uppercase ASCII or lowercase ASCII or Unicode character) or an underscore
 ( _ ).
2.The rest of the identifier name can consist of letters (uppercase ASCII 
 	or lowercase ASCII or Unicode character), underscores ( _ ) or digits 
 0-9).
3.case sensitive

Python refers to anything used in a program as an object. include number and string

Python is strongly object-oriented in the sense that everything is an object 
including numbers, strings and functions.

implicit line joining 括号 不需要\ 进行换行
i = \
5
Logical And Physical Line 可以用；去一行写多个指令 但是请不要用

statements with the same indentation: 
Each such set of statements is called a block. 


Chapter 2: Operations and Expressions
+ - * / ** // % << >> (signed shift). & | ^ ~ < > <= >= == != not and
short-circuit or
Shortcut for math operation and assignment
a *= 3
／： 13/3 = 4.33333  //: 13/3 = 4(down to the nearest whole number)

Evaluation Order
remember the table

Control Flow
remember the if - elif - else:
while True:
	print("I love you, and I hate you, Wang Yiming")

For loop:
The for..in statement is another looping statement which iterates over 
a sequence of objects i.e. go through each item in a sequence

Remember that the else part is optional. When included, it is always 
executed once after the for loop is over unless a break statement is 
encountered.

break statement
continue statement

There is no switch statement in Python.

变量作用域：
局部变量 全局变量   全局变量可以在函数里面输出
global statement:  change the name to be global   not encouraged

Default Argument Values
def say(message, times=1):
    print(message * times)
the default argument value should be a constant. More precisely, 
the default argument value should be immutable
有默认值的行参必须放在最后面

Keyword Arguments

VarArgs parameters	
def total(a=5, *numbers, **phonebook):
    print('a', a)
    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)
    #iterate through all the items 
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))

There are four built-in data structures in Python - list, tuple, 
    dictionary and set. in dictionary
tuple dictionary
Every function implicitly contains a return None statement at the end 
unless you have written your own return statement.

docstrings
'''line 1

line 3'''

from..import
avoid using the from..import statement, use the import statement instead. 
Byte-compiled .pyc files
Every module has a name and statements in a module can find out the name of their module. 
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
 
from mymodule import *
 Remember that you should avoid using import-star, i.e. from mymodule import * .
 Explicit is better than Implicit
help(list) dir(list)

There are four built-in data structures in Python - list, tuple, 
dictionary and set. 
Lists, tuples and strings are examples of sequences,
The major features are membership tests, (i.e. the in and not in
 expressions) and indexing operations, which allow us to fetch a
  particular item in the sequence directly.
slicing operation 
tuple
empty () single element(1,)
bri = set(['brazil', 'russia', 'india'])
Sequences

# copy by reference
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist is just another name pointing to the same object!
mylist = shoplist
# I purchased the first item, so I remove it from the list
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# Notice that both shoplist and mylist both print
# the same list without the 'apple' confirming that
# they point to the same object
print('Copy by making a full slice')
# Make a copy by doing a full slice
mylist = shoplist[:]
# Remove first item
del mylist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# Notice that now the two lists are different

Fields are of two types - they can belong to each instance/object of the class
or they can belong to the class itself. They are called instance variables and 
class variables respectively.

Class methods have only one specific difference from ordinary functions - they 
must have an extra first name that has to be added to the beginning of the 
parameter list, but you do not give a value for this parameter when you call the
 method, Python will provide it. This particular variable refers to the object 
 itself, and by convention, it is given the name self .

class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello, my name is', self.name)
p = Person('Swaroop')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()

需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，
是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样
的变量名

>>> bart = Student('Bart Simpson', 98)
>>> bart.get_name()
'Bart Simpson'
>>> bart.__name = 'New Name' # 设置__name变量！
>>> bart.__name
'New Name'

表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name
变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码
给bart新增了一个__name变量。

python add two underscores to indicate a private variable or method;
如果你写了代码“from <模块/包名> import *”，那么以“_”开头的名称都不会被导入，
除非模块或包中的“__all__”列表显式地包含了它们。

“__spam”这种形式（至少两个前导下划线，最多一个后续下划线）的任何标识符将会被“_classname__spam”
这种形式原文取代，在这里“classname”是去掉前导下划线的当前类名。
class A(object): 
... def _internal_use(self): 
... pass 
... def __method_name(self): 
... pass 

dir(A()) 
['_A__method_name', ..., '_internal_use']

__init__ 类似这样的 表示python内部定义的特殊方法名

List Comprehensions

generator 
g = (x * x for x in range(10))
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行
时从上次返回的yield语句处继续执行。
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()
函数获得一个Iterator对象。

编写高阶函数，就是让函数的参数能够接收别的函数
def add(x, y, f):
    return f(x) + f(y)
add(-5, 6, abs)

>>> def f(x):
...     return x * x
...
>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]
map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，
因此通过list()函数让它把整个序列都计算出来并返回一个list。

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
>>> from functools import reduce
>>> def add(x, y):
...     return x + y
...
>>> reduce(add, [1, 3, 5, 7, 9])
25

filter

Python内建的filter()函数用于过滤序列。

和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数
依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
# 结果: [1, 5, 9, 15]

偏函数
>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> int2('1010101')
85

Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。

在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：

int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：

>>> int('12345')
12345
但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：

>>> int('12345', base=8)
5349
>>> int('12345', 16)
74565
假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：

def int2(x, base=2):
    return int(x, base)
这样，我们转换二进制就非常方便了：

>>> int2('1000000')
64
>>> int2('1010101')
85
functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：

>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> int2('1010101')
85
所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住
（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。


对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，
将无法调用run()方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()
方法就可以了：

class Timer(object):
    def run(self):
        print('Start...')
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，
就可以被看做是鸭子。

通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过
程中动态给class加上功能，这在静态语言中很难实现。

实例属性 & 类属性
在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Ani
mal类型或者它的子类，
否则，将无法调用run()方法。对于Python这样的动态语言来说，则不一定需要传入Animal类型。

但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实
例能添加的属性：
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots

Python内置的@property装饰器就是负责把一个方法变成属性调用的

还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，
这样，程序运行时就减少了出错的可能性。

1、_xxx 不能用于’from module import *’ 以单下划线开头的表示的是protected类型的变量。

即保护类型只能允许其本身与子类进行访问。

2、__xxx 双下划线的表示的是私有类型的变量。只能是允许这个类本身进行访问了。连子类也

不可以

3、__xxx___ 定义的是特列方法。像__init__之类的
from pythonModule.pythonClass import *
