"""
M
"""

# @@ Program should be able to catch errors in opening csv file, delete the file and tell the user to update data to
# continue
from time import sleep
from datetime import datetime as dt
import itertools as it
import os
import csv
from textwrap import indent
from colorama import init, Fore, Style

"""
addresses = {
             0: main(),
             1:convert(),
             1.1:direct_conversion(), #there is no reason anyone'd ever want to go back to that
             1.2:chain_conversion(),
             1.3:reverse_conversion(), #there is no reason anyone'd ever want to go back to that
             2:foreign(),
             3:arbitrage(),
             4:data_handle(),
             4.1:view_data(), #there is no reason anyone'd ever want to go back to that
             4.2:update_data(),
             4.3:create_new_data
             5:learn(),
             6:help_direct(),
             }
             
functions that call other functions = {
             main(), #trivial case
             convert()>>chain_conversion(), calls 4.2, 4.3, 6, 3
             foreign(), calls 4.2 if get_data() is not None | else calls 4.3
             arbitrage(), calls 4.2 if get_data() is not None | else calls 4.3
             data_handle(), calls get_help()
             }
             
functions that get the param where_from
             {           
             get_help()
             data_handle()
             arbitrage()
             create()
             edit()
             }
             
"""


def indented_print(text=""):
    """
    prints indented text on terminal
    :param text:

    :return:
    """

    print(Fore.RESET + indent(text, prefix="    "))


def i_print_b(text=""):
    """
    prints indented green text on terminal
    :param text:
    :return:
    """
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + indent(text, prefix="    "))


def i_print_g(text=""):
    """
    prints indented green text on terminal
    :param text:
    :return:
    """
    print(Fore.GREEN + Style.BRIGHT + indent(text, prefix="    "))


def i_print_y(text=""):
    """
    prints indented green text on terminal
    :param text:
    :return:
    """
    print(Fore.LIGHTYELLOW_EX + indent(text, prefix="    "))


def i_print_r(text=""):
    """
    prints indented red text on terminal
    :param text:
    :return:
    """
    print(Fore.RED + Style.BRIGHT + indent(text, prefix="    "))


def i_print_m(text=""):
    """
    prints indented red text on terminal
    :param text:
    :return:
    """
    print(Fore.MAGENTA + indent(text, prefix="    "))


def beautiful_line():
    """
    Prints beautiful line on screen

    :return:
    """

    print(Fore.RED + indent("." * 4, prefix="    "), end="")
    print(Fore.LIGHTRED_EX + "." * 6, end="")
    print(Fore.YELLOW + "." * 5, end="")
    print(Fore.LIGHTYELLOW_EX + "." * 4, end="")
    print(Fore.LIGHTGREEN_EX + "." * 7, end="")
    print(Fore.GREEN + "." * 6, end="")
    print(Fore.LIGHTCYAN_EX + "." * 8, end="")
    print(Fore.BLUE + "." * 7, end="")
    print(Fore.MAGENTA + "." * 6, end="")
    print(Fore.LIGHTMAGENTA_EX + "." * 8)


def clear():
    """
    Clears the screen or terminal
    """

    os.system('cls')


def done():
    """Clears the screen and displays closing message before closing the program"""
    os.system("color 0b")
    clear()
    print("\n" * 6 + "=" * 76 + "\n\n" + " " * 30 + "Enjoy your day!\n\n" + "=" * 76 + "\n" * 7)
    sleep(2)
    clear()
    exit()
    return 0


def get_data():
    """
    Reads currency data from the csv file
    :rtype: None or list
    :return:  list containing previous data
    """

    try:
        with open("my_currencies.csv") as mc:
            lead = csv.reader(mc, delimiter=',')
            data = [line for line in lead if len(line) != 0]
            if len(data) == 0:
                return None
            else:
                previous_data = data[-1]
                return previous_data
    except IOError:
        return None


beginner = False
if get_data() is None:
    beginner = True


def continue_process(n):
    """

    :param n:
    :return:
    """
    indented_print("\n1. Continue Data Edit\n2. Help")
    selection = int_inputs(n)
    if selection == 1:
        return 0
    else:
        get_help()


def check_data(n):
    """
    Checks if data exits in the csv file should the user attempt to use it. if none is available
    it automatically refers them to the data update by function call
    :return: void
    """

    if get_data() is None:
        clear()
        i_print_r("\nInsufficient Data. Please Update Your Data To Proceed\n")
        sleep(1.5)
        i_print_y("\n ...Referring To Data Centre\n\n ...Please Wait...")
        indented_print("\n\n\n\n")
        sleep(3)
        create(n)
        return 0


def welcome():
    """Displays the formatted start-up messages on the screen"""

    clear()
    os.system('color 0b')
    print("\n" * 6 + "=" * 76 + "\n\n" + " " * 21 + "FOURSCORE FINANCIAL TECHNOLOGIES\n\n" + "=" * 76 + "\n" * 7)

    sleep(3)
    clear()
    print("\n" * 6 + "=" * 76 + "\n\n" + " " * 30 + "FOREX ARBITRAGE\n\n" + "=" * 76 + "\n" * 7)
    sleep(1.5)
    clear()
    print("\n" * 6 + "=" * 76 + "\n\n" + " " * 30 + "At Your Service :)\n\n" + "=" * 76 + "\n" * 3)
    if beginner:
        i_print_m(" " * 16 + "Tip! Forex Arbitrage Works Best With More Data\n")
        sleep(1)
    else:
        print("\n" * 3)
    sleep(2)
    os.system("color 0f")
    clear()


