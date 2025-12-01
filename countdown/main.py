import time

def main():
    n_str = input("Start countdown from: ")
    if not n_str.isdigit():
        print("Please enter a positive integer.")
        return
    n = int(n_str)
    for i in range(n, -1, -1):
        print(i)
        time.sleep(1)
    print("Done!")

if __name__ == "__main__":
    main()
