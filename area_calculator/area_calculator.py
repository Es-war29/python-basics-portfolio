
print("==================")
print("Area Calculator 📐")
print("==================")

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")



def circle():
    radius = float(input("Enter the radius:"))
    area = 3.14 * pow(radius, 2)
    print(f"Area of circle with radius: {radius}, is {area:.2f}\n")


def triangle():
    height = float(input("Enter the height:"))
    base = float(input("Enter the base:"))
    area = (height * base) / 2
    print(f"Area of triangle with height: {height} and base: {base}, is {area:.2f}\n")


def square():
    side = float(input("Enter the side:"))
    area = pow(side, 2)
    print(f"Area of Square with side:{side}, is {area:.2f}\n")


def rectangle():
    length = float(input("Enter the length:"))
    width = float(input("Enter the width:"))
    area = length * width
    print(f"Area of rectangle with length : {length} and width : {width}, is {area:.2f}\n")


def main():
    while True:
        shape = input("Which shape (1.Triangle,2.Rectangle ,3.square,4.Circle ) or '5.quit' to exit: ").lower()

        if shape == '1':
            triangle()
        elif shape == '3':
            square()
        elif shape == '2':
            rectangle()
        elif shape == '4':
            circle()
        elif shape == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid shape. Please try again.\n")


if __name__ == '__main__':
    main()

