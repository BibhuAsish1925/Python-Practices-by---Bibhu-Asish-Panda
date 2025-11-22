def parse_number(s):
    s = s.strip()
    if s.lower() == 'q':
        return 'q'
    # Try int first
    try:
        i = int(s)
        return i
    except ValueError:
        pass
    # Try float
    try:
        f = float(s)
        return f
    except ValueError:
        return None

def get_operand(prompt):
    """Prompt user for an operand; allow quitting."""
    while True:
        raw = input(prompt).strip()
        if raw.lower() == 'q':
            return 'q'
        val = parse_number(raw)
        if val is None:
            print("  Invalid number. Try again or type 'q' to quit.")
            continue
        return val

def print_menu():
    print("\nChoose operation (type symbol) or 'q' to quit:")
    print("  +   Addition")
    print("  -   Subtraction")
    print("  *   Multiplication")
    print("  /   Division (float)")
    print("  //  Floor division (integer result)")
    print("  %   Modulus (remainder)")
    print("  **  Exponent (power)")
    print("  ^   Bitwise XOR (only meaningful for integers)")
    print("  &   Bitwise AND (ints)")
    print("  |   Bitwise OR  (ints)")
    print("  <<  Left shift (ints)")
    print("  >>  Right shift (ints)")
    print()

def ensure_int_operands(op, x, y):
    """For bitwise/shift ops ensure operands are integers."""
    bit_ops = {'^','&','|','<<','>>'}
    if op in bit_ops:
        if not (isinstance(x, int) and isinstance(y, int)):
            print("  Note: bitwise/shift operations require integer operands.")
            # try convert floats that are whole numbers to int
            if (isinstance(x, float) and x.is_integer()) and (isinstance(y, float) and y.is_integer()):
                return int(x), int(y)
            else:
                return None
    return x, y

def calculate(op, x, y):
    try:
        if op == '+':
            return x + y
        if op == '-':
            return x - y
        if op == '*':
            return x * y
        if op == '/':
            return x / y
        if op == '//':
            return x // y
        if op == '%':
            return x % y
        if op == '**':
            return x ** y
        if op == '^':
            return x ^ y
        if op == '&':
            return x & y
        if op == '|':
            return x | y
        if op == '<<':
            return x << y
        if op == '>>':
            return x >> y
    except ZeroDivisionError:
        return "Error: Division by zero."
    except Exception as e:
        return f"Error: {e}"
    return "Unknown operation."

def main():
    print("Simple Python Terminal Calculator")
    print("Type 'q' at any prompt to quit.")
    while True:
        print_menu()
        op = input("Operation: ").strip()
        if not op:
            print("  Please type an operation symbol (e.g. +, -, *, /).")
            continue
        if op.lower() == 'q':
            print("Goodbye")
            break

        # get operands
        x = get_operand("Enter first operand: ")
        if x == 'q':
            print("Goodbye")
            break
        y = get_operand("Enter second operand: ")
        if y == 'q':
            print("Goodbye")
            break

        # ensure integer operands for bitwise/shift ops
        ensured = ensure_int_operands(op, x, y)
        if ensured is None:
            print("  Cannot perform bitwise/shift with non-integer operands. Try again.")
            continue
        else:
            x, y = ensured

        result = calculate(op, x, y)
        print("\n------ RESULT ------")
        print(f"{x} {op} {y} = {result}")
        print("--------------------\n")

if __name__ == "__main__":
    main()
