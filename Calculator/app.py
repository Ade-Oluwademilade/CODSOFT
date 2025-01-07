#!/usr/bin/python3
#  ____                 _ _           _      
# |  _ \  ___ _ __ ___ (_) | __ _  __| | ___ 
# | | | |/ _ \ '_ ` _ \| | |/ _` |/ _` |/ _ \
# | |_| |  __/ | | | | | | | (_| | (_| |  __/
# |____/ \___|_| |_| |_|_|_|\__,_|\__,_|\___|


# Check if the number entered is an integer
def is_int(input_str):
    return input_str.isdigit() or (input_str[0] == '-' and input_str[1:].isdigit())

# Check if the number is a decimal
def is_float(input_str):
    try:
        float(input_str)
        return '.' in input_str
    except ValueError:
        return False



def parse_number(input_str):
    if is_int(input_str):
        return int(input_str)
    elif is_float(input_str):
        return float(input_str)
    else:
        return None


def calculator():                   
    appName = """
      ____      _            _       _                  _                
     / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __     / \   _ __  _ __  
    | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|   / _ \ | '_ \| '_ \ 
    | |__| (_| | | (__| |_| | | (_| | || (_) | |     / ___ \| |_) | |_) |
     \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|    /_/   \_\ .__/| .__/ 
                                                            |_|   |_|      
    """
    print(appName)



    print("Calculator App")
    print("Select an operator:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operator = input("What operation would you like to perform (1-4): ")
    if operator not in ["1", "2", "3", "4"]:
        print("Error! Select a valid operator.")
        return

    # Get input of first number
    num1_input = input("Enter the first number: ")
    num1 = parse_number(num1_input)
    if num1 is None:
        print("Invalid input! Please enter a valid number.")
        return

    # Get input of second number
    num2_input = input("Enter the second number: ")
    num2 = parse_number(num2_input)
    if num2 is None:
        print("Invalid input! Enter a valid number.")
        return

    # Perform the operation
    if operator == "1":
        result = num1 + num2
        operation = "+"
    elif operator == "2":
        result = num1 - num2
        operation = "-"
    elif operator == "3":
        result = num1 * num2
        operation = "*"
    elif operator == "4":
        if num2 == 0:
            print("Error: Cannot divide a number by 0")
            return
        result = num1 / num2
        operation = "/"
    
    # Display result
    print(f"The result of {num1} {operation} {num2} is: {result}")

if __name__ == "__main__":
    calculator()