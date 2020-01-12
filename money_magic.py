"""
This application calculates the amount of money you can make in N year
"""
from colorama import Fore, init
from os import system


def main():
    """

    :return:
    """
    age = int(input('Enter Your Age: '))
    amt = int(input("Enter Amount: $"))
    rate = float(input("Enter Annual Rate of Return :"))
    n = int(input("Enter Number of Years: "))


    system("cls")
    print(Fore.LIGHTBLUE_EX + f"Initial Investment = ${amt}\nAnnual Rate Of Return = {rate}\nNumber of years = {n}")
    counter = 0
    print(Fore.LIGHTBLUE_EX + "Age # ", end="")
    print(Fore.LIGHTMAGENTA_EX + '{:>25s}'.format("Amount in $"))
    for i in range(n+1):

        if i == 0:
            print(Fore.RED + f"Age {age} ", end="")
            print(Fore.LIGHTGREEN_EX + '{:>25,.2f}'.format(amt))
            continue
        amt += amt * rate
        print(Fore.WHITE + f"Age {i+age} ", end="")
        print(Fore.LIGHTGREEN_EX + '{:>25,.2f}'.format(amt))
        counter += 1
        if counter % 10 == 9:
            print()
    a=input("Press enter to exit")


if __name__ == "__main__":
    system("color 0b")
    init()
    init(convert=True)
    main()

