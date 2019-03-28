if __name__ == '__main__':
    num = int(input('请输入一个奇数数字:'))
    for i in range(num, 0, -1):
        print(i * ' ' + (num + 1 - i) * '*' + +(num - i) * '*')