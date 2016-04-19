def solve(x, y, z, lis):
    w = int_check(lis)
    if w:
        minus_b = float(y) * float(-1)
#        print('minus_b = ' + str(minus_b))
        b_squared = pow(float(y), 2.0)
#        print('b_squared = ' + str(b_squared))
        four_a_c = 4 * float(x) * float(z)
#        print('four_a_c = ' + str(four_a_c))
        two_a = 2 * float(x)
#        print('two_a = ' + str(two_a))
        to_be_square_root = b_squared - four_a_c
        square_root = pow(float(to_be_square_root), 0.5)
        var1 = minus_b + square_root
        var2 = minus_b - square_root
        var3 = var1/two_a
        var4 = var2/two_a
        plus_answer = 'x1 = ' + str(var3)
        minus_answer = 'x2 = ' + str(var4)
        solutions = [plus_answer, minus_answer]
        sol = ', '.join(solutions)
        return sol
    else:
        print('There were one or more invalid inputs.')


# Welcome Message
print('Welcome to the Quadratic Formula calculator.')
print('The Quadratic Formula is -b ± √b^2 - 4ac / 2a.')

# Inputs
a, b, c = input('Please enter your values: ').split(',')
abc = [a, b, c]


def int_check(lis):
    for i in lis:
        try:
            float(i)
            return True
        except ValueError:
            return False


print(solve(a, b, c, abc))
