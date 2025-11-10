def main():
    students = {
        "Alice": 85,
        "Bob": 90,
        "Charlie": 78,
        "David": 92
    }

    for name, mark in students.items():
        print(f"{name}: {mark}")

    total = sum(students.values())
    count = len(students)
    average = total / count if count > 0 else 0
    print(f"Average mark: {average:.2f}")

if __name__ == "_main_":
    main()