def int_inputs(n):
    """An error handling function to get integer inputs from the user"""

    while True:
        try:
            option = int(input(Fore.LIGHTCYAN_EX + "\n    >>> "))
            if option not in range(1, n + 1):
                i_print_r("Invalid Entry :( Please Try Again.")
                continue
            else:
                return option
        except ValueError:
            i_print_r("Invalid Entry :( Please Try again")
            continue


def back(n):
    """This function displays the options the user has after they are done running None type returning funtions.
    It takes their location as an integer which represents their current function call. Depending on their choice
    they can be taken to their previous menu or they can exit the application"""

    i_print_y("\n||Where To Next?\n")
    indented_print("1. Back")
    indented_print("2. Exit")
    option = int_inputs(2)
    if option == 1:
        if n == 0:
            main()
        elif n == 1:
            convert()
        elif n == 2:
            foreign()
        elif n == 3:
            arbitrage(n
                      )
        elif n == 4:
            data_handle()
    else:
        done()


def help_direct():
    """Sends a user to the help menu after a number of invalid inputs"""

    clear()
    i_print_m("Please refer to Help")
    i_print_g("1. Help")
    i_print_r("2. Continue")
    option = int_inputs(2)
    if option == 1:
        get_help()
    elif option == 2:
        pass
    return


def compare_time():
    """This function is a poorly designed attempt at calculating the time that has passed since the last data
    entry. A better way to do it would have been to use the epoch time instead or maybe master the time module
    better, but it was not until the middle of it's design that i realised i could have done it better. The sheer
    number of variables used is mind boggling, even to me. But I am not ready to tear down the code. The next
    version will, however, be better!"""

    if get_data() is None:
        i_print_r("No Data Found\n")
        return 0
    previous = get_data()[0].split(" ")
    now = str(dt.now())
    now = now.split(' ')
    n_time = now[1].split(":")
    p_time = previous[1].split(":")
    now_date = now[0].split("-")

    p_date = previous[0].split("-")

    ydiff = eval(now_date[0]) - eval(p_date[0])

    # eval() wont take it as int if it has a 0 at start
    if now_date[1][0] == "0":
        now_date[1] = now_date[1].replace("0", '')

    if p_date[1][0] == "0":
        p_date[1] = p_date[1].replace("0", '')

    mdiff = eval(now_date[1]) - eval(p_date[1])

    if now_date[2][0] == "0":
        now_date[2] = now_date[2].replace("0", '')
    # eval() wont take it as int if it has a 0 at start
    if p_date[2][0] == "0":
        p_date[2] = p_date[2].replace("0", '')

    ddiff = eval(now_date[2]) - eval(p_date[2])

    if n_time[0][0] == "0" and n_time[0][1] != "0":
        n_time[0] = n_time[0].replace("0", '')

    if n_time[1][0] == "0" and n_time[1][1] != "0":
        n_time[1] = n_time[1].replace("0", '')

    if p_time[0][0] == "0" and p_time[0][1] != "0":
        p_time[0] = p_time[0].replace("0", '')

    if p_time[1][0] == "0" and p_time[1][1] != "0":
        p_time[1] = p_time[1].replace("0", '')

    n_h_diff = eval(n_time[0]) - eval(p_time[0])
    p_h_diff = eval(n_time[1]) - eval(p_time[1])

    # Checking for negatives
    if p_h_diff < 0:
        p_h_diff += 60
        n_h_diff -= 1

    if ydiff != 0:
        i_print_r(text="Last Data Update Over A Year Ago!\n")
        return 0
    if mdiff != 0:
        i_print_r(text="Last Data Update Over A Month Ago!\n")
        return 0

    if ddiff > 0:
        days = eval(now_date[2]) - eval(p_date[2])
        if days >= 7:
            if days // 7 == 1 and days % 7 <= 2:
                i_print_r(text=f"Last Data Update: About A Week Ago!\n")

            elif days // 7 == 1 and days >= 3:
                i_print_r(f"Last Data Update: About {days // 7} week {days % 7} days ago!\n")

            else:
                i_print_r(f"Last Data update: About {days // 7} weeks ago\n")
            return 0
        elif days == 1:
            hours = 24 - eval(p_time[0]) + eval(n_time[0])
            minutes = eval(n_time[1]) - eval(p_time[1])
            if minutes >= 60:
                hours += 1
                minutes -= 1
            elif minutes < 0:
                hours -= 1
                minutes += 60
            if hours > 24:
                i_print_r(f"Last Data Update: A day and {hours % 24} hours ago!\n")

            else:
                if hours < 12:
                    i_print_g(f"Last Data Update: {hours} hours, {minutes} minutes ago!\n")
                else:
                    i_print_r(f"Last Data Update: {hours} hours, {minutes} minutes ago!\n")
            return 0

        else:
            i_print_r(text=f"last Data Update: About {days} days ago!\n")
            return 0
    else:
        if n_h_diff != 0:
            if n_h_diff < 6:
                i_print_g(text=f"last Data Update: {n_h_diff} hours, {p_h_diff} minutes ago!\n")
            else:
                i_print_r(text=f"last Data Update: {n_h_diff} hours, {p_h_diff} minutes ago!\n")

        else:
            i_print_g(text=f"last Data Update: {p_h_diff} minutes ago!\n")
        return 0


