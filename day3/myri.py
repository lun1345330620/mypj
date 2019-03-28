if __name__ == '__main__':
    mlist = input('请输入:')
    mset = set(mlist)
    if mlist.__len__() == mset.__len__():
        pass
    else:
        for i in mset:
            if mlist.count(i) >= 2:
                print('重复的出现了',mlist.count(i),'次')
