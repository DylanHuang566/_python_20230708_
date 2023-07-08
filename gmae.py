#猜數字遊戲1-100，顯示猜了幾次，猜對猜錯。並提示下一次猜的範圍
import random

number = random.randint(1, 100)
guesses_taken = 0
guess = None

print("歡迎來到猜數字遊戲！")
print("猜一個介於 1 到 100 之間的數字。")

while guess != number:
    guess = int(input("請輸入你的猜測: "))
    guesses_taken += 1

    if guess < number:
        print("太低了！再高一點。")
        print("下一次猜的範圍是", guess + 1, "到 100。")
    elif guess > number:
        print("太高了！再低一點。")
        print("下一次猜的範圍是 1 到", guess - 1, "。")
    else:
        print(f"恭喜你猜對了！你總共猜了 {guesses_taken} 次。")
        break

