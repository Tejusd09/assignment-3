def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers"
    
    if number == 0:
        return 1
    
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def main():
    print("Factorial Calculator")
    print("-------------------")
    
    try:
        num = int(input("Enter a non-negative integer: "))
        
        result = factorial(num)
        
        print(f"\nFactorial of {num} is: {result}")
        
        if isinstance(result, int) and num <= 10 and num > 0:
            calculation = " × ".join(str(i) for i in range(1, num + 1))
            print(f"Calculation: {calculation} = {result}")
            
    except ValueError:
        print("Error: Please enter a valid integer!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()