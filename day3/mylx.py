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
    qlist = []
    for i in klist:
        qlist.append(i.strip(' '))
    # print(qlist)

    qset = set()
    for i in qlist:
        qset.add(i)
    print(qset)

    mdict = {}
    for i in qset:
        mdict[i] = qlist.count(i)
    print(mdict)

    for k,v in mdict.items():
        print(k,'出现了',v,'次')