def get_two_currencies():
    """
    gets the user to select two currencies
    :return: tuple of two currencies (start, end)
    """

    check_data(1)
    currencies = eval(get_data()[1])
    while True:
        print(Fore.RESET + indent("\nSelect Starter Currency ", prefix="    "), end="")

        starter = input(Fore.LIGHTCYAN_EX + ">>> ")

        try:
            starter = int(starter)
            starter = currencies[starter - 1]

            break
        except ValueError:
            if starter in currencies:
                break
            else:
                i_print_r('Currency Not Found. Please try again!')
        except IndexError:
            i_print_r("Invalid Selection. Please Try again")
    while True:
        print(Fore.RESET + indent("\nSelect Ending Currency  ", prefix="    "), end="")
        end = input(Fore.LIGHTCYAN_EX + ">>> ")
        try:
            end = int(end)
            end = currencies[end - 1]
            if starter == end:
                i_print_r("Starter Currency cannot be equal to Final Currency.")
                i_print_m("For that kind of trading, select 'Find An Opportunity' from Main Menu.")
                continue
            break
        except ValueError:
            if end in currencies:
                if starter == end:
                    i_print_r("Starter Currency cannot be equal to Final Currency.")
                    i_print_m("that kind of trading, select 'Find An Opportunity' from the Main Menu.")
                    continue
                break
            else:
                i_print_r('Currency Not Found. Please try again!')
        except IndexError:
            i_print_r("Invalid Selection. Please Try again")

    return starter, end


def convert():
    """
    Convert Menu. Allows user to do a direct conversion locally or calls arbitrage() to perform chain conversion
    Does a direct conversion of two currencies
    :return: void
    """

    clear()
    i_print_y("\n\n||Currency conversions\n")
    indented_print("1. Direct Conversion")
    indented_print("2. Try Chain Conversion")
    indented_print("3. Reverse Conversion")
    indented_print("4. Back To Main Menu")
    option = int_inputs(4)
    if option == 1 or option == 3:
        clear()
        if option == 1:
            i_print_y("\n\n||Simple Conversion\n")
        else:
            i_print_y("\n\n||Reverse Conversion\n")
        check_data(1)
        quotes = eval(get_data()[2])

        currencies = eval(get_data()[1])
        n = len(currencies)
        i_print_m("Available Currencies\n")

        for i in range(n):
            i_print_g(f"{i + 1}. {currencies[i]}")
        indented_print()
        starter, end = get_two_currencies()
        rate = quotes[(starter, end)][0]
        if rate is None:
            i_print_r(":( Rate is Unavailable.")
            i_print_m("Please Update Your Data")
        else:
            while True:
                try:
                    if option == 1:
                        print(Fore.RESET + indent("\nEnter Starting Value    ", prefix="    "), end="")
                        num = float(
                            input(Fore.LIGHTCYAN_EX + f">>> {starter} "))
                        clear()
                        indented_print("\n\n")
                        indented_print(f"\n{starter} {round(num, 2)} >> {end} {round(num * rate, 2)}")
                        print(Fore.RESET + indent("\nChanging ", prefix="    "), end="")
                        print(Fore.LIGHTCYAN_EX + f"{starter} {num}", end="")
                        print(Fore.RESET + " at ", end="")
                        print(Fore.LIGHTCYAN_EX + f"{rate}", end="")
                        print(Fore.RESET + " yields ", end="")
                        print(Fore.LIGHTGREEN_EX + f"{end} {round(num * rate, 2)}")
                        break

                    else:
                        print(Fore.RESET + indent("\nEnter Ending Value    ", prefix="    "), end="")
                        num = float(input(Fore.LIGHTCYAN_EX + f">>> {end} "))
                        indented_print("\n\n")
                        indented_print(f"\n{starter} {round(num / rate, 3)} >> {end} {num}")
                        print(Fore.RESET + indent("\nYou need ", prefix="    "), end="")
                        print(Fore.LIGHTGREEN_EX + f"{starter} {round(num / rate, 3)}", end="")
                        print(Fore.RESET + "to get", end="")
                        print(Fore.LIGHTCYAN_EX + f"{end} {num}", end="")
                        print(Fore.RESET + " at ", end="")
                        print(Fore.LIGHTCYAN_EX + f"{rate}")
                        break
                except ValueError:
                    i_print_r(":( Please Try Again")

        back(1)

    elif option == 2:
        arbitrage(1)

    else:
        main()


