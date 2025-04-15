#01 Adding Two numbers In python

def main():
    print("This Program Adds Two integer number")
    num1: str = input("Enter First Number: ")
    num1: int = int(num1)
    num2: str = input("Enter First Number: ")
    num2: int = int(num2)
    TOTAL: int = num1 + num2
    print(f"Sum of two numbers is ", TOTAL)

if __name__ == '__main__':
    main()
    