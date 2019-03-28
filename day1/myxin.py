if __name__ == '__main__':
    i={1,2,3,4,5,6,7,8,9}
    for m in i:
        for n in i:
            print(str(m)+"*"+str(n)+"="+str(m*n),end=" ")
            if m==n:
                print()
                break