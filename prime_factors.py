def factors(value):
    divisor = 2
    divisors = []
    if value > 1:

        while value != divisor:
            if value % divisor == 0:
                divisors.append(divisor)
                value = value // divisor
            else:
                divisor += 1
        divisors.append(divisor)
    return divisors
