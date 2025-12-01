def print_table(n: int):
    print(f"\nMultiplication Table up to {n}")
    header = "    " + " ".join(f"{i:3d}" for i in range(1, n + 1))
    print(header)
    print("   " + "-" * (4 * n))
    for row in range(1, n + 1):
        line = f"{row:2d}|"
        for col in range(1, n + 1):
            line += f"{row * col:4d}"
        print(line)

def main():
    num_str = input("Generate table up to (e.g. 10): ")
    if not num_str.isdigit():
        print("Please enter a positive integer.")
        return
    n = int(num_str)
    if n <= 0:
        print("Number must be positive.")
        return
    print_table(n)

if __name__ == "__main__":
    main()
