"""用python设计的第一个小程序"""
import random

answer = random.randint(1,10)
const = 3


while const > 0:
    temp = input("不妨猜猜闵军心中想的数字,你有三次机会哦！：")
    guess = int(temp)
    if guess == answer:
        print("哇晒！你是闵军心里的小蛔虫哈！")
        print("猜对了，可惜不给你奖励！")
        break
    else:
        if guess < answer:
            print("小了哦！")
        else:
            print("大了哦！")
        const -= 1

print("游戏结束了！不玩了哦！")
