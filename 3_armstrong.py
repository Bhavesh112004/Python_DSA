def count_digit(iNo1):
    count = 0;
    while iNo1 > 0:
        iNo1 = iNo1 // 10;
        count = count + 1;

    return count;

def check_armstrong(iNo):
    digit_count = count_digit(iNo);
    total = 0;
    while iNo > 0:
        digit = iNo % 10;
        total = total + digit ** digit_count;
        iNo = iNo // 10

    return total;

def main():

    print("Enter the Number: ")
    num = int(input());
    temp = num;

    No_check = check_armstrong(num);

    if (No_check == temp):
        print("Armstrong");

    else: 
        print("Not Armstrong");

if __name__ == "__main__":
    main()