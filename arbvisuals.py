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

"""
License should be implemented so that I have a list of keys which when used will be deleted.
When a key is entered, it allows the key in the program to change to the serial number of the user's
machine. If key == serialNumber, the user will never see the prompt for the key. Fallacy: when they start 
to share, keys become reusable. Solve this be a sharable variable of True or False
"""


def check_license():
    """
    checks whether the computer has access to the application
    :return:
    """
    user = os.getlogin()
    clear()
    if user != "clifford":
        print(indent("\n" * 6 + "***ACCESS DENIED***", prefix="    " * 7))
        print("\n"+"    " * 6 + "***LICENSE KEY NOT FOUND***")
        print("\n" +"   " * 3 + "contact <cliffygamy@gmail.com> to request a license key" + "\n"*5)
        sleep(10)
        exit()
    else:
        return 0


def indented_print(text):
    """
    prints indented text on termianal
    :param text:
    :return:
    """
    print(indent(text, prefix="    "))


def clear():
    """
    Clears the screen or terminal
    """

    os.system('cls')


def done():
    """Clears the screen and displays closing message before closing the program"""

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
    indented_print("\n1. Continue Data Edit\n2. Exit")
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
        indented_print("\nInsufficient Data. Please Update Your Data To Proceed\n")
        sleep(1.5)
        indented_print("\n ...Referring To Data Centre\n\n ...Please Wait...")
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
        print(" " * 16 + "Tip! Forex Arbitrage Works Best With More Data\n")
        sleep(1)
    else:
        print("\n" * 3)
    sleep(2)
    clear()


def int_inputs(n):
    """An error handling function to get integer inputs from the user"""

    while True:
        try:
            option = int(input("\n    >>> "))
            if option not in range(1, n + 1):
                indented_print("Invalid Entry :( Please Try Again.")
                continue
            else:
                return option
        except ValueError:
            indented_print("Invalid Entry :( Please Try again")
            continue


def back(n):
    """This function displays the options the user has after they are done running None type returning funtions.
    It takes their location as an integer which represents their current function call. Depending on their choice
    they can be taken to their previous menu or they can exit the application"""

    indented_print("\n||Where To Next?\n")
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
    indented_print("Please refer to Help")
    indented_print("1. Help")
    indented_print("2. Continue")
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
        indented_print("No Data Found\n")
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
        indented_print("Last Data Update Over A Year Ago!\n")
        return 0
    if mdiff != 0:
        indented_print("Last Data Update Over A Month Ago!\n")
        return 0

    if ddiff > 0:
        days = eval(now_date[2]) - eval(p_date[2])
        if days >= 7:
            if days // 7 == 1 and days % 7 <= 2:
                indented_print(f"Last Data Update: About A Week Ago!\n")
                return 0
            elif days // 7 == 1 and days >= 3:
                indented_print(f"Last Data Update: About {days // 7} week {days % 7} days ago!\n")
                return 0
            else:
                indented_print(f"Last Data update: About {days // 7} weeks ago\n")
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
                indented_print(f"Last Data Update: 1 day, {hours % 24} hours and {minutes} minutes ago!\n")
            else:
                indented_print(f"Last Data Update: {hours} hours, {minutes} minutes ago!\n")
            indented_print()

        else:
            indented_print(f"last Data Update: About {days} days ago!\n")
    else:
        if n_h_diff != 0:
            indented_print(f"last Data Update: {n_h_diff} hours, {p_h_diff} minutes ago!\n")

        else:
            indented_print(f"last Data Update: {p_h_diff} minutes ago!\n")


