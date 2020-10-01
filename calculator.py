"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input ("Enter your Equation : ")
    tokens = user_input.split(" ")
    print (tokens)
    if tokens[0] == "q":
        print("ITS BROKEN")
        break
    else:
        token1 = int(tokens[1])
        token2 = int(tokens[2])
        if tokens[0] == "+":
            print(add(token1, token2))
        elif tokens[0] == "-":
            print(subtract(token1, token2))
        elif tokens[0] == "*":
            print(multiply(token1, token2))
        elif tokens[0] == "/":
            print(divide(token1, token2))
        elif tokens[0] == "square":
            print(square(token1))
        elif tokens[0] == "cube":
            print(cube(token1))
        elif tokens[0] == "pow":
            print(power(token1, token2))
        elif tokens[0] == "mod":
            print(mod(token1, token2))