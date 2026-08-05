def Insertion_Sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = key

    return arr

def main():
    nums = [3,5,6,4,8,9,10,7,1]
    sorted_list = Insertion_Sort(nums)
    print(sorted_list)

if __name__ == "__main__":
    main()