def get_two_currencies():
    """
    gets the user to select two currencies
    :return: tuple of two currencies (start, end)
    """

    check_data(1)
    currencies = eval(get_data()[1])
    while True:

        starter = input(indent("\nSelect Starter Currency >>> ", "    "))

        try:
            starter = int(starter)
            starter = currencies[starter - 1]

            break
        except ValueError:
            if starter in currencies:
                break
            else:
                indented_print('Currency Not Found. Please try again!')
        except IndexError:
            indented_print("Invalid Selection. Please Try again")
    while True:
        end = input(indent("\nSelect Final Currency   >>> ", "    "))

        try:
            end = int(end)
            end = currencies[end - 1]
            if starter == end:
                indented_print(
                    "Starter Currency cannot be equal to Final Currency.\nFor that kind of trading, select 'Find An "
                    "Opportunity'\nfrom Main Menu.")
                continue
            break
        except ValueError:
            if end in currencies:
                if starter == end:
                    indented_print(
                        "Starter Currency cannot be equal to Final Currency.\nFor that kind of trading, select 'Find "
                        "An Opportunity'\nfrom the Main Menu.")
                    continue
                break
            else:
                indented_print('Currency Not Found. Please try again!')
        except IndexError:
            indented_print("Invalid Selection. Please Try again")

    return starter, end


