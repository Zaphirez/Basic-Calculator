def calc(num1, op, num2):
    if not type(num1) is int:
        raise TypeError("Num1 is NaN!")
    if not type(num2) is int:
        raise TypeError("Num2 is NaN!")
    match op:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "/":
            return num1 / num2
        case "*":
            return num1 * num2


print(calc(1, "+", 2))
