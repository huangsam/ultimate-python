"""
Encapsulation is a feature of OOP that allows you to hide the
implementation details of a class from its users.
Encapsulation allows us to limit the access of certain attributes
within a class. This prevents users from directly accessing and modifying such
attributes from outside the class. Instead, users must use methods to access and
modify attributes.
"""
import random


class BankAccount:
    def __init__(self, account_holder_name):
        """
        In python, a class attribute can be made private by prefixing it with two underscores.
        This makes it inaccessible to users outside the class.
        By default, class attributes are public. Therefore, they can be accessed and modified
        outside of the class.

        Here, account_number and balace are private while account_holder_name is public.
        """
        self.account_holder_name = account_holder_name
        """
        The account number is generated automaticallyusing the randint function from
        the random module when a new instance of the class is created.
        The balance is set to 0.0 by default.
        """
        self.__account_number = random.randint(1000000000, 9999999999)  # generate a random account number of 10 digits.
        self.__balance = 0.0

    def deposit(self, balance):
        self.__balance += balance  # add the deposited amount to the balance.

    def withdraw(self, balance):
        self.__balance -= balance

    def get_balance(self):
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

    def delete_account(self):
        """
        This method is used to delete an account.
        """
        self.__balance = 0.0
        self.__set_account_number(0)
        self.account_holder_name = ""


def main():
    # Account names constants.
    USER1 = "John Doe"
    USER2 = "Jane Doe"

    # Account instances.
    account1 = BankAccount(USER1)
    account2 = BankAccount(USER2)

    # Accounts list.
    accounts = [account1, account2]

    assert account1.account_holder_name == USER1
    assert account2.account_holder_name == USER2

    # Check if the accounts are an instance of the BankAccount class.
    assert all(isinstance(account, BankAccount) for account in accounts)
    # Check if the account balance are floats.
    assert all(isinstance(account.get_balance(), float) for account in accounts)
    # Check if the account balance are integers.
    assert all(isinstance(account.get_account_number(), int) for account in accounts)

    # Deposit amount and check if the balance is updated.
    account1.deposit(100.0)
    assert (account1.get_balance() == 100.0)

    # Withdraw amount and check if the balance is updated.
    account1.withdraw(50.0)
    assert (account1.get_balance() == 50.0)

    # Assert the data types of account balance.
    assert (isinstance(account1.get_balance(), float))

    # Delete account and assert values.
    account1.delete_account()
    assert (account1.get_balance() == 0.0)
    assert (account1.get_account_number() == 0)
    assert (account1.account_holder_name == "")


if __name__ == "__main__":
    main()
