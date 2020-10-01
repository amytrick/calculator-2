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
            subtract(token1, token2)
        elif tokens[0] == "*":
            multiply(token1, token2)
        elif tokens[0] == "/":
            divide(token1, token2)
        elif tokens[0] == "square":
            square(token1)
        elif tokens[0] == "cube":
            cube(token1)
        elif tokens[0] == "pow":
            power(token1, token2)
        elif tokens[0] == "mod":
            mod(token1, token2)