#   s = azyxyyzaaaa
#   q = ["a","d","y","x"]
# contraint s contains only small letters

def string_check(s,q):
    hash_list = [0]*26;
    for ch in s:
        ascii_value = ord(ch);
        index = ascii_value -97;
        hash_list[index] += 1;

    for ch in q:
        ascii_value = ord(ch);
        index = ascii_value - 97
        print(hash_list[index]);

def main():
    str1 = "azyxyyzaaaa";
    char1 = ["a","d","y","x"];

    string_check(str1, char1);

if __name__ == "__main__":
    main()