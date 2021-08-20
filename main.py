from sympy import *


def first_condition(nums, f):
    for num in nums:
        if f(num) < nums[0] or f(num) > nums[1]:
            return false
    return true

def second_condition(nums, f_prime):
    for i in range(len(nums)):
        if i <= 1:
            continue
        # a and b are not in this interval

        if f_prime(nums[i]) <= -1 or f_prime(nums[i]) >= 1:
            return false
    return true

#f is out g(x)
#steps is the length of our series
#x is the first input (x_0)
def generate_series(f, steps, x):
    i = 0
    while steps>(-1):
        print("x_",i,"= ",x) #print x_i of series
        x=f(x)
        i+=1
        steps-=1

    print("The END!")


if __name__ == '__main__':
    # Help
    print("Ex: (x^2+x^(1/3))*(1/2); (use ^ for power)")
    print("Ex: exp(x^2)^(1/3); (use exp(x) for e^x)")
    print("Ex: sin(x)+cos(x^2); (use sin(x) and cos(x) for sin and cos)")
    # variable of function
    x = symbols('x')

    # expr is the function & f is lambdify
    expr = sympify(input("g(x) = ").replace('^', '**'))
    #print(expr)
    f = lambdify(x, expr)

    # expr_prime is the derivation of function & f_prime is lambdify
    expr_prime = expr.diff(x)
    f_prime = lambdify(x, expr_prime)


    # Enter endpoints of the Interval
    a, b = input("Enter endpoints of the Interval\nSeperate them with whitespace: ").split()
    a = float(a)
    b = float(b)

    true_conditions = 0 #count of true conditions

    # Check the First condition
    f_prime_answers = solve(expr_prime, x)
    for i in f_prime_answers:
        if i < a or i > b:
            f_prime_answers.remove(i)
    f_prime_answers = [a, b] + f_prime_answers
    if first_condition(f_prime_answers, f):
        print("First Condition is true!")
        print("We have at least 1 fixed point in [{}, {}]".format(a, b))
        true_conditions += 1
    else:
        print("First condition is not true!")
        exit(0)


    # Check the Second condition
    f_2primes_answers = solve(expr_prime.diff(x), x)
    for i in f_2primes_answers:
        if i < a or i > b:
            f_2primes_answers.remove(i)
    f_2primes_answers = [a, b] + f_2primes_answers
    if second_condition(f_2primes_answers, f_prime):
        print("Second Condition is true!")
        print("We have a unique fixed point in [{}, {}]".format(a, b))
        true_conditions += 1
    else:
        print("Second condition is not true!")
        exit(0)

    # Enter number of iteration for the Sequence And print the Sequence
    if true_conditions == 2:
        #get the steps of the series
        steps = int(input("Enter the length of Sequence (number of steps)(print until x_steps): "))
        #get the first input (x_0)
        x0 = float(input("Enter X_0: "))
        # check if x_0 is in the interval
        if x0>=a and x0<=b :
            generate_series(f,steps,x0) # if x_0 is in the interval run the function to generate the series
        else:
            print("x_0 is out of interval of g(x)") # if x_0 is not in the interval print error
            exit(0)
    else:
        print("conditions are not valid!") # if conditations are not valid print error
        exit(0)