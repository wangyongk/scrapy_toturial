#lambda函数也叫匿名函数，即，函数没有具体的名称
#使用函数 lambda 变量名称：变量表达式
def f(x):
    return x**2
print(f(4))
#Python中使用lambda
g = lambda x : x**2
print(g(4))
"""
                    优点
        1. 用Python写一些执行脚本时，使用lambda可以省去定义函数的过程，
           让代码更加精简。
        2. 对于一些抽象的，不会别的地方再复用的函数，
           有时候给函数起个名字也是个难题，
           使用lambda不需要考虑命名的问题。
        3. 使用lambda在某些时候让代码更容易理解。
"""
def action(x):
    return lambda y:x+y
a=action(2)
a1=a(22)
print(a1)
"""
    这里定义了一个action函数，返回了一个lambda表达式。
    其中lambda表达式获取到了上层def作用域的变量名x的值。
    a是action函数的返回值，a(22)，
    即是调用了action返回的lambda表达式
"""