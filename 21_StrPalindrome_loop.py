def CheckPalindrome(string, left, right):
    while left < right:
        if string[left] != string[right]:
            return False

        left +=1
        right -=1

    return True

def main():
    string = "nabcde"
    left = 0
    right = len(string)-1
    Result = CheckPalindrome(string, left, right)
    if Result == True:
        print("Palindrome")

    else:
        print("Not palindrome")


if __name__ == "__main__":
    main()