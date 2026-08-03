def checkfibbo(n):
    '''a, b = 0, 1
    for i in range(n):
        print(a, end = " " )
        nth = a + b
        a = b
        b = nth'''

    if n == 0 or n == 1:
        return n

    return checkfibbo(n-1)+checkfibbo(n-2)
        
def main():
    n = 6
    a = 0
    ans = checkfibbo(n)
    print(ans)

if __name__ == "__main__":
    main()