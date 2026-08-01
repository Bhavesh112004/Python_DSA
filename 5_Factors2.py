def check_factors(no):
    lst = [];
    for i in range (1,(no//2)+1):
        if (no % i == 0):
            lst.append(i);
    lst.append(no);
    print(lst);

def main():

    print("Enter the Number: ");
    num = int(input());

    check_factors(num)

if __name__ == "__main__":
    main()