# 单行注释
''' 多行注释 '''
if __name__ == '__main__':
    while True:
        hehe = input('你是谁')
        if hehe == 'q':
            break
        else:
           i = 0
        while i<10:
            if i % 2==0:
                print('偶数')
            else:
                print('积数')
                i+=1

    myarr = [1,2,3,4,5]
    for m in myarr:
        print(m)