def foreign():
    # @@ help referrals in this function get the input 2

    """
    Calculates the value of a currency in all the forign currencies for which data permits
    :return: void
    """
    clear()
    i_print_y("\n\n||Foreign Worth\n")
    indented_print("1. Use currently available data")
    indented_print("2. Update and use data")
    indented_print("3. Main Menu")
    option = int_inputs(3)
    if option == 1:
        clear()
        check_data(2)
        master_data = get_data()
        master_quotes = eval(master_data[2])

        currencies = eval(master_data[1])
        i_print_y("\n\n||Initialisation\n")
        i_print_m('Available Currencies\n')
        for i in range(len(currencies)):
            i_print_g(f"{i + 1}. {currencies[i]}")
        while True:
            print(Fore.RESET + indent("\nSelect Base Currency ", prefix="    "), end="")
            base = input(Fore.LIGHTCYAN_EX + " >>> ")
            try:
                base = int(base)
                base = currencies[base - 1]
                break
            except ValueError:
                if base in currencies:
                    break
                else:
                    print(Fore.LIGHTRED_EX + indent('Currency Not Found.'.upper(), prefix="    "), end="")
                    print(Fore.LIGHTMAGENTA_EX + ' Please try again!')
            except IndexError:
                print(Fore.LIGHTRED_EX + indent('invalid entry.'.upper(), prefix="    "), end="")
                print(Fore.LIGHTMAGENTA_EX + ' Please try again!')

        quotes = [key for key in master_quotes.keys() if key[0] == base and master_quotes[key][0] is not None]

        if len(quotes) == 0:
            print(Fore.LIGHTRED_EX + indent('fatal! insufficient data.'.upper(), prefix="    "), end="")
            print(Fore.YELLOW + ' Please Update Data To Continue\n\n')
            beautiful_line()
            i_print_y("\n\nReferring To Data Centre")
            i_print_m("Please Wait...")
            sleep(7)
            edit()

        while True:
            try:
                print(Fore.RESET + "\n    Starting Amount", end="")
                num = float(input(Fore.LIGHTCYAN_EX + f" >>> {base} "))
                break
            except ValueError:
                i_print_r(":( Please Try Again")

        clear()
        print(Fore.YELLOW + indent("\n||Showing Value of", prefix="    "), end="")
        print(Fore.LIGHTCYAN_EX + f" {base} {num} ", end="")
        print(Fore.YELLOW + "In Other Currencies.\n")
        indented_print('{:<15s}'.format("Currency") + '{:>20}'.format("Value"))
        indented_print()
        for key in quotes:
            print(Fore.LIGHTCYAN_EX + indent("{:<15s}".format(key[1]) + "{:s}".format('|'), prefix="    "), end="")
            print(Fore.LIGHTCYAN_EX + '{:>19,.2f}'.format(num * master_quotes[key][0]))
        indented_print("\nPLEASE NOTE")
        i_print_m(
            "This section only shows the foreign value when calculated \nusing direct rates, your money might "
            "actually be worth more\nin some of "
            " the currencies! "
            "To see how much more it might\nbe worth, visit 'Convert A Currency' from the Main Menu and\nselect 'Try "
            "Chain Conversion'")
        back(2)
    elif option == 2:
        edit()
    else:
        main()
    # @@ print the list of currencies in data base
    # @@ if none available prompt them to update data


def write_data(rates, currencies, new):
    """
    Writes data into csv file
    :param rates:
    :param currencies:
    :param new
    :return: void
    """

    with open("my_currencies.csv", mode='a') as my_cs:
        writer = csv.writer(my_cs, delimiter=',', lineterminator='\n')
        writer.writerow([dt.now(), currencies, rates, new])


def easy_rate(rate):
    """

    :param rate:
    :return:
    """
    # @@Add nil function
    if rate == 'nil' or rate == 'Nil' or rate == 'None' or rate == 'none' or rate == 'n' or rate == 'N':
        return None, (None, None)
    elif '/' in rate or ',' in rate:
        # place , where we have the x and then delete the /
        if '/' in rate:
            n = rate.split('/')
        else:
            n = rate.split(',')
        try:
            n[0] = float(n[0])
            n[1] = float(n[1])
            n = tuple(n)
            num_rate = float(n[1]) / float(n[0])
            return num_rate, n
        except ValueError:
            continue_process(3)
            return None
            # if None returned put into loop
    else:
        try:
            rate = float(eval(rate))
            if rate > 0:
                return rate, (None, None)
            else:
                i_print_r(":( Rate cannot be negative")
                return None
        except SyntaxError:
            i_print_r(":( Invalid Format. ")
            return None
        except ValueError:
            i_print_r(":( Invalid Format. ")
            return None
        except NameError:
            i_print_r(":( Invalid Format. ")
            return None


def create(k):
    """

    Handles the process of inputting currency data data from the user
    :param k: The function address whence the user came
    :return: void

    """
    # k is the address where user came from
    # @@ help referrals in this function get the input 4

    clear()
    i_print_y("\n\n||Create New Data\n")
    indented_print("Enter Number of Currencies ")
    while True:
        n = int_inputs(25)
        if n >= 2:
            break
        else:
            i_print_r("At Least Two Currencies Required\nEnter Number of Currencies\n")

    currencies = []
    rates = {}
    clear()
    i_print_y("\n\n||Currency Tickers\n")
    for g in range(n):
        while True:
            print(Fore.MAGENTA + indent(f'Currency {g + 1}: ', prefix="    "), end="")
            cur = input(Fore.LIGHTCYAN_EX)
            print()
            if cur not in currencies:
                currencies.append(cur)
                break
            else:
                i_print_r("Error! That currency has already been registered.")
                i_print_m("Please Try again")
    pairs = list(it.permutations(currencies, 2))

    clear()
    i_print_y("\n\n||Enter The Rates Below\n")

    for pair in pairs:
        # Allow entry of rate as a pair of values. The tuple will be stored in the dict as a second value to the pair
        # key
        while True:
            print(Fore.RESET + indent(f"{pairs.index(pair) + 1}. {pair[0]} / {pair[1]} = ", prefix="    "), end="")
            rate = input(Fore.LIGHTCYAN_EX)
            rate = easy_rate(rate)
            if rate is None:
                continue
            else:
                rates[pair] = rate
                print()
                break
    write_data(rates, currencies, new=False)
    back(k)


