def func(n):
    if n ==1:
        return 1

    return n+func(n-1)

def main():
    n = 10
    result = func(n)
    print(result)

if __name__ == "__main__":
    main()