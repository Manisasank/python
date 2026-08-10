def safe_calculate(a, b, operator):
# Dynamic typing: 'a' and 'b' can be int, float, or numeric strings
    a, b = float(a), float(b)
    operations = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a / b if b != 0 else None,
    }
    result = operations.get(operator)
    if result is None:
        return "Error: invalid operator or division by zero"
    return result
print(safe_calculate(10, "4", "/"))   # 2.5
print(safe_calculate(5, 0, "/"))      # Error message