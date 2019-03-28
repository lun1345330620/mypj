import  random
if __name__ == '__main__':
    mystu = [1,5,4,3,1,7,9,8,2]
    # mystu.sort()
    # print(mystu)

    # 降序
    mystu.sort(reverse=True)
    print(mystu)

    # 打乱顺序
    random.shuffle(mystu)

    # 倒着打印
    mystu.reverse()
    print(mystu)
    # 临时排序
    num = sorted(mystu,reverse=True)
    print(num)

    






















