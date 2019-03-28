if __name__ == '__main__':
    str = 'sadasdsdd'
    # 查找
    s = str.find('d')
    print(s)

    # 从下表开始找
    s1 = str.find('a',3)
    print(s1)

    #
    s2= str.find('s',2,6)
    print(s2)

    st = str.index('s',3,6)
    print(st)


    ss = str.count('s',5,8)
    print(ss)












