# 自定義函數
def my_abs(x):
    if x<0:
        return -x
    else:
        return x

def my_sum(lower_bound,upper_bound):
    SUM = 0
    for i in range(lower_bound,upper_bound+1):
        SUM += i
    return  SUM
print("my_abs:")
print("\t%d -> %d" % (-1,my_abs(-1)))
print("\t%d -> %d" % (2,my_abs(2)))
print("my_sum:")
print("\tsum of [%d %d] is %d" % (10,20,my_sum(10,20)))
