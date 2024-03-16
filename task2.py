def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

def main():
    n = int(input("Enter the number of terms for Fibonacci sequence: "))
    if n <= 0:
        print("Please enter a positive integer.")
        return
    fibonacci_sequence = generate_fibonacci(n)
    print("Fibonacci sequence up to", n, "terms:")
    print(fibonacci_sequence)

if __name__ == "__main__":
    main()