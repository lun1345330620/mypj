if __name__ == '__main__':
    name = "good"
    age = 18
    addr = "beijing"
    #默认print的使用方式
    print(name, age, addr, sep="-", end="======")
    #替换行尾的换行，输出不换行，用end参数实现
    print(name, age, addr, end="")
    #参数之间去掉分隔符（一个 空格）
    print(name, age, addr, sep="")