def print_rates(rates):
    """

    :param rates:
    """
    i_print_y("\n\n||Rates\n")

    indented_print("{:<14s}".format('Pair') + "{0:>19s}".format('Rate') + "{:>30s}".format('Pair Exchange'))
    print()
    for k in rates:
        v = rates[k]
        try:
            i_print_b(
                "{:<14s}".format(str(k[0]) + "/" + str(k[1])) + "{0:>19,.3f}".format(v[0]) + "{:>30s}".format(
                    str(v[1])))
        except TypeError:
            i_print_r(
                "{:<14s}".format(str(k[0]) + "/" + str(k[1])) + "{0:>19s}".format('-----') + "{:>30s}".format(
                    str(v[1])))


def edit():
    """

    :return:
    """
    clear()
    check_data(4)
    previous_data = get_data()
    currencies, rates = eval(previous_data[1]), eval(previous_data[2])
    i_print_y("\n\n||Data Update\n")
    check_data(0)
    # indented_print currencies here under my currencies
    i_print_m("My Currencies\n")
    for cur in currencies:
        i_print_g(cur)
    indented_print("\n1. Add A Currency\n2. Update Rates\n3. Back")
    option = int_inputs(3)
    clear()

    if option == 1:
        # you have to update quotes to show the new currency
        while True:
            i_print_y("\n\n||New Currency\n")
            print(Fore.RESET + indent("Enter new currency ", prefix="    "), end="")
            new_currency = input(Fore.LIGHTCYAN_EX + " >>> ")
            error = False  # Variable will tell us whether we got out of the next loop due to an error or not
            if new_currency not in currencies:
                currencies.append(new_currency)
                clear()
                i_print_g("\nCurrency successfully added to My Currencies!\n")
                new_pairs = list(set([pair for pair in it.permutations(currencies, 2) if
                                      pair[0] == new_currency or pair[1] == new_currency]))
                i_print_m("The following new pairs have been created\n")
                for pair in new_pairs:
                    indented_print(str(new_pairs.index(pair) + 1) + '. ' + pair[0] + ' / ' + pair[1])
                sleep(7.5)
                clear()
                i_print_y("\n\n||New Quotes\n")
                i_print_m("Enter The Rates below\n")

                for pair in new_pairs:
                    while True:
                        print(Fore.RESET + indent(str(new_pairs.index(pair) + 1) + '. ' + pair[0] + ' / ' +
                                                  pair[1] + " = ", prefix="    "), end="")
                        rate = input(Fore.LIGHTCYAN_EX)
                        rate = easy_rate(rate)
                        if rate is None:
                            continue
                        else:
                            rates[pair] = rate
                            break

                write_data(rates, currencies, new=False)
                back(4)
                break

            else:
                error = True
                i_print_r("Oops :( This currency has already been registered")
                i_print_m("\n1. Try again\n2. Back")
                selection = int_inputs(2)
                if selection == 1:
                    clear()
                    continue
                else:
                    break

        if error:
            clear()
            edit()

    elif option == 2:
        first_time = True
        while True:
            if first_time:

                clear()
                i_print_m("A new quote for A/B can be given as A/B = rate or"
                          "A,B = rate. \nThe rate can be given as a number eg 11.00 "
                          "or as the sample\nof amounts you can exchange. Eg if 10 A "
                          "gives 110 B then \nrate can be given as 10,110. See help.")
            else:
                pass
            print_rates(rates)
            indented_print("\nEnter new quote")
            new_quote = input(Fore.LIGHTCYAN_EX + indent("\n>>> ", prefix="    "))
            try:
                new_quote = new_quote.split("=")
                pair, rate = new_quote[0], new_quote[1]
            except IndexError:
                i_print_r(":( Invalid input")
                continue_process(4)
                continue

            # Handling input types for pair to make it a tuple
            if "/" in pair:
                pair = tuple(pair.split("/"))

            elif "," in pair:
                pair = tuple(pair.split(","))

            else:
                i_print_r(":( Invalid input.")
                continue_process(4)
                continue
            pair = (pair[0].strip(" "), pair[1].strip(" "))
            if pair[0] not in currencies or pair[1] not in currencies:
                indented_print(f"pair = {pair}")
                i_print_r("One of the currencies was not found.")
                continue_process(4)
                continue
            if pair[0] == pair[1]:
                i_print_r("Cannot add quote of a single currency")
                continue_process(4)
                continue
            rate = easy_rate(rate)
            if rate is None:
                continue_process(4)
                continue
            try:
                rates[pair] = rate
                first_time = False
                indented_print("\n1. Continue Data Edit\n2: Done\n3. Exit")
                selection = int_inputs(3)
                if selection == 1:
                    clear()
                    continue
                elif selection == 2:
                    clear()
                    break
            except KeyError:
                i_print_r(":( Invalid pair entry.")
                continue_process(4)
                continue

        write_data(rates, currencies, new=True)
        clear()
        i_print_g("\nData successfully updated!")
        back(4)
        done()

    else:
        data_handle()


