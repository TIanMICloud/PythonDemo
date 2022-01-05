"""用python设计的第一个小程序"""
temp = input("不妨猜猜闵军心中想的数字：")
guess = int(temp)
if guess == '9':
    print("哇晒！你是闵军心里的小蛔虫哈！")
    print("猜对了，可惜不给你奖励！")
else:
    print("猜错了哦，我心中想的数字是9！")
print("游戏结束了！不玩了哦！")
