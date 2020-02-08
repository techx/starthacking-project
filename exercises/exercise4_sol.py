# Exercise 4a Solutions
def quadratic(x):
    # Example quadratic: f(x) = 2x^2+3x+1
    return 2*x**2 + 3*x + 1

print(quadratic(2))


# Exercise 4b Solution
def quadratic():
    # Example quadratic: f(x) = 2x^2+3x+1-
    x = int(input("Pick a value for x: "))
    return 2*x**2 + 3*x + 1

quadratic()