# Frequncy Map

def Frequency_map(nums,x):
    hash_map = {};
    for i in range(0, len(nums)):
        hash_map[nums[i]] = hash_map.get(nums[i],0)+1;

    print(f"The no occured {hash_map[x]} times in the list");

def main():
    print("Enter the length of the list: ");
    n = int(input());
    
    lst = [];
    print("Enter the elements in the list");
    for i in range (n):
        ele = int(input());
        lst.append(ele);

    print("Enter the number to know its occurance: ")
    x = int(input());

    Frequency_map(lst,x);

if __name__ == "__main__":
    main()