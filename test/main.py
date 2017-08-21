
def main():
    nums = []
    a = int(raw_input(""))

    while a != 42:
        nums.append(a)
        a = int(raw_input(""))

    for num in nums:
        print(num)

if __name__ == '__main__':
    main()
