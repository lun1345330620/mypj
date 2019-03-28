def dd():
    m = input('输入')
    n = '@'
    if n in m:
        m = m.split('@',2)
        print('合法')
        print(m)
    else:
        print('不合法')
if __name__ == '__main__':
    pass

