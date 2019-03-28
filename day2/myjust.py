if __name__ == '__main__':
    m=[1,2,3,4,5,6,7,8,9]
    for i in m:
        for j in m[0:i]:
            print(i,j,sep="*",end="=")
            print(str(i*j).ljust(2),end="   ")
        print()