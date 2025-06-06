def main():
    op=int(input("which operator do you want to check?\n1.Arithmetic operators\n2.Assignment operators\n3.Comparison operators\n4.Logical operators\n5.Bitwise operators\n6.Special operators\n\n Enter your choice: ")) 
    checker(op)

def checker(op):
    match op:
        case 1:
            Arithmetic()
        case 2:
            Assignment()
        case 3:
            Comparison()
        case 4:
            Logical()
        case 5:
            Bitwise()
        case 6:
            Special()
        case default :
            print("Please select a valid choice!")

def Arithmetic():
    print("\nArithmetic Operations:")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("1. Addition:", a + b)
    print("2. Subtraction:", a - b)
    print("3. Multiplication:", a * b)
    print("4. Division:", a / b if b != 0 else "Undefined (division by zero)")
    print("5. Modulus:", a % b)
    print("6. Exponentiation:", a ** b)
    print("7. Floor Division:", a // b if b != 0 else "Undefined")

def Assignment():
    print("\nAssignment Operations:")
    a = int(input("Enter a value for 'a': "))
    print("Initial a =", a)
    a += 5
    print("a += 5:", a)
    a -= 3
    print("a -= 3:", a)
    a *= 2
    print("a *= 2:", a)
    a /= 4
    print("a /= 4:", a)
    a %= 3
    print("a %= 3:", a)

def Comparison():
    print("\nComparison Operations:")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("a == b:", a == b)
    print("a != b:", a != b)
    print("a > b:", a > b)
    print("a < b:", a < b)
    print("a >= b:", a >= b)
    print("a <= b:", a <= b)

def Logical():
    print("\nLogical Operations:")
    a = bool(int(input("Enter 1 (True) or 0 (False) for A: ")))
    b = bool(int(input("Enter 1 (True) or 0 (False) for B: ")))
    print("A and B:", a and b)
    print("A or B:", a or b)
    print("not A:", not a)

def Bitwise():
    print("\nBitwise Operations:")
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))
    print("a & b:", a & b)
    print("a | b:", a | b)
    print("a ^ b:", a ^ b)
    print("~a:", ~a)
    print("a << 1:", a << 1)
    print("a >> 1:", a >> 1)

def Special():
    print("\nSpecial Operators:")
    a = [1, 2, 3]
    b = a
    c = a[:]
    print("a is b:", a is b)
    print("a is c:", a is c)
    print("a == c:", a == c)
    print("2 in a:", 2 in a)
    print("5 not in a:", 5 not in a)

if __name__ == "__main__":
    main()


