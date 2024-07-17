# 这是我的第一行python代码
say_hi = "Hello World"
print("你的第一行代码：", say_hi)

# 变化的量
name = "文件管理系统"
name2 = '文件管理系统'
name3 = """
这是一段长文本，
有多长的，
是真的很长。
"""
name4, name5, name6 = "文件", "系统", "管理"

name7 = name8 = name9 = "文件系统"

name10 = "文件" + "系统"

# 打印Print
print("莫烦Python最棒~")
print(name)
print("莫烦Python的", name, "业界顶呱呱")
print("我看着", "莫烦", "的教学长大的~")

# 数学运算
num_of_files = 10
print("我系统里有", num_of_files, "个文件")
print("分五组，每组", num_of_files / 5, "个")
print("幂:3**2=", 3**2)
print("取整数:10//3=", 10//3)

a = 1
a += 1
print("a += ", a)
a -= 1
print("a -= ", a)
a *= 10
print("a *= ", a)
a /= 2
print("a /= ", a)

# 条件判断
in_trash = False
if not in_trash:
    print("不可以被彻底删除")
else:
    print("可以被彻底删除")

print("2 != 2", 2 != 2)
print(2 < 3 and 2 < 5)  # and表示两个条件都成立
print(2 > 3 or 3 == 3)  # or表示两个条件有一个成立
print(2 > 3 or not 3 == 3 and 5 < 10)  # not表示取反

today = 4
if today == 1:
    print("周一")
elif today == 2:
    print("周二")
elif today == 3:
    print("周三")
else:
    print("周一周二周三之外的一天")  # if-elif-else

for i in range(5):
    print("新文件-" + str(i))
for i in range(3, 10, 2):
    print("新文件-" + str(i))  # 3开始，到10前，步长为2

count = 0
guess_num = 10
while guess_num != 20:
    guess_num += 1
    count += 1
    if count > 10:
        break
    print(guess_num)

for i in range(10):
    if i % 2 != 0:
        continue    # 跳过奇数
    print(i)
