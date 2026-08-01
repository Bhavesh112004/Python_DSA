#   for checking the occurance of element of m in n
#   m = [5,3,2,2,1,5,5,7,5,10]
#   n = [10,111,1,9,5,67,2]

def freq_check(m,n):
    hash_list = [0]*11;
    for num in m:
        hash_list[num] +=1;

    for num in n:
        if num<1 or num>10:
            print(0)
        else:
            print(hash_list[num])
 
def main():
    lst1 = [5,3,2,2,1,5,5,7,5,10];
    lst2 = [10,111,1,9,5,67,2];

    freq_check(lst1, lst2);

if __name__ == "__main__":
    main()

# but if m contains M elements
# and n contains N elements
# 1<=n[i]<=10
# time complexity will be O(M+N)
# if m and n can have 10^8 elements it will take 2*10^8 approx 10*8
