import time

def main():
    print("Simple Stopwatch")
    print("Commands: 'start', 'stop', 'reset', 'quit'")
    start_time = None
    elapsed = 0.0

    while True:
        cmd = input("> ").strip().lower()

        if cmd == "start":
            if start_time is None:
                start_time = time.time()
                print("Started.")
            else:
                print("Already running.")
        elif cmd == "stop":
            if start_time is not None:
                elapsed += time.time() - start_time
                start_time = None
                print(f"Stopped at {elapsed:.2f} seconds.")
            else:
                print("Not running.")
        elif cmd == "reset":
            start_time = None
            elapsed = 0.0
            print("Reset.")
        elif cmd == "quit":
            if start_time is not None:
                elapsed += time.time() - start_time
            print(f"Total time: {elapsed:.2f} seconds.")
            break
        else:
            if start_time is not None:
                current = elapsed + (time.time() - start_time)
            else:
                current = elapsed
            print(f"Unknown command. Elapsed: {current:.2f} seconds.")

if __name__ == "__main__":
    main()
