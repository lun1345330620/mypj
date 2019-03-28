if __name__ == '__main__':
    # 字典
    mdict = {'姓名':'高博','年龄':'18'}
    print(mdict)
    mdict = {'gao':'gou','nian':'3'}
    m = int(input("请输入:"))
    if m%4 ==0:
        if m%100 != 0:
            print('闰年')
        else:
            print('平年')
    elif m%400 == 0:
        print('世纪年')




