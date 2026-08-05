def merge_array(left, right):
    n = len(left)
    m = len(right)
    result = []
    i,j = 0,0
    while i<n and j<m:
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        
        else:
            result.append(right[i])
            j += 1

    if i<n:
        while i<n:
            result.append(left[i])
            i += 1

    if j<m:
        while j<m:
            result.append(right[j])
            j += 1

    return result

def merge_sort(arr):
    if len(arr) <=1:
        return arr
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    sorted_array= merge_array(left, right)

    return sorted_array

def main():
    nums = [3,1,2,4,1,5,2,6,4]
    sorted_array = merge_sort(nums)
    print(sorted_array)

if __name__ == "__main__":
    main()