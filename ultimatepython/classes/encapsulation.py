"""
Encapsulation is a feature of OOP that allows you to hide the
implementation details of a class from its users.
Encapsulation allows us to limit the access of certain attributes
within a class. This prevents users from directly accessing and modifying such
attributes from outside the class. Instead, users must use methods to access and
modify attributes.
"""
import secrets

# Module-level constanct
_INVALID_AMOUNT_MESSAGE = "Invalid amount."
_INSUFFICIENT_BALANCE_MESSAGE = "Insufficient balance."


class BankAccount:
    def __init__(self, account_holder_name):
        """
        In Python, a class attribute can be made private by prefixing it with two underscores.
        This makes it inaccessible to users outside the class.
        By default, class attributes are public. Therefore, they can be accessed and modified
        outside of the class.

        Here, account_number and balance are private while account_holder_name is public.
        """
        self.account_holder_name = account_holder_name
        """
        The account number is generated automatically using the randbelow function from
        the random module when a new instance of the class is created.
        The balance is set to 0 by default.
        """
        self.__account_number = secrets.randbelow(10**10)  # generate a random account number of 10 digits.
        self.__balance = 0

    def deposit(self, balance):
        """
        The deposit function is used to add new balance to the account.
        The provided balance is added to the existing balance.
        """
        self.__balance += int(balance)

    def withdraw(self, balance):
        """
        The withraw method is used to deduct the balance from the account.
        In case there is insufficient balance, or the input is invalid,
        a value error is raised.
        """
        if balance <= 0:
            raise ValueError(_INVALID_AMOUNT_MESSAGE)
        if balance > self.__balance:
            raise ValueError(_INSUFFICIENT_BALANCE_MESSAGE)

        self.__balance -= balance

    def get_balance(self):
        """
        This function returs the available balance in the account.
        """
        return self.__balance

    def get_account_number(self):
        """
        The account number is generated randomly when a new instance of the class is created.
        Since the attribute is also private, it cannot be accessed directly from outside the class.
        The get_account_number method allows you to access the account number outside of the class.
        But since we do not define a setter method for this variable, we cannot modify it outside the class.
        Therefore, the account number generated while creating an object of the BankAccount class cannot be changed
        but can only be read using this function.
        """
        return self.__account_number

    def __set_account_number(self, number):
        """
        This is a private method. Similar to private variables,
        private methods also cannot be accessed outside the class.
        """
        self.__account_number = number

    def remove_account_details(self):
        """
        This method is used to reset the account details.
        Here, the __set_account_number function is private.
        This, it cannot be called from outside the class.
        However, the remove_account_details calls the function from
        inside the class and as it is a public method, it can be called from
        outside the class.
        """
        self.__balance = 0
        self.__set_account_number(0)
        self.account_holder_name = ""


def main():
    # Account names constants.
    USER1 = "John Doe"
    USER2 = "Jane Doe"

    # Account instances.
    account1 = BankAccount(USER1)
    account2 = BankAccount(USER2)

    assert account1.account_holder_name == USER1
    assert account2.account_holder_name == USER2

    # Deposit amount and check if the balance is updated.
    account1.deposit(100)
    assert account1.get_balance() == 100

    # Withdraw amount and check if the balance is updated.
    account1.withdraw(50)
    assert account1.get_balance() == 50

    # validating invalid amounts.
    error_inputs = [-10, 0, 150]
    for input in error_inputs:
        try:
            account1.withdraw(input)
        except ValueError as e:
            assert str(e) in {_INSUFFICIENT_BALANCE_MESSAGE, _INVALID_AMOUNT_MESSAGE}

    # Remove account details and assert values.
    account1.remove_account_details()

    assert account1.get_balance() == 0
    assert account1.get_account_number() == 0
    assert account1.account_holder_name == ""


if __name__ == "__main__":
    main()
