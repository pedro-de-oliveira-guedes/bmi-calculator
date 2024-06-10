class BmiCalculator:
    def calculate_bmi(self, weight: float, height: float) -> float:
        # Check if weight and height are actually float values
        if not isinstance(weight, float):
            raise ValueError("Weight must be a float value")
        if not isinstance(height, float):
            raise ValueError("Height must be a float value")
        
        # Check if weight and height are positive values
        if weight <= 0:
            raise ValueError("Weight must be a positive value")
        if height <= 0:
            raise ValueError("Height must be a positive value")
        
        return weight / (height ** 2)