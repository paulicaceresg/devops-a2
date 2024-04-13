import unittest

def calculate_area(length, width):
    return length * width

class TestRectangleArea(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertEqual(calculate_area(5, 10), 50) #expected output is 50
        
    def test_negative_numbers(self):
        self.assertEqual(calculate_area(-5, 10), -50) #expected output is -50
        
    def test_zero_values(self):
        self.assertEqual(calculate_area(0, 10), 0) #expected output is 0
        
    def test_float_inputs(self):
        self.assertAlmostEqual(calculate_area(2.5, 3.5), 8.75) #expected output is 8.75
        
    def test_nonnumeric_inputs(self):
        self.assertRaises(TypeError, calculate_area, 'five', 10) #expected output is TypeError

def main():
    print("Please choose the input you want for length:")
    length = float(input())
    print("Please choose the input you want for width:")
    width = float(input())
    try:
        result = calculate_area(length, width)
        print("\nThe area of a rectangle with length %.2f and width %.2f is %.2f" %(length, width, result))
    except TypeError:
        print("TypeError! Please enter a valid input." )

if __name__ == '__main__':
    main()