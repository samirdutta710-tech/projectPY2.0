def calculate_bmi(weight_kg: float, height_m: float) -> float:
    return weight_kg / (height_m ** 2)

def bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("⚖️ BMI Calculator")
    try:
        weight = float(input("Weight (kg): "))
        height = float(input("Height (m): "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if height <= 0:
        print("Height must be positive.")
        return

    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    print(f"\nYour BMI is {bmi:.1f} ({category})")

if __name__ == "__main__":
    main()
