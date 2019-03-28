import random
if __name__ == '__main__':
    num = int(input("输入一个整数"))
    if num % 2 != 0:
        pass
    else:
        num1 = random.randint(0,100)
        print(num1)
    if num > num1:
        print(num)
    elif num < num1:
        print(num1)