def print_returns(where_from_p, conversions, returns):
    """

    Manages the business of printing the results from arbitrage calculations aesthetically
    :param where_from_p: function address whence the user came
    :param conversions: type <list>: The permutations of the possible changing routes
    :param returns: type <list>: The gains corresponding to the permutations
    :return: void


    """

    clear()
    if where_from_p == 0 or where_from_p == 3:
        try:
            conversions[0][0]
        except IndexError:
            i_print_r("\nOOps! :( \nNo Such Results Available")
            i_print_m("Try using a different base currency or adding more data")
            back(3)

    combs_to_print = [[] for o in range(len(conversions))]
    for combs in conversions:
        for per in combs:
            n = ''
            for i in range(len(per)):
                if i != len(per) - 1:
                    n += per[i] + ' >> '
                else:
                    n += per[i]
            combs_to_print[conversions.index(combs)].append(n)

    returns_to_print = [[] for o in range(len(conversions))]

    if where_from_p == 1:
        i_print_y("\n\nSelect an option")
        indented_print("\n1. Start With Amount To Convert\n2. Show Results In Terms Of Rates")
        option_p = int_inputs(2)
        if option_p == 1:
            while True:
                try:
                    print(Fore.RESET + indent("\nEnter Amount ", prefix="    "), end="")
                    amount = float(input(Fore.LIGHTMAGENTA_EX + f" >>> {conversions[0][0][0]} "))
                    break
                except ValueError:
                    i_print_r(":( Invalid Input")
                    i_print_m("Please Try Again")
        else:
            amount = 1

    else:
        amount = 100

    for return_list in returns:
        for n in return_list:
            if where_from_p != 1:
                n -= 1
            n *= amount
            returns_to_print[returns.index(return_list)].append(n)

    reference = 0
    if where_from_p == 1:
        try:
            reference_pair = conversions[0][0][0], conversions[0][0][-1]
            reference = returns_to_print[0][conversions[0].index(reference_pair)]
        except ValueError:
            reference = 0

    lengths = []
    for order in combs_to_print:
        for conversion in order:
            lengths.append(len(conversion))
    max_len = max(lengths)
    format_guy = "{:<" + str(max_len) + "}"
    clear()

    if where_from_p != 1:
        i_print_y("\n||Arbitrage Explorer\n")
        i_print_m(f"\nShowing how much can be made from a {conversions[0][0][0]} arbitrage execution\n\n")

        indented_print(format_guy.format("Conversion Chain") + "{:>16s}".format("Return (%)"))
    else:
        i_print_y("\n||Conversion Chains\n")
        i_print_m(
            f"\nShowing how much {conversions[0][0][-1]} can be made from {conversions[0][0][0]} {round(amount, 2)}\n\n")
        if amount == 1:
            indented_print(format_guy.format("Conversion Chain") + "{:>16s}".format(" Effective Rate"))
        else:
            indented_print(format_guy.format("Conversion Chain") + "{:>16s}".format("Value"))

    indented_print()

    for i in range(len(combs_to_print)):
        for j in range(len(combs_to_print[i])):
            if where_from_p != 1 or (where_from_p == 1 and amount != 1):
                if (where_from_p != 1 and returns_to_print[i][j] > 0) or \
                        (where_from_p == 1 and returns_to_print[i][j] > reference):
                    i_print_g(
                        format_guy.format(combs_to_print[i][j]) + str("{:>16,.2f}".format(returns_to_print[i][j])))
                elif reference == 0 or (where_from_p == 1 and returns_to_print[i][j] < reference):
                    i_print_r(
                        format_guy.format(combs_to_print[i][j]) + str("{:>16,.2f}".format(returns_to_print[i][j])))
                else:
                    i_print_b(
                        format_guy.format(combs_to_print[i][j]) + str("{:>16,.2f}".format(returns_to_print[i][j])))
            else:
                if returns_to_print[i][j] > reference:
                    i_print_g(
                        format_guy.format(combs_to_print[i][j]) + str("{:>16,.4f}".format(returns_to_print[i][j])))
                elif returns_to_print[i][j] < reference:
                    i_print_r(format_guy.format(combs_to_print[i][j]) + str(
                        "{:>16,.4f}".format(returns_to_print[i][j])))
                else:
                    i_print_b(format_guy.format(combs_to_print[i][j]) + str(
                        "{:>16,.4f}".format(returns_to_print[i][j])))

    if where_from_p == 0 or where_from_p == 3:
        back(3)
    else:
        back(1)


