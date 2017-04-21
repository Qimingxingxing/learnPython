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
