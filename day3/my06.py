if __name__ == '__main__':
    for y in range(30, -30, -1):
        mlist = []
        for x in range(-30, 30):
            if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0:
                mlist.append("*")
            else:
                mlist.append(" ")
            s = "".join(mlist)
        print(s)
        print('\033[1;35;0m\033[0m')

