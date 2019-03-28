if __name__ == '__main__':
    mdict = {}

    klist = ['name','age','password']
    vlist = ['aaa','bbb','ccc']

    for i in mdict:
        mdict[i] = klist[vlist.index(i)]

    print(mdict)