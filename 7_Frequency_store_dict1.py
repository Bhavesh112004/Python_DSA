# Frequncy Map

def Frequency_map(nums,x):
    freq_map = {};
    for i in range(0, len(nums)):
        if nums[i] in freq_map:
            freq_map[nums[i]] +=1;
        else:
            freq_map[nums[i]] = 1;

    print(f"The no occured {freq_map[x]} times in the list")

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