def convert():
    """
    Convert Menu. Allows user to do a direct conversion locally or calls arbitrage() to perform chain conversion
    Does a direct conversion of two currencies
    :return: void
    """

    clear()
    indented_print("\n||Currency conversions\n")
    indented_print("1. Direct Conversion")
    indented_print("2. Try Chain Conversion")
    indented_print("3. Reverse Conversion")
    indented_print("4. Back To Main Menu")
    option = int_inputs(4)
    if option == 1 or option == 3:
        clear()
        if option == 1:
            indented_print("\n||Simple Conversion\n")
        else:
            indented_print("\n||Reverse Conversion\n")
        check_data(1)
        quotes = eval(get_data()[2])

        currencies = eval(get_data()[1])
        n = len(currencies)
        indented_print("Available Currencies\n")

        for i in range(n):
            indented_print(f"{i + 1}. {currencies[i]}")
        starter, end = get_two_currencies()
        rate = quotes[(starter, end)][0]
        if rate is None:
            indented_print(":( Rate is Unavailable. Please Update Your Data")
        else:
            while True:
                try:
                    if option == 1:
                        num = float(input(indent(f"\nEnter Starting Value    >>> {starter} ", prefix="    ")))
                        indented_print(f"\n{starter} {round(num, 2)} >> {end} {round(num * rate, 2)}")
                        break
                    else:
                        num = float(input(indent(f"\nEnter Ending Value    >>> {end} ", "    ")))
                        indented_print(f"\n{starter} {round(num / rate, 3)} >> {end} {num}")
                        indented_print(f"\nYou need {starter} {round(num / rate, 3)} to get {end} {num} at {rate}")
                        break
                except ValueError:
                    indented_print(":( Please Try Again")

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
    indented_print("\n||Foreign Worth\n")
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
        indented_print('\n||Available Currencies\n')
        for i in range(len(currencies)):
            indented_print(f"{i + 1}. {currencies[i]}")
        while True:
            base = input(indent("\n|Select Base Currency\n>>> ", prefix='    '))
            try:
                base = int(base)
                base = currencies[base - 1]
                break
            except ValueError:
                if base in currencies:
                    break
                else:
                    indented_print(':( Currency Not Found. Please try again!')
            except IndexError:
                indented_print(":( Invalid Selection. Please Try again!")

        quotes = [key for key in master_quotes.keys() if key[0] == base and master_quotes[key][0] is not None]

        if len(quotes) == 0:
            indented_print(":) Insufficient Data. Please Update Data To Continue.")
            sleep(1)
            indented_print("\nReferring To Data Centre\n\n Please Wait...")
            sleep(2)
            create(2)

        while True:
            try:
                num = float(input(indent(f"\nEnter Starting Amount \n>>> {base} ", "    ")))
                break
            except ValueError:
                indented_print(":( Please Try Again")

        clear()
        indented_print(f"\n||Value of {base} {num} In Forex\n")
        indented_print('{:<10s}'.format("Currency") + '{:>20}'.format("Value"))
        indented_print("")
        for key in quotes:
            indented_print(
                '{:<10s}'.format(key[1]) + '{:s}'.format('|') + '{:>19,.2f}'.format(num * master_quotes[key][0]))
        indented_print(
            "\nThis section only shows the foreign value when calculated \nusing direct rates, your money might "
            "actually be worth more\nin some of "
            " the currencies! "
            "To see how much more it might\nbe worth, visit 'Convert A Currency' from the Main Menu and\nselect 'Try "
            "Chain Conversion'")
        back(2)
    elif option == 2:
        create(2)
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
    if rate == 'nil' or rate == 'Nil' or rate == 'None' or rate == 'none':
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
                indented_print(":( Rate cannot be negative")
                return None
        except SyntaxError:
            indented_print(":( SInvalid Format. ")
            return None
        except ValueError:
            indented_print(":( Invalid Format. ")
            return None
        except NameError:
            indented_print(":( Invalid Format. ")
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
    indented_print("\n||Create New Data\n")
    indented_print("Enter Number of Currencies ")
    while True:
        n = int_inputs(25)
        if n >= 2:
            break
        else:
            indented_print("At Least Two Currencies Required\nEnter Number of Currencies\n")

    currencies = []
    rates = {}
    clear()
    indented_print("\n||Currency Tickers\n")
    for g in range(n):
        while True:
            cur = input(indent(f'Currency {g + 1}\n>>> ', "    "))
            if cur not in currencies:
                currencies.append(cur)
                break
            else:
                indented_print("Error! That currency has already been registered. Please try again!")
    pairs = it.permutations(currencies, 2)

    clear()
    indented_print("\n||Enter The Rates Below\n")

    cls_counter = 0
    for pair in pairs:
        # Allow entry of rate as a pair of values. The tuple will be stored in the dict as a second value to the pair
        # key
        cls_counter += 1
        counter = 0

        # the counter keeps track of the number of failed attempts and then suggests they go to help

        while True:
            rate = input(str(pair[0] + "/" + pair[1] + "... "))

            # Keep code on top
            # Use function easy rates
            # @@Add nil function
            if rate == 'nil' or rate == 'Nil' or rate == 'None' or rate == 'none':
                rates[pair] = (None, (None, None))
                break
            elif '/' in rate or ',' in rate:
                # place , where we have the x and then delete the /
                if '/' in rate:
                    n = rate.split('/')
                else:
                    n = rate.split(',')
                try:
                    n[0] = int(n[0])
                    n[1] = int(n[1])
                    n = tuple(n)
                    num_rate = float(n[1]) / float(n[0])
                    rates[pair] = tuple([num_rate, n])
                    if cls_counter % 3 == 0:
                        clear()
                        indented_print("\n||Enter Rates Below")
                    break
                except ValueError:
                    counter += 1
                    if counter > 3:
                        indented_print("Invalid Format! Please Refer to Help.")
                    else:
                        indented_print("Invalid Format. Please try again")
                    continue
            else:
                try:
                    rate = float(eval(rate))
                except SyntaxError:
                    counter += 1
                    if counter > 3:
                        indented_print("Please Refer to Help.")
                        help_direct()
                        continue
                    else:
                        indented_print("Invalid Format. Please try again")
                        continue

                if type(rate) == float:
                    if rate > 0:
                        rates[pair] = (rate, (None, None))
                        if cls_counter % 3 == 0:
                            clear()
                            indented_print("\n\n")
                        break
                    else:
                        counter += 1
                        if counter >= 3:
                            indented_print("Please Refer to Help.")
                            help_direct()
                            continue
                        else:
                            indented_print(":( Rate Cannot Be Negative. Please Try Again.")
                else:
                    counter += 1
                    if counter > 3:
                        indented_print(":( Please Refer To Help")
                        help_direct()
                        continue
                        # @@ Allow them to navigate to help from here
                    else:
                        indented_print(":( Invalid Entry. Please Try Again")
                        continue
    write_data(rates, currencies, new=True)
    back(k)


