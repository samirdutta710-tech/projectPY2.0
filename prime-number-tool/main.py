def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def list_primes(limit: int):
    return [n for n in range(2, limit + 1) if is_prime(n)]

def main():
    while True:
        print("\nPrime Number Tool")
        print("1. Check if a number is prime")
        print("2. List primes up to N")
        print("3. Quit")
        choice = input("Choose: ")

        if choice == "1":
            num_str = input("Enter a number: ")
            if not num_str.lstrip("-").isdigit():
                print("Please enter an integer.")
                continue
            n = int(num_str)
            if is_prime(n):
                print(f"{n} is prime.")
            else:
                print(f"{n} is NOT prime.")
        elif choice == "2":
            limit_str = input("List primes up to: ")
            if not limit_str.isdigit():
                print("Please enter a positive integer.")
                continue
            limit = int(limit_str)
            primes = list_primes(limit)
            print("Primes:", primes)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
