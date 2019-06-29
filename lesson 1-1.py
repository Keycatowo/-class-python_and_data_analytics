# 成人票價，台北、台中、左營
ticket_price_adult = [290,700,1490]

# 輸入
target = input("請輸入目的地：")
target_code = -1
ticket_adult = int(input("成人票張數："))
ticket_child = int(input("兒童票張數："))
back_forth = input("是否來回票[是/否]：")
is_back_forth = True
sum_price = 0
# 目的地處理
if(target == "台北" ):
    target_code = 0
elif(target == '台中'):
    target_code = 1
elif(target == '左營'):
    target_code = 2

if target == -1:
    print("輸入錯誤！")
else:
    # 來回票處理
    if(back_forth == "是"):
        is_back_forth = True
    else:
        is_back_forth = False
    # 計算票價
    sum_price = ticket_adult * ticket_price_adult[target_code] + ticket_child * ticket_price_adult[target_code] * 0.5
    if(is_back_forth):
        sum_price = sum_price * 0.9
    # 顯示
    print("最終金額為：",round(sum_price))
