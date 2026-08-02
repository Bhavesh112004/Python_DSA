def func(i,n):
    if n < i:
        return
    #print(i)
    #func(i+1,n)
    func(i,n-1)
    print(n)

def main():
    n = 10
    func(1,n)

if __name__ == "__main__":
    main()