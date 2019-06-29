# 計算 1 + 2 + 3 + ... + 100
count_sum = 0
for i in range(1,101):
    count_sum += i
s = "1 + 2 + 3 + ... + 100=%d" % (count_sum)  # 字串格式化，語法：  "內容%d %d" % (int,int)
print(s)
print("\n\n\n")

# 九九乘法表
for i in range(1,10):
    for j in range(1,10):
        print("%d x %d = %d" % (i,j,i*j))
print("\n\n\n")

# 九九乘法表2 - 方形版
for i in range(1,10):
    for j in range(1,10):
        print("%d x %d = %d\t" % (i,j,i*j),end="")
    print("")
print("\n\n\n")


