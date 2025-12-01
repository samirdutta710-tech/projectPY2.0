import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(t + "\n")

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet. 🎉")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do CLI")
        print("1. List tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
        elif choice == "3":
            list_tasks(tasks)
            num = input("Enter task number to remove: ")
            if num.isdigit():
                idx = int(num) - 1
                if 0 <= idx < len(tasks):
                    tasks.pop(idx)
                    save_tasks(tasks)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
