def check_palindrome(no):
    result = 0;
    while (no > 0):
        digit = no % 10;
        result = (result * 10)+ digit;
        no = no // 10;

    return result;

def main():
    print("Enter the Number: ");
    num = int(input());
    temp = num;
    No = check_palindrome(num);
    if (No == temp):
        print("Palindrome");
    else:
        print("Not Palindrome");

if __name__ == "__main__":
    main()

# time complexity = O(log base 10(N))