def print_rates(rates):
    """

    :param rates:
    """
    indented_print("\n||Rates\n")

    indented_print("{:<14s}".format('Pair') + "{0:>19s}".format('Rate') + "{:>30s}".format('Pair Exchange'))
    for k in rates:
        v = rates[k]
        try:
            indented_print(
                "{:<14s}".format(str(k[0]) + "/" + str(k[1])) + "{0:>19,.3f}".format(v[0]) + "{:>30s}".format(
                    str(v[1])))
        except TypeError:
            indented_print(
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
    indented_print("\n||Data Update\n")
    check_data(0)
    # indented_print currencies here under my currencies
    indented_print("||My Currencies")
    for cur in currencies:
        indented_print(cur)
    indented_print("\n1. Add A Currency\n2. Update Rates\n3. Back")
    option = int_inputs(3)
    clear()

    if option == 1:
        # you have to update quotes to show the new currency
        while True:
            new_currency = input(indent("\n||New Currency\nEnter new currency \n>>> ", prefix="    "))
            error = False  # Variable will tell us whether we got out of the next loop due to an error or not
            if new_currency not in currencies:
                currencies.append(new_currency)
                clear()
                indented_print("\nCurrency successfully added to my currencies!")
                new_pairs = list(set([pair for pair in it.permutations(currencies, 2) if
                                      pair[0] == new_currency or pair[1] == new_currency]))
                indented_print("The following new pairs have been created\n")
                for pair in new_pairs:
                    indented_print(str(new_pairs.index(pair) + 1) + '. ' + pair[0] + ' / ' + pair[1])
                sleep(7.5)
                clear()
                indented_print("\n||New Quotes\n\nEnter The Rates below\n")
                for pair in new_pairs:
                    while True:
                        rate = input(str(new_pairs.index(pair) + 1) + '. ' + pair[0] + ' / ' + pair[1] + "\n>>> ")
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
                indented_print("Oops :( This currency has already been registered")
                indented_print("\n1. Try again\n2. Back")
                selection = int_inputs(2)
                if selection == 1:
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
                indented_print("A new quote for A/B can be given as A/B = rate or"
                      "A,B = rate. \nThe rate can be given as a number eg 11.00 "
                      "or as the sample\nof amounts you can exchange. Eg if 10 A "
                      "gives 110 B then \nrate can be given as 10,110. See help.")
            else:
                pass
            print_rates(rates)
            new_quote = input("\nEnter new quote\n>>> ")
            try:
                new_quote = new_quote.split("=")
                pair, rate = new_quote[0], new_quote[1]
            except IndexError:
                indented_print(":( Invalid input")
                continue_process(4)
                continue

            # Handling input types for pair to make it a tuple
            if "/" in pair:
                pair = tuple(pair.split("/"))

            elif "," in pair:
                pair = tuple(pair.split(","))

            else:
                indented_print(":( Invalid input.")
                continue_process(4)
                continue
            pair = (pair[0].strip(" "), pair[1].strip(" "))
            if pair[0] not in currencies or pair[1] not in currencies:
                indented_print(f"pair = {pair}")
                indented_print("One of the currencies was not found.")
                continue_process(4)
                continue
            if pair[0] == pair[1]:
                indented_print("Cannot add quote of a single currency")
                continue_process(4)
                continue
            rate = easy_rate(rate)
            if rate is None:
                continue_process(4)
                continue
            try:
                rates[pair] = rate
                indented_print("\n1. Continue Data Edit\n2: Done\n3. Exit")
                selection = int_inputs(3)
                if selection == 1:
                    continue
                elif selection == 2:
                    break
            except KeyError:
                indented_print(":( Invalid pair entry.")
                continue_process(4)
                continue

        write_data(rates, currencies, new=True)
        clear()
        indented_print("\nData successfully updated!")
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
            indented_print(
                "\n\nOOps! :( \nNo Such Results Available\n\nTry using a different base currency or adding\nmore data")
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
        indented_print("\n|Select an option\n\n1. Start With Amount To Convert\n2. Show Results In Terms Of Rates")
        option_p = int_inputs(2)
        if option_p == 1:
            while True:
                try:
                    amount = float(input(indent(f"\nEnter Amount >>> {conversions[0][0][0]} ", prefix="    ")))
                    break
                except ValueError:
                    indented_print(":( Please Try Again")
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

    lengths = []
    for order in combs_to_print:
        for conversion in order:
            lengths.append(len(conversion))
    max_len = max(lengths)
    format_guy = "{:<" + str(max_len) + "}"
    clear()

    if where_from_p != 1:
        indented_print("\n||Arbitrage Explorer\n")
        indented_print(f"\nShowing how much can be made from a {conversions[0][0][0]} arbitrage execution\n\n")

        indented_print(format_guy.format("Conversion Chain") + "{:>16s}".format("Return (%)"))
    else:
        indented_print("\n||Conversion Chains\n")
        indented_print(
            f"\nShowing how much {conversions[0][0][-1]} can be made from {conversions[0][0][0]} {round(amount, 2)}\n\n")
        if amount == 1:
            indented_print(format_guy.format("Conversion Chain") + "{:>16s}".format(" Effective Rate"))
        else:
            indented_print(format_guy.format("Conversion Chain") + "{:>16s}".format("Value"))

    indented_print("")

    for i in range(len(combs_to_print)):
        for j in range(len(combs_to_print[i])):
            if where_from_p != 1:
                indented_print(format_guy.format(combs_to_print[i][j]) + str("{:>16,.2f}".format(returns_to_print[i][j])))
            else:
                if amount == 1:
                    indented_print(format_guy.format(combs_to_print[i][j]) + str("{:>16,.4f}".format(returns_to_print[i][j])))
                else:
                    indented_print(format_guy.format(combs_to_print[i][j]) + str("{:>16,.2f}".format(returns_to_print[i][j])))

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
        indented_print("\n||Arbitrage Explorer\n")
    else:
        indented_print("\n||Chain Conversions\n")
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
        indented_print("\n\n||Available Currencies\n")
        for i in range(len(currencies)):
            indented_print(f"{i + 1}. {currencies[i]}")

        if n <= 2:
            indented_print(
                "Insufficient data for Arbitrage conversions to work\n Please update your data and try again!")
            return 0

        if where_from == 0 or where_from == 3:
            while True:

                base = input(indent("\n|Select Base Currency\n>>> ", prefix="    "))
                try:
                    base = int(base)
                    base = currencies[base - 1]
                    break
                except ValueError:
                    if base in currencies:
                        break
                    else:
                        indented_print('Currency Not Found. Please try again!')
                except IndexError:
                    indented_print("Invalid Selection. Please Try again")
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
            indented_print("\n1. Show Sorted Gains Only\n2. Show Failed Arbitrages\n3. Show All Results")
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
    indented_print("\n||Data Centre\n")
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

        indented_print("\n||Currencies\n")

        num_of_currencies = len(currencies)
        for i in range(num_of_currencies):
            indented_print(f"{i + 1}. {currencies[i]}")
        indented_print("\nPlease Wait...")
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
    indented_print("\n||Learn")
    indented_print("\nLearn About?\n\n1. How it works\n2. Tips on getting rates")
    select = int_inputs(2)
    if select == 1:
        clear()
        indented_print("\n||How It Works")
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
        indented_print("\n||Getting Currencies")
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
    indented_print("\n1. Back to Learn")
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
    indented_print("||Help")
    # Add Menu to allow user to navigate the help
    indented_print("\nThis section is still under development")
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
    indented_print(
        "\nDeveloped by Fourscore Financial Technologies\nGitHub @@Cliff688\nVersion 2019.1.10.2\nCopyright 2019\n"
        "\n||Disclaimer\n\nThe developer will not be held responsible for any loss \nof money incurred while "
        "attempting "
        "to profit using\nthe methods developed in this application. Nor will the \ndeveloper hold any responsibility"
        "for any harm caused \nto the user's computer or any data loss thereof. By \nusing this application, you, "
        "the user "
        "Agree to these terms\nof use and do so with the acknowledgement that it is \nat your own risk.\n")
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
    indented_print("\n||Main Menu\n")
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
    check_license()
    welcome()
    main()
