"""Calculate body mass index from metric measurements."""


def main():
    try:
        weight = float(input("Weight (kg): "))
        height = float(input("Height (m): "))
        if weight <= 0 or height <= 0:
            raise ValueError
    except ValueError:
        print("Use positive numeric values.")
        return
    bmi = weight / height**2
    category = "underweight" if bmi < 18.5 else "healthy range" if bmi < 25 else "overweight" if bmi < 30 else "obese range"
    print(f"BMI: {bmi:.1f} ({category})")


if __name__ == "__main__":
    main()
