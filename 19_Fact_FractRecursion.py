def fact(no):
    if no == 1 or no ==0:
        return 1

    return no*fact(no-1)

def main():
    n = 1
    result = fact(n)
    print(result)


if __name__ == "__main__":
    main()