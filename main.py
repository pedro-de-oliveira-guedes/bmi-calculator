from modules.bmi_calculator import BmiCalculator

def run_bmi_app():
    weight = input("Enter your weight in kg: ")
    height = input("Enter your height in m: ")

    bmi_calculator = BmiCalculator()
    bmi = bmi_calculator.calculate_bmi(float(weight), float(height))
    print(f"Your BMI is: {bmi}")

    bmi_category = bmi_calculator.get_bmi_category(bmi)
    print(f"You are: {bmi_category}")


if __name__ == "__main__":
    run_bmi_app()