import sys

def main():
    if len(sys.argv) != 3:
        print("Error: Please provide exactly two numbers as command-line arguments.")
        print("Usage: python week5_task3.py 12 34")
        sys.exit(1)

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
    except ValueError:
        print("Error: Both arguments must be numbers.")
        sys.exit(1)

    result = a + b
    if a.is_integer() and b.is_integer():
        print(int(result))
    else:
        print(result)

if __name__ == "_main_":
    main()