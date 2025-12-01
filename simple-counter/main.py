def main():
    n_str = input("Count up to: ")
    if not n_str.isdigit():
        print("Please enter a positive integer.")
        return
    n = int(n_str)
    for i in range(1, n + 1):
        print(i)

if __name__ == "__main__":
    main()
