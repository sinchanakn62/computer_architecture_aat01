binary = input("Enter the binary number: ")

if not binary or any(bit not in "01" for bit in binary):
    print("Invalid binary number!")
    exit()

direction = input("Enter shift direction (L/R): ").upper()

if direction not in ("L", "R"):
    print("Invalid direction!")
    exit()

positions = int(input("Enter number of positions: "))

if positions < 0:
    print("Number of positions cannot be negative.")
    exit()

print("\nOriginal number:", binary)

for i in range(positions):
    if direction == "L":
        binary = binary[1:] + "0"
    else:
        binary = "0" + binary[:-1]

    print("After shift", i + 1, ":", binary)

print("Final result:", binary)
