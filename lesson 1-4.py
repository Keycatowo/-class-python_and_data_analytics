import time
count_sum = 0
t_i = time.time() #起始時間
for i in range (1,100000):
    count_sum += i
t_f = time.time() #結束時間

print("計算式子\n\t1+2+...+100000=%d\n花費時間:%f秒" % (count_sum,t_f-t_i))

