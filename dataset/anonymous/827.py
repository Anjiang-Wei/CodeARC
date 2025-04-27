def solution(temp):
    def convert_to_celsius(temperature):
        # Correct formula to convert Fahrenheit to Celsius
        celsius = (temperature - 32) * (5.0 / 9.0)
        return celsius

    c = convert_to_celsius(temp)
    # Check if the temperature is freezing or above
    if c <= 0:
        return f"{c} is freezing temperature"
    else:
        return f"{c} is above freezing temperature"

