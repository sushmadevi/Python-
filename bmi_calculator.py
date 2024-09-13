# bmi_calculator.py

def calculate_bmi(weight, height_cm):
    # Convert height from cm to meters
    height_m = height_cm / 100
    # Calculate BMI
    bmi = weight / (height_m ** 2)
    return bmi

def categorize_bmi(bmi):
    # Categorize BMI based on given ranges
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    # Input weight and height from user
    weight = float(input("Enter your weight in kg: "))
    height_cm = float(input("Enter your height in cm: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height_cm)
    
    # Categorize and display BMI
    category = categorize_bmi(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are categorized as: {category}")

if __name__ == "__main__":
    main()