if __name__ == '__main__':
    b = []
    for i in range(10):
        if i == 0:
            print([1])
        else:
            b = [1] + [b[i] + b[i + 1] for i in range(len(b) - 1)] + [1]
            print(b)