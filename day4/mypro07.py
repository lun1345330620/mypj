def dd():
    a = input('请输入任意数字')
    if a == a[::1]:
        print(a,'是回文数')
    else:
        print(a,'不是回文数')
if __name__ == '__main__':
    dd()