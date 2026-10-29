import re


def binary(n, bits):
    return format(n & ((1 << bits) - 1), f'0{bits}b')


expression = input("Enter expression: ").strip()

pattern = r'\(*\s*\(?\s*([+-]?\d+)\s*\)?\s*([+-])\s*\(\s*([+-]?\d+)\s*\)\s*\)*'
match = re.fullmatch(pattern, expression)

if not match:
    print("Invalid expression format.")
    raise SystemExit

a = int(match.group(1))
op = match.group(2)
b = int(match.group(3))

result = a + b if op == '+' else a - b

print("\nOperand 1:", a)
print("Binary (8-bit):", binary(a, 8))

print("Operand 2:", b)
print("Binary (8-bit):", binary(b, 8))

print("Result (decimal):", result)
print("Result (16-bit binary):", binary(result, 16))
print("Result (8-bit binary):", binary(result, 8))

overflow = result < -128 or result > 127
print("8-bit Arithmetic Overflow:", "Yes" if overflow else "No")