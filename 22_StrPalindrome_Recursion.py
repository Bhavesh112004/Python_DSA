def CheckPalindrome(string, left, right):
    if left >= right:
        return True
    
    if string[left] != string[right]:
        return False
        
    return CheckPalindrome(string, left+1, right-1)


def main():
    string = "naveevan"
    left = 0
    right = len(string)-1
    Result = CheckPalindrome(string, left, right)
    if Result == True:
        print("Palindrome")

    else:
        print("Not palindrome")


if __name__ == "__main__":
    main()