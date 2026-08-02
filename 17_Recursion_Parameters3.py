def func(sum, i, n):
    if i > n:
        print(sum)
        return
    func(sum+i, i+1, n)

def main():
    n = 10
    func(0,1,n)

if __name__ == "__main__":
    main()