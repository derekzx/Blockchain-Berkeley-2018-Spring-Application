# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# For example,
#
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = -2, denominator = 1, return "-2".
# Given numerator = 2, denominator = 3, return "0.(6)".
# Given numerator = 5, denominator = 2, return "2.5".

def divide(numerator, denominator):
    result = ""

    if numerator < 0 or denominator < 0:
        result = "-"

    abs_num, abs_denom = abs(numerator), abs(denominator)
    quotient, remainder = divmod(abs_num, abs_denom)

    if remainder == 0:
        result += str(quotient)
        return result
    else:
        result += (str(quotient) + ".")
        passed = {}
        i = len(result)
        while remainder:
            if remainder not in passed.keys():
                passed[remainder] = i
            else:
                i=passed[remainder]
                result = result[:i] + "(" + result[i:] + ")"
                return result
            remainder *= 10
            result += str(remainder//abs_denom)
            remainder %= abs_denom
            i += 1
        return result