def arbitrage(where_from):
    """
    :type where_from: int

    """

    # @@ help referrals in this function get the input 3

    clear()
    if where_from == 0 or where_from == 3:
        i_print_y("\n\n||Arbitrage Explorer\n")
    else:
        i_print_y("\n\n||Chain Conversions\n")
    indented_print("1. Use currently available data")
    indented_print("2. Update and use data")
    indented_print("3. Main Menu")
    option = int_inputs(3)

    if option == 1:

        check_data(where_from)

        past_data = get_data()

        currencies = eval(past_data[1])
        quotes = eval(past_data[2])

        num_of_currencies = len(currencies)
        n = num_of_currencies
        clear()
        i_print_y("\n\n||Initialisation\n")
        i_print_m("Available Currencies\n")
        for i in range(len(currencies)):
            i_print_g(f"{i + 1}. {currencies[i]}")

        if n <= 2:
            i_print_r(
                "Insufficient data for Arbitrage conversions to work")
            i_print_m("Please update your data and try again!")
            return 0

        if where_from == 0 or where_from == 3:
            while True:
                print(Fore.RESET + indent("\nSelect Base Currency", prefix="    "), end="")
                base = input(Fore.LIGHTCYAN_EX + " >>> ")
                try:
                    base = int(base)
                    base = currencies[base - 1]
                    break
                except ValueError:
                    if base in currencies:
                        break
                    else:
                        i_print_r("Currency Not Found.")
                        i_print_m(" Please try again!")
                except IndexError:
                    i_print_r("Invalid Selection. ")
                    i_print_m(" Please try again!")
            currencies.append(base)
            orders = [o for o in range(3, n + 1)]
            p_returns = [[] for o in orders]
            n_returns = [[] for o in orders]
            indeterminate_permutations = [[] for i in orders]
            positive_permutations = [[] for i in orders]
            negative_permutations = [[] for i in orders]
            returns = [[] for i in orders]
            mc = [list(set([k for k in it.permutations(currencies, order + 1) if k[0] == k[order]])) for order in
                  orders]

        else:

            starter, end = get_two_currencies()
            orders = [o for o in range(1, n)]
            indeterminate_permutations = [[] for i in orders]
            returns = [[] for o in orders]
            # orders corresponds to number of conversions
            mc = [list(set([k for k in it.permutations(currencies, order + 1) if k[0] == starter and k[order] == end]))
                  for order in
                  orders]
            if quotes[(starter, end)][0] is None:
                i_print_r("\nFATAL! REFERENCE QUOTE IS UNAVAILABLE")
                i_print_m(f"Update rate for {starter}/{end}\n")
                beautiful_line()
                back(1)
                return 0
        # the order corresponds to the number of currencies involved

        for combinations in mc:

            g = mc.index(combinations)
            k = 0
            for permutation in combinations:

                num = 1
                for i in range(len(permutation)):

                    if i + 1 != len(permutation):

                        pair = (permutation[i], permutation[i + 1])

                        try:
                            num *= quotes[pair][0]

                        except TypeError:

                            indeterminate_permutations[g].append(permutation)
                            # append permutation to it's correct position in indeterminate_permutations
                            # delete permutation from combinations later so as not to break the current looping process
                            break

                    else:
                        break

                if where_from == 0 or where_from == 3:
                    if num - 1 > 0:
                        p_returns[g].append(num)
                        positive_permutations[g].append(combinations[k])
                    else:
                        n_returns[g].append(num)
                        negative_permutations[g].append(combinations[k])

                returns[mc.index(combinations)].append(num)
                k += 1
        """
        A serious bug is here. occurs when the removing indeterminate permuattions removes a whole order or something. to 
        see what i mean add a fifth cuurency to four and try chain conevrions"""
        nmc = [list(set(mc[i]).difference(set(indeterminate_permutations[i]))) for i in range(len(orders))]
        p_unsorted = []
        p_unsorted_results = []
        if where_from == 0 or where_from == 3:
            for item in positive_permutations:
                p_unsorted += item
            for r in p_returns:
                p_unsorted_results += r
        else:
            for item in nmc:
                p_unsorted += item
            for r in returns:
                p_unsorted_results += r

        p_sorted = sorted(p_unsorted_results, reverse=True)

        all_sorted = [p_unsorted[p_unsorted_results.index(i)] for i in p_sorted]

        printable_conversions = []
        printable_conversions.append(all_sorted)
        printable_gains = []
        printable_gains.append(p_sorted)

        # check if returns align with their permutations after this process

        #  the printing business
        clear()
        if where_from == 0 or where_from == 3:
            i_print_g("\n1. Show Sorted Gains Only")
            i_print_r("2. Show Failed Arbitrages")
            i_print_b("3. Show All Results")
            f = int_inputs(3)
            if f == 1:
                print_returns(3, printable_conversions, printable_gains)
            elif f == 2:
                print_returns(3, negative_permutations, n_returns)
            else:
                print_returns(3, nmc, returns)
        else:
            print_returns(1, printable_conversions, printable_gains)

    elif option == 2:
        if beginner:
            create(where_from)
        elif not beginner:
            edit()

    elif option == 3:
        main()


