# 函数、类、模块

def modify_name(filename):
    filename += ".txt"
    filename = "my_" + filename
    print(filename)


modify_name("f1")


def my_func():
    filename = "f1"
    total_name = "my_" + filename + ".txt"
    print(total_name)


my_func()


def modify_name(filename):
    filename += ".txt"
    filename = "my_" + filename
    return filename


new_filename = modify_name("f1")
print(new_filename)


def f(x, a=1, b=1, c=0):
    return a*x**2 + b*x + c*1


print(f(2, a=2))
print(f(2))

# global filename提出申请在函数内部修改全局变量filename
