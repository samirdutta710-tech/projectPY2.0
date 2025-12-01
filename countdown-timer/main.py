import time

def countdown(seconds: int):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("00:00")
    print("⏰ Time's up!")

def main():
    user = input("Enter time in seconds: ")
    if not user.isdigit():
        print("Please enter a valid number.")
        return
    countdown(int(user))

if __name__ == "__main__":
    main()