def data_handle():
    """

    """
    # @@ help referrals in this function get the input 4

    clear()
    i_print_y("\n\n||Data Centre\n")
    compare_time()
    indented_print("1. View current data")
    indented_print("2. Update Data")
    indented_print("3. Create New Data")
    indented_print("4. Back To Main Menu")

    option = int_inputs(4)

    if option == 1:

        check_data(4)

        past_data = get_data()
        currencies = eval(past_data[1])
        rates = eval(past_data[2])
        clear()

        i_print_y("\n||Currencies\n")

        num_of_currencies = len(currencies)
        for i in range(num_of_currencies):
            indented_print(f"{i + 1}. {currencies[i]}")
        i_print_m("\nPlease Wait...")
        sleep(5)  # Clear screen here
        clear()
        print_rates(rates)
        back(4)

    elif option == 2:
        edit()

    elif option == 3:
        create(4)

    elif option == 4:
        main()


def learn():
    """

    """
    clear()
    i_print_y("\n\n||Learn")
    indented_print("\nLearn About?\n\n1. How it works\n2. Tips on getting rates")
    select = int_inputs(2)
    if select == 1:
        clear()
        i_print_y("\n||How It Works")
        indented_print("\n Arbitrage occurs when identical products, commodities or anything\n"
                       "of value are sold at different prices in different places. Sometimes\n"
                       "it can even be happening in the same place. In this case our commodities\n"
                       "are forex which can be found at different effective rates across\n"
                       "different money changing institutions or people.\n"
                       "\n For example, Zimbabwe being an under-developed financial market,\n"
                       "offers opportunities to profit from disparities in information\n"
                       "which may lead to disparities in prices and rates. But these\n"
                       "opportunities are not always obvious. \n\n Our premise is this: with"
                       "the right tools, it should be possible\nto exploit these opportunities"
                       "without necessarily having to end\nup with an undesirable currency.\n"
                       "\n We have designed the arbitrage calculator to figure that out for\n"
                       "you, so you can focus on the more important business of managing\n"
                       "your your wealth.\n"
                       "\n This application allows you to gather rates from the forex \n"
                       "changing people, and does the calculations for you.")
    else:
        clear()
        i_print_y("\n||Getting Currencies")
        indented_print("\n As a rule, when finding these currency rates, you should always \n"
                       "take the ones that gives you more of the currency you're getting.\n"
                       "i.e whenever you get from currency A to currency B, take the rate\n"
                       "that gives you the largest value of B divided by A -- more B for \n"
                       "less A. All the other rates are not of any use to you.\n"
                       "\n For example,\n"
                       " If there are three rates for USD > ZWL : 10/100, 10/110, 10/120\n"
                       "take the last one -- ALWAYS, even if you don't want the end \n"
                       "currency, just feed the rate into the data.\n\n"
                       "You can also benefit from the more expensive rates as they are\n"
                       "most likely to have more lucrative B > A rates. E.g our changer\n"
                       "with the USD 10 to ZWL 100 most likely offers the best ZWL to USD\n"
                       "price. Remember that trick.\n"
                       "\n NB See the Help section to see how you can input your currency\n"
                       "data easily, without having to do the calculations to determine the\n"
                       "actual mathematical rate")
    i_print_m("\n1. Back to Learn")
    indented_print("2. Back to Main Menu")
    indented_print("3. Exit")
    option = int_inputs(3)
    if option == 1:
        learn()
    elif option == 2:
        main()
    else:
        done()


def get_help():
    """

    """
    clear()
    i_print_y("\n\n||Help")
    # Add Menu to allow user to navigate the help
    i_print_m("\nThis section is still under development")
    indented_print("1. Back")
    indented_print("2. Exit")
    option = int_inputs(2)
    if option == 1:
        main()
    elif option == 1:
        done()


def about():
    """

    """
    clear()
    i_print_r(
        "\nDeveloped by Fourscore Financial Technologies")
    i_print_g("GitHub @@Cliff688\nVersion 2019.1.10.2\nCopyright 2019\n")
    i_print_y("\n||Disclaimer\n")
    indented_print("The developer will not be held responsible for any loss \nof money incurred while "
                   "attempting "
                   "to profit using\nthe methods developed in this application. Nor will the \ndeveloper hold any responsibility"
                   "for any harm caused \nto the user's computer or any data loss thereof. By \nusing this application, you, "
                   "the user "
                   "Agree to these terms\nof use and do so with the acknowledgement that it is \nat your own risk.\n")
    i_print_y("||Where to next?")
    indented_print("1. Back to Main Menu")
    indented_print("2. Exit")
    option = int_inputs(2)
    if option == 1:
        main()
    elif option == 2:
        done()


def main():
    """

    :return:
    """
    clear()
    i_print_y("\n\n||Main Menu\n")
    compare_time()
    indented_print("1. Convert A Currency")
    indented_print("2. Foreign Value")
    indented_print("3. Find An Opportunity")
    indented_print("4. Data Centre")
    indented_print("5. Learn About Arbitrage")
    indented_print("6. Help")
    indented_print("7. About Us")
    indented_print("8. Exit")
    select = int_inputs(8)
    if select == 1:
        convert()
    elif select == 2:
        foreign()
    elif select == 3:
        arbitrage(0)
    elif select == 4:
        data_handle()
    elif select == 5:
        learn()
    elif select == 6:
        get_help()
    elif select == 7:
        about()
    else:
        done()
    return 0


if __name__ == "__main__":
    welcome()
    main()
