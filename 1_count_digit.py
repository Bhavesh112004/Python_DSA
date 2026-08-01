def count_digit(num):
    count = 0;
    while(num > 0):
        num = num // 10;
        count += 1;

    print("The no of digits is: ",count);
        
def main():
    print("Enter the Number : ");
    num = int(input());

    count_digit(num);

if __name__ == "__main__":
    main()


"""
n= 5438
n // 10 = 543
n = 543
n// 10 = 54
n = 54
n // 10 = 5
n = 5
n // 5 = 0
n =0 
terminate loop
iterate 4 times
time complexity = O(log base 10 N)
"""