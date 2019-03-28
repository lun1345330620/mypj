if __name__ == '__main__':
    mlist = [1,2,5,8,7,9,6,4,7]
    nlist = [2,5,4,8,7,6]
    m = [2,5,4]
    nnlist = mlist[2:10:2]

    mm = [[2,5,8],[1,4,7],[3,6,9]]
    print(type(mlist))
    # 在列表末尾添加数据
    mlist.append(50)
    print(mlist)
    # 添加数据
    mlist.insert(3,60)
    print(mlist)
    # 删除
    del mlist[2]
    print(mlist)
    # 从最后一个数据开始删除
    mlist.pop(9)
    print(mlist)
    # 按照指定数据删除
    mlist.remove(8)
    print(mlist)
    # 将指定数据修改
    mlist[0] = 50
    print(mlist)
    # 是否重复 id
    print(id(mlist))
    print(id(nlist))
    # 是否包含在不在
    print(m in mlist)
    print(m not in mlist)
    # 遍历
    for m in mlist:
        print(m,end=',')
    #
    for i in mm:
        for j in i:
            print('nlist[{1}] = {0}'.format(j,j.__index__()))
    # 反转
    mlist.reverse()
    print(mlist)
    #
    mlist.count(6)
    print(mlist)















