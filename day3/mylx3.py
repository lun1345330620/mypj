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

    nlist = []
    for i in klist:
        nlist.append(i.strip(' '))
    print(nlist)

    mset = set()
    for i in nlist:
        mset.add(i)
    print(mset)

    mdict = {}
    for i in mset:
        mdict[i] = nlist.count(i)
    print(mdict)

    for k,v in mdict.items():
        print(k,'出现了',v,'次')