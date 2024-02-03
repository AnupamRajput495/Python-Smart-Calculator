def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            print("Sorry, can't divide by zero! Try again with a non-zero divisor.")
            return None
    else:
        print("Invalid operator! Try +, -, *, or /.")
        return None

def main():
    expression = input("Enter expression (e.g., 2+3*4): ")

    operands = []
    operators = []

    current_operand = ""
    for char in expression:
        if char.isdigit() or (char == '.' and current_operand.count('.') < 1):
            current_operand += char
        elif char in ['+', '-', '*', '/']:
            if current_operand:
                operands.append(float(current_operand))
                current_operand = ""
            operators.append(char)

    if current_operand:
        operands.append(float(current_operand))

    if len(operators) + 1 != len(operands):
        print("Invalid expression! Make sure the number of operators matches the number of operands.")
        return

    result = operands[0]
    for i in range(len(operators)):
        result = calculate(result, operands[i + 1], operators[i])

        if result is None:
            return
    
    print(f"Result: {result:.2f}")

if __name__ == "__main__":
    main()