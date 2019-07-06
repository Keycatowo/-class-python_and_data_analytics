# 幾A幾B

def compare_A(a,b):
    count = 0
    Sa = str(a)
    Sb = str(b)
    for i in range(0,3+1):
        if Sa[i] == Sb[i]:
            count +=1
    return count

def compare_B(a,b):
    # appear_times = [0 for x in range(0,10)] #寫法同下
    appear_times_a = [0] * 10
    appear_times_b = [0] * 10
    B_sum = 0
    S_a = str(a)
    S_b = str(b)
    for i in range(0,3+1):
        for j in range(0,9+1):
            if int(S_a[i]) == j:
                appear_times_a[j] += 1
            if int(S_b[i]) == j:
                appear_times_b[j] += 1
    for i in range(0,9+1):
        if appear_times_a[i]>0 and appear_times_b[i]>0:
            B_sum += min(appear_times_a[i],appear_times_b[i])
    B_sum -= compare_A(guess,ans)
    return B_sum

import  random

ans = random.randint(1000,9999)
times = 0
print(ans)
while times<4:
    times += 1
    guess = int(input("請輸入一個4位數字:"))
    A = compare_A(guess,ans)
    # print(A)
    B = compare_B(guess,ans)
    # print(B)
    print("第%d次猜測：%dA%dB" % (times,A,B))
    # if(compare_A(guess,ans)):
    #     print("Bingo!")
    #     break
    # else:
    #     print("Again~")

    if times == 4 :
        print("Game Over!")
        print("The answer is %d!" % (ans))
