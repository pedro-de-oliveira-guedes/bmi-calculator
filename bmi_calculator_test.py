from bmi_calculator import BmiCalculator

import unittest

class TestBmiCalculator(unittest.TestCase):
    def setUp(self):
        self.bmi_calculator = BmiCalculator()
    
    def test_calculate_bmi_with_non_float_weight(self):
        with self.assertRaises(ValueError):
            self.bmi_calculator.calculate_bmi("weight", 1.75)
    
    def test_calculate_bmi_with_non_float_height(self):
        with self.assertRaises(ValueError):
            self.bmi_calculator.calculate_bmi(70.0, "height")
    
    def test_calculate_bmi_with_negative_weight(self):
        with self.assertRaises(ValueError):
            self.bmi_calculator.calculate_bmi(-70.0, 1.75)

    def test_calculate_bmi_with_negative_height(self):
        with self.assertRaises(ValueError):
            self.bmi_calculator.calculate_bmi(70.0, -1.75)
    
    def test_calculate_bmi_with_valid_values(self):
        self.assertEqual(self.bmi_calculator.calculate_bmi(70.0, 1.75), 22.86)
    
    def test_get_bmi_category_with_non_float_bmi(self):
        with self.assertRaises(ValueError):
            self.bmi_calculator.get_bmi_category("bmi")
    
    def test_get_bmi_category_with_negative_bmi(self):
        with self.assertRaises(ValueError):
            self.bmi_calculator.get_bmi_category(-22.86)
    
    def test_get_bmi_category_with_underweight_bmi(self):
        self.assertEqual(self.bmi_calculator.get_bmi_category(18.49), "Underweight")
    
    def test_get_bmi_category_with_normal_weight_bmi(self):
        self.assertEqual(self.bmi_calculator.get_bmi_category(18.5), "Normal weight")
    
    def test_get_bmi_category_with_overweight_bmi(self):
        self.assertEqual(self.bmi_calculator.get_bmi_category(24.99), "Normal weight")

    def test_get_bmi_category_with_obese_bmi(self):
        self.assertEqual(self.bmi_calculator.get_bmi_category(30.0), "Obese")