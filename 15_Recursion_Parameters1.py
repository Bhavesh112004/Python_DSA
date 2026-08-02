def func(x,n):
    if n == 0:
        return;
    print(x)
    func(x,n-1)
    
def main():
    x = 15;
    n = 4
    func(x,n)

if __name__ == "__main__":
    main()