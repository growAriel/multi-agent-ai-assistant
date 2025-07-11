# guess_number.py
import random

def guess_number():
    print("欢迎来到猜数字游戏!")
    print("我已经想好了一个1-100之间的数字，你有10次机会猜中它")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"尝试 {attempts + 1}/{max_attempts}: 你的猜测是? "))
        except ValueError:
            print("请输入一个有效的数字!")
            continue
            
        if guess < 1 or guess > 100:
            print("请输入1-100之间的数字!")
            continue
            
        attempts += 1
        
        if guess == secret_number:
            print(f"恭喜你! 你在第{attempts}次猜中了数字 {secret_number}!")
            break
        elif guess < secret_number:
            print("太小了，再大一点!")
        else:
            print("太大了，再小一点!")
    else:
        print(f"很遗憾，你没有猜中。正确的数字是 {secret_number}")

    play_again = input("想再玩一次吗? (y/n): ").lower()
    if play_again == "y":
        guess_number()
    else:
        print("谢谢游玩，再见!")

if __name__ == "__main__":
    guess_number()