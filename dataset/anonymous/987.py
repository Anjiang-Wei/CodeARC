def solution(s):
    import re
    # Regular expression to match substrings in alphabetical order
    reg = re.compile('a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*')
    # Find all matches and return the longest one
    return max(reg.findall(s), key=len)

