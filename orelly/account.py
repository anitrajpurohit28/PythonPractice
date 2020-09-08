#account.py
"""Account class Defination"""

from decimal import Decimal

class Account:
    """Account class from maintaining a bank account balance."""

    def __init__(self, name, balance):
        """Initialize an account object."""

        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= 0.00')

        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money to the account."""

        if amount < Decimal('0.0'):
            raise ValueError('Amount must be positive')
        self.balance += amount


