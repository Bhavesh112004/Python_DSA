#   for checking the occurance of element of m in n
#   m = [5,3,2,2,1,5,5,7,5,10]
#   n = [10,111,1,9,5,67,2]

def freq_check(m,n):
    for num1 in n:
        count = 0;
        for num2 in m:
            if num1 == num2:
                count = count + 1;

        print(f"{num1}:{count}");

def main():
    lst1 = [5,3,2,2,1,5,5,7,5,10];
    lst2 = [10,111,1,9,5,67,2];

    freq_check(lst1, lst2);

if __name__ == "__main__":
    main()

# but if m contains M elements
# and n contains N elements
# time complexity will be O(M*N)
# if m and n can have 10^8 elements TC = 10^16
# which will throw TLE time limit exceeded error so optimise it