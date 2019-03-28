if __name__ == '__main__':
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]
    # 去除两边的空格
    vlist = []
    for i in klist:
        vlist.append(i.strip(' '))
    print(vlist)
    # 将vlist列表放到set集合里 病遍历
    mset = set()
    for i in vlist:
        mset.add(i)
    print(mset)
    # 将set集合放到字典里面
    mdict = {}
    for i in mset:
        mdict[i] = vlist.count(i)
    print(mdict)
    # 打印输出每个元素出现的次数
    for k,v in mdict.items():
        print(k,'出现了',v,'次')





