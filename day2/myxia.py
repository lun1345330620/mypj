if __name__ == '__main__':
    num = [1,5,6,7,9,8,4,6,3]
    # 排序
    num.sort()
    print(num)

    # 反转
    num.reverse()
    print(num)

    # 临时排序，倒叙
    n = sorted(num,reverse=True)
    print(n)

    # 添加
    num.append(80)
    print(num)

    # 添加插入
    num.insert(5,90)
    print(num)

    # 从最后一位开始删除
    num.pop()
    print(num)

    # 删除指定元素
    num.remove(7)
    print(num)

    # 根据索引删除
    del num[3]
    print(num)










