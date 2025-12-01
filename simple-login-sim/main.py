USERNAME = "admin"
PASSWORD = "secret123"

def main():
    print("Simple Login (fake)")
    user = input("Username: ")
    pwd = input("Password: ")

    if user == USERNAME and pwd == PASSWORD:
        print("Login successful!")
    else:
        print("Login failed.")

if __name__ == "__main__":
    main()
