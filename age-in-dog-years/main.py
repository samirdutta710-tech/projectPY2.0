def main():
    age_str = input("Your age in years: ")
    if not age_str.isdigit():
        print("Please enter a whole number.")
        return
    age = int(age_str)
    dog_years = age * 7
    print(f"In dog years, you are about {dog_years} 🐶")

if __name__ == "__main__":
    main()
