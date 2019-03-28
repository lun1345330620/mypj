if __name__ == '__main__':
    mlist = list()

    for i in range(1,11):
        mlist.append(i**2)
    print(mlist)

    # 列表的生成式   复合列表生成式
    mlist = []
    m = [ i**2 for i in range(1,11) if i % 2 == 0]
    print(m)
    print('m = {mlistkey}'.format(mlistkey = m))


    # 全排列
    mlist = [1,2,3]
    nlist = ['a','b','c']

    qlist = []

    for m in mlist:
        for n in nlist:
            qlist.append(str(m) + n)
    print(qlist)

    m = [str(m) + n for m in mlist for n in nlist]
    print(m)







