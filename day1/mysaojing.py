if __name__ == '__main__':

    num = int(input("请输入："))
    # if num % 2 != 0:
    #     num+=1
    s = '*'
    for i in range(1, num+2, 2):
        t = (num - i) // 2
        print(' '* t + '*' * i + ' ' * t)
    for i in reversed(range(1, num+1, 2)):
        t = (num - i) // 2
        print(' ' * t + s * i + ' ' * t)












