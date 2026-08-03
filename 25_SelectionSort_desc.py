def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        max_index = i
        for j in range(i+1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr
                

def main():
    nums = [1,4,8,3,2,7,4,6]
    sorted_array = selection_sort(nums)
    print(sorted_array)

if __name__ == "__main__":
    main()