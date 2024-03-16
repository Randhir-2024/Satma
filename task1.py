def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width

def main():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    
    result = calculate_area(length, width)
    print("Area:", result)
    
if __name__ == "__main__":
    main()
    
