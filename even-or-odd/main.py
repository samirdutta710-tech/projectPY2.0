def main():
    n_str = input("Enter an integer: ")
    if not n_str.lstrip("-").isdigit():
        print("That is not an integer.")
        return
    n = int(n_str)
    if n % 2 == 0:
        print(f"{n} is even.")
    else:
        print(f"{n} is odd.")

if __name__ == "__main__":
    main()
