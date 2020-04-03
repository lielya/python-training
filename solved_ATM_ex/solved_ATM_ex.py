"""Simulating an ATM. """

import sys

ATM_FILE = 1  # The number 1 refers to the place of the file as a parameter


def check_the_balance(costumer_id, costumers_dictionary):
    """Check the state of costumer's money in the bank.

    Args:
    costumer_id (string): costumer id.
    costumers_dictionary (dictionary): dictionary of all costumers in
                                       the bank.
    """
    balance = int(costumers_dictionary[costumer_id][1])
    return balance


def cash_withdrawal(costumer_id, amount_to_withdrawal, costumers_dictionary):
    """Withdrawal from the ATM amount of money.

    Args:
    costumer_id (string): costumer id.
    amount_to_withdrawal (integer): amount the costumer wants to withdrawal.
    costumers_dictionary (dictionary): dictionary of all costumers in
                                       the bank.
    """
    balance_now = check_the_balance(costumer_id, costumers_dictionary)
    if amount_to_withdrawal > 0:
        if balance_now >= amount_to_withdrawal:
            new_balance = balance_now - amount_to_withdrawal
            costumers_dictionary[costumer_id][1] = str(new_balance)
            return True
    return False


def cash_deposit(costumer_id, amount_to_deposit, costumers_dictionary):
    """deposit to the bank some of money.

    Args:
    costumer_id (string): costumer id.
    amount_to_deposit (integer): amount the costumer wants to deposit.
    costumers_dictionary (dictionary): dictionary of all costumers in
                                       the bank.
    """
    if amount_to_deposit > 0:
        balance_now = check_the_balance(costumer_id, costumers_dictionary)
        new_balance = balance_now + amount_to_deposit
        costumers_dictionary[costumer_id][1] = str(new_balance)
        return True
    return False


def change_password(costumer_id, new_password, costumers_dictionary):
    """Changing the costumer's ATM password.

    Args:
    costumer_id (string): costumer id.
    new_password (integer): the new password the costumer wants to change to.
    costumers_dictionary (dictionary): dictionary of all costumers in
                                       the bank.
    """
    change_password_type = str(new_password)
    if new_password > 0:
        if len(change_password_type) == 4:
            costumers_dictionary[costumer_id][0] = change_password_type
            return True
    return False


def main():
    costumers_dictionary = {}
    try:
        with open(sys.argv[ATM_FILE], 'r') as atm_file:
            for line in atm_file:
                costumers_dictionary[line.split()[0]] = line.split()[1:]

    except FileNotFoundError:
        print("Your file path is incorrect. Please check it.")

    try:
        print("welcome to bank!\n")
        costumer_id = input("enter your id:\n")
        while costumer_id != str(-1):
            if len(costumer_id) == 9 and costumer_id.isdigit() and \
                    costumers_dictionary.get(costumer_id):
                print("for checking your balance press 1")
                print("for cash withdrawal press 2")
                print("for cash deposit press 3")
                print("for change password press 4")
                costumer_choice = int(input("pressing: \n"))

                if costumer_choice == 1:
                    print("your balance: ", end='')
                    print(check_the_balance
                          (costumer_id, costumers_dictionary))
                    costumer_id = input("enter your id/ to stop and save"
                                        " changes press (-1):\n")

                elif costumer_choice == 2:
                    amount_to_withdrawal = int(input("please enter the "
                                                     "amount to withdrawal:\n"
                                                     ""))
                    if cash_withdrawal(costumer_id, amount_to_withdrawal,
                                       costumers_dictionary):
                        print("The action was succeeded")
                        costumer_id = input("enter your id/ to stop and save"
                                            " changes press (-1):\n")
                    else:
                        print("failed - check your amount\n")

                elif costumer_choice == 3:
                    amount_to_deposit = int(input("please enter "
                                                  "the amount you want"
                                                  " to deposit: \n "))
                    if cash_deposit(costumer_id, amount_to_deposit,
                                    costumers_dictionary):
                        print("The action was succeeded")
                        costumer_id = input("enter your id/ to stop and save"
                                            " changes press (-1):\n")
                    else:
                        print("failed - check your amount\n")

                elif costumer_choice == 4:
                    new_password = int(input("enter a new password: \n"))
                    if change_password(costumer_id, new_password,
                                       costumers_dictionary):
                        print("password changed")
                        costumer_id = input("enter your id/ to stop and save"
                                            " changes press (-1):\n")
                    else:
                        print("not a good password, needs to be 4 digits:")

                else:
                    print("choose 1/2/3/4 option: ")
            else:
                costumer_id = input("the id isn't exists/isn't right, "
                                    "enter a new one:\n")

    except ValueError:
        print("Value Error! your input needs to be digit value")
    except Exception as e:
        print(e)
    finally:
        with open(sys.argv[ATM_FILE], 'w') as atm_file:
            for line in costumers_dictionary:
                atm_file.write(f"{line} {' '.join(costumers_dictionary[line])}"
                               f"\n")


if __name__ == '__main__':
    main()
