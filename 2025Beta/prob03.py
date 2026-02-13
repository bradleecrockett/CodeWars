import math
# Dictionary to store the operations and a list of all the equations
ops = {"ADD" : '+', "SUBTRACT" : '-', "MULTIPLY" : '*', "DIVIDE" : '/'}
equations: list[str] = []

def op(a:float, b:float, operation:str) -> float:
    if operation == "ADD":
        return a + b
    elif operation == "SUBTRACT":
        return a - b
    elif operation == "MULTIPLY":
        return a * b
    else:
        return a / b

# Get all the equations
while True:
    equation = input()
    if equation == "END": break
    equations.append(equation)

# Iterate through all the equations and check if the output is correct
for equation in equations:
    # Split the equation into the numbers, operation, and output
    equation = equation.split()
    A = float(equation[0])
    B = float(equation[1])
    OP = equation[2]
    OUT = float(equation[3])

    # Calculate the output and check if it is correct
    output: float = math.trunc(op(A, B, OP) * 10) / 10
    if output == OUT:
        print(f"{OUT} is correct for {A} {ops[OP]} {B}")
    else:
        print(f"{A} {ops[OP]} {B} = {output}, not {OUT}")
