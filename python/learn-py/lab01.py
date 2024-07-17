# 基础功能、循环、数据、判断

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

# 数据种类
files = ["f1.txt", "f2.txt", "f3.txt", "f4.txt", "f5.txt"]
print("files[:3] ", files[:3])
print("files[2:4] ", files[2:4])
print("files[-3:] ", files[-3:])
print("old files[1] ", files[1])
files[1] = 12  # 覆盖原文件
print("new files[1] ", files[1])

lt = [1, "file", ["2", 3.2]]
print(lt)
lt[2][0] = "new string"
print(lt)  # List列表

files = {"ID": 111, "passport": "my passport", "books": [1, 2, 3]}  # Key-Value对
print(files)
print(files["books"])  # Dict字典
files["ID"] = 222
print(files)
files["ID"] = [2, 3, 4]  # 覆盖原ID
print(files)

files = ("file1", "file2", "file3")  # Tuple元组
print(files[1])  # files[1] = "file4"这里会报错

my_files = {"file1", "file2", "file3"}  # Set集合
print(my_files)
my_files.add("file3")
print(my_files)
my_files.add("file4")
print(my_files)
my_files.remove("file3")
print(my_files)
print("my_files", my_files)
your_files = {"file1", "file3", "file5"}
print("your_files", your_files)
print("交集 ", your_files.intersection(my_files))
print("并集 ", your_files.union(my_files))
print("补集 ", your_files.difference(my_files))

files = ["f1.txt", "f2.txt", "f3.txt", "f4.txt", "f5.txt"]
for f in files:  # 相当于for i in range(len(files))
    if f == "f3.txt":  # 相当于if files[i] == "f3.txt":
        print("I got f3.txt")
files = {"ID": 111, "passport": "my passport", "books": [1, 2, 3]}
for key in files.keys():
    print("key:", key)

for value in files.values():
    print("value:", value)

for key, value in files.items():
    print("key:", key, ", value:", value)

files = []  # for循环添加再pop出
for i in range(5):
    files.append("f"+str(i)+".txt")  # 添加
    print("has", files)
for i in range(len(files)):
    print("pop", files.pop())   # 从最后一个开始 pop 出
    print("remain", files)

files = ["f1.txt", "f2.txt"]
files.extend(["f3.txt", "f4.txt"])  # 扩充入另一个列表
print("extend", files)
files.insert(1, "file5.txt")     # 按位置添加到第1位（首位是0哦）
print("insert", files)
del files[1]  # 移除某索引
print("del", files)
files.remove("f3.txt")  # 移除某值
print("remove", files)

files = {"ID": 111, "passport": "my passport", "books": [1, 2, 3]}
print('files["ID"]:', files["ID"])  # 按key拿取，并在拿取失败的时候给一个设定好的默认值
print('files.get("ID"):', files.get("unknown ID", "不存在这个 ID"))
files.update({"files": ["1", "2"]})  # 将另一个字典补充到当前字典
print('update:', files)
popped = files.pop("ID")  # pop 调一个item，和列表的 pop 类似
print('popped:', popped)
print("remain:", files)
