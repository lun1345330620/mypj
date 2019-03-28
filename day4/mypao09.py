import random

if __name__ == '__main__':
    mlist = [random.randint(0,50) for a in range(50)]
    print(mlist)

    nlist =mlist[::2]
    print("奇数下标切片后：",nlist)
    nlist.sort()
    print("排序后：",nlist)

