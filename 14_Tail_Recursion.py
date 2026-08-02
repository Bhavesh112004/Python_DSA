def func(count):
    if count == 4:
        return;
    count += 1;
    func(count);
    print("Hello");

def main():

    func(0);

if __name__ == "__main__":
    main()