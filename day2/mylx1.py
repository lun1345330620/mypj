if __name__ == '__main__':
    # 存储控制台输入的字符串
    strr = input("请任意输出一串字符串")
    # strs用来存储重复过的字符串
    strs = ""
    # 以字符串长度遍历该字符串
    for i in range(0,len(strr)):
        # 判断每个字符在此字符串中是否重复
        if strr.count(strr[i]) >= 2:
            # 判断是否加入过存储的字符串
            if strs.find(strr[i]) == -1 :
                # 如果没存在加入该字符串中
                strs += strr[i];

    print("原字符串：",strr)
    # 将得到的字符串集遍历
    for i in range(0, len(strs)):
        print("重复过的字符为",strs[i],"  出现的次数为：",strr.count(strs[i]))

    print("重复过的字符组成的字符串集合为：",strs)