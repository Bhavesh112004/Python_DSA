def bubble_sort(arr):
    n = len(arr)
    for i in  range(n-2,-1,-1):
        is_swapped = False
        for j in range(0,i+1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
                is_swapped = True

        if is_swapped == False:
            break
            

    return arr

def main():
    nums = [1,4,2,5,8,5,14,8,0]
    sorted_array = bubble_sort(nums)
    print(sorted_array)
    

if __name__ == "__main__":
    main()