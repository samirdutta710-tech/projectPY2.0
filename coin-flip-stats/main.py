import random

def flip_coin():
    return random.choice(["H", "T"])

def main():
    print("🪙 Coin Flip Stats")
    n_str = input("How many flips? ").strip()
    if not n_str.isdigit():
        print("Please enter a positive integer.")
        return
    n = int(n_str)

    heads = 0
    tails = 0
    for _ in range(n):
        result = flip_coin()
        if result == "H":
            heads += 1
        else:
            tails += 1

    print(f"\nTotal flips: {n}")
    print(f"Heads: {heads}")
    print(f"Tails: {tails}")

if __name__ == "__main__":
    main()
