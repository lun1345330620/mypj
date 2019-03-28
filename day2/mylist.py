if __name__ == '__main__':
    #mlist = list()   # mlist = []  创建列表的方式  两种
    mlist = list()    # mlist = []
    print(type(mlist))

    mlist.append('啦啦')
    print(mlist)

    mlist.insert(1,'傻缺')
    print(mlist)


    mlist.append('傻屌')
    print(mlist)

    mlist.insert(1,'抽')
    print(mlist)

    mlist.pop()
    print(mlist)


    mlist.remove('抽')
    print(mlist)


    del mlist[0]
    print(mlist)


    del mlist






















