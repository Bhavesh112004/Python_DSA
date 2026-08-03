def selection_sort(arr):
    n = len(arr)
    for i in range(0,n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index]= arr[min_index], arr[i]

    return arr
            
def main():
    nums = [1,2,8,4,5,6,9,7]
    sorted_array = selection_sort(nums)
    print(sorted_array)

if __name__ == "__main__":
    main()