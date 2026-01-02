import math

def main():
    print("Math Module Calculations")
    print("-----------------------")
    
    try:
        num = float(input("Enter a number: "))
        
        print(f"\nCalculations for number: {num}")
        print("-" * 40)
        
        if num >= 0:
            sqrt_result = math.sqrt(num)
            print(f"Square root: √{num} = {sqrt_result:.4f}")
        else:
            print(f"Square root: √{num} = Undefined (cannot calculate square root of negative number)")
        
        if num > 0:
            log_result = math.log(num)
            print(f"Natural logarithm: ln({num}) = {log_result:.4f}")
        else:
            print(f"Natural logarithm: ln({num}) = Undefined (logarithm is defined only for positive numbers)")
        
        sine_result = math.sin(num)
        print(f"Sine (in radians): sin({num}) = {sine_result:.4f}")
        
        print("\n" + "-" * 40)
        print("Additional Information:")
        print(f"The number in degrees: {math.degrees(num):.2f}°")
        print(f"Cosine (in radians): cos({num}) = {math.cos(num):.4f}")
        print(f"Tangent (in radians): tan({num}) = {math.tan(num):.4f}")
        
    except ValueError:
        print("Error: Please enter a valid number!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()