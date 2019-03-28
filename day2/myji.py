if __name__ == '__main__':
    strr = input("请输入一个字符串:")
    strs = ""
    for i in range(0,len(strr)):
        if strr.count(strr[i]) >=2:
            if strs.find(strr[i]) == -1:
                strs += strr[i]

    print('原字符串',strr)
    for i in range(0,len(strs)):
        print('重复的字符串',strs[i],'出现的次数',strr.count(strs[i]))
    print('重复的字符串组成的集合',strs[i])