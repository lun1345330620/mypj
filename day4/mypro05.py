def dd():
    qlist = [i for i in range(1,10)]
    nlist = [j for j in range(1,15)]
    mset = {m for m in qlist}
    nset = {n for n in nlist}
    mm = mset|nset
    print('并集',mm)
if __name__ == '__main__':
    pass







