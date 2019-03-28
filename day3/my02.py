def run():
    for i in range(1, 10):
        for j in range(1, 10):
            print(str(i), '*', str(j), '=', str(i * j).ljust(2), end='  ')
            if i == j:
                print()
                break


def run1():
    for i in range(1,10):
        print(str(i).ljust(3),end=" ")
        if i%9 == 0:
            print('\n')
if __name__ == '__main__':
    pass
