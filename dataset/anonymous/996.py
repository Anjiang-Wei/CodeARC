def solution(a, b, res):
    return {
        a + b: "addition",
        a - b: "subtraction",
        a * b: "multiplication",
        a / b: "division"
    }.get(res, "invalid result")

