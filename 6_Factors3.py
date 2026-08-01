def square_root(no):
    i = 0;
    while i * i <= no:
        i += 1;

    return i -1;

def check_factors(no):
    lst = [];
    for i in range (1,square_root(no)+1):
        if (no % i == 0):
            lst.append(i);
            if (no//i != square_root(no)):
                lst.append(no//i);
    
    print(lst);

def main():

    print("Enter the Number: ");
    num = int(input());

    check_factors(num)

if __name__ == "__main__":
    main()