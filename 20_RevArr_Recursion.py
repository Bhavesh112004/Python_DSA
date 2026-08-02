def reverse(arr, left, right):
    if left >= right:
        return

    arr[left], arr[right] = arr[right], arr[left]
    reverse(arr,left+1, right-1)
    return arr

def main():
    num = [5,7,3,2,6,1,5,9]
    left = 0
    right = len(num)-1
    result = reverse(num, 2, 5)
    print(result)


if __name__ == "__main__":
    main()