import day4.mypro04 as d1
import day4.mypro05 as d2
import day4.mypro06 as d3
import day4.mypro07 as d4
if __name__ == '__main__':
    mdict = {
        '1':'[1]输入用户姓名及性别，然后给出下列的提示',
        '2':'[2]随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集',
        '3':'[3]注意一个用户信息，包含EMAIL号，判断信息是否合法，如果合法则输出相关信息（姓名长度不能少于6位，邮件中包含@）',
        '4':'[4]从键盘输入一行字符串，判断是否是回文数',
    }
    mfundict = {
        1:d1.dl,
        2:d2.dd,
        3:d3.dd,
        4:d4.dd
    }
    while True:
        for i in mdict.values():
            print(i)
        num = int(input('输入功能编号'))
        mfundict[num]()










