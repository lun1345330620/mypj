
def user(name,pwd):
    print('name={0}'.format(name))
    print('pwd={0}'.format(pwd))

def user1(name,pwd='222'):
    print('name = {0}'.format(name))
    print('pwd = 123'.format(pwd))

def user2 (name, pwd, nakename=''):
    print('name={0}'.format(name))
    print('pwd={0}'.format(pwd))

def user3 (name,pwd,nakename=''):
    if nakename:
        u1 = {'name':name,'pwd':pwd,'nakename':nakename}
    else:
        u1 = {'name':name,'pwd':pwd}
    return u1

def getname(names):
    for i in names:
        print(i)

def getn(names):
    names.append('gun')
    names = ['good','luck','to','me']


if __name__ == '__main__':

    user(name='高波',pwd='123')

    user1(name='hehe')

    user2(name='高波',pwd='111')
    user2(name='高波1',pwd='222',nakename='傻缺')

    u = user3('高波','1234',nakename='gg')
    print(u)

    names = ['good','luck','to','me']
    getname(names)

    getn(names)
    print(names)

