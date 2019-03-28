if __name__ == '__main__':

    mstr = 'good good study , day day up'
    mcount = mstr.count('good')
    print(mcount)

    mc = mstr.count('good',1)
    print(mc)

    mm = mstr.count('good',0,10)
    print(mm)

    # 修改字符
    m = mstr.replace('day','go')
    print(m)

    m1 = mstr.split('\v',5)
    print(m1)

    # 首字母大写
    m2 = mstr.capitalize()
    print(m2)

    # 是否以指定字符串开头
    mm = mstr.startswith('d',2,5)
    print(mm)

    





