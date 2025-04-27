def derivative_of_polynomial(eq: str) -> str:
    import re

    # Regular expression to match terms in the polynomial
    my_regexp = (r'(?P<sign>[+\-]?)'
                 r'(?P<coeff>\d*)'
                 r'x'
                 r'(?:\^(?P<exp>\d+))?')

    # Helper function to convert string to integer, defaulting to 1 if empty
    def as_int(s):
        return int(s) if s else 1

    result = ''
    # Iterate over each term in the polynomial
    for monom in re.finditer(my_regexp, eq):
        sign, coeff, exp = monom.groups()
        coeff, exp = list(map(as_int, (coeff, exp)))
        coeff *= exp  # Multiply coefficient by exponent
        exp -= 1      # Decrease exponent by 1
        # Format the term based on the new exponent
        result += ('{sign}{coeff}' if exp == 0 else 
                   '{sign}{coeff}x' if exp == 1 else
                   '{sign}{coeff}x^{exp}'
                  ).format(sign=sign, coeff=coeff, exp=exp)
    # Return the result or '0' if the result is empty
    return result if result else '0'

