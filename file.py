def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation!")
                continue
                
            print(f"Result: {num1} {op} {num2} = {result}")
            
            again = input("Calculate again? (yes/no): ").lower()
            if again != 'yes':
                print("Goodbye!")
                break
                
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            
if __name__ == "__main__":
    calculator()
