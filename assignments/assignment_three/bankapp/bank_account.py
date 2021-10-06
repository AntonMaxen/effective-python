from .user import User
from .utils import class_utils as cu


class BankAccount:
    """Bank account class that keeps track of money and users."""
    def __init__(self, amount, currency, account_id, users=None):
        """
        Initialize BankAccount object with passed arguments and keyword
        arguments.

        Args:
            amount: amount of money to start the account with.
            currency: the currency as str.
            account_id: id for the bankaccount.
            users: list of User object to start the account with.

        """
        self.amount = amount
        self.currency = currency
        self.account_id = account_id

        users = [users] if isinstance(users, User) else users
        if isinstance(users, list) and cu.all_is_instance_of(users, User):
            self.users = users
        else:
            self.users = []

    def add_user(self, user):
        """
        add a User object to self.users.

        Args:
            user: User object

        """
        if user not in self.users:
            self.users.append(user)

    def remove_user(self, user):
        """
        Remove User object from self.users.

        Args:
            user: the User object to remove.

        """
        if user in self.users:
            self.users.remove(user)

    def get_user_by_id(self, user_id):
        """
        returns a User object that matches user_id.

        Args:
            user_id: user_id to search for.
        Returns:
            match: the found User object or None.

        """
        matches = cu.get_exact_matches_by_attribute(
            self.users,
            'user_id',
            user_id,
            insensitive=False
        )
        match = matches[0] if len(matches) > 0 else None
        return match

    def withdraw(self, amount, user=None):
        """
        withdraws amount from self.amount

        Args:
            amount: The amount to withdraw.
            user: for logging purposes #TODO

        """
        if self.amount < amount:
            print('Not Enough Balance on account')
            return

        self.amount -= amount

        print(f'Withdrawing {amount} from Account_ID: {self.account_id}')
        print(f'New balance: {self.amount + amount} -> {self.amount}')

        return self.amount

    def deposit(self, amount, user=None):
        """
        deposits amount from self.amount

        Args:
            amount: The amount to deposit.
            user: for logging purposes #TODO.
        Returns:
            self.amount: The updated amount.

        """
        self.amount += amount
        print(f'Depositing {amount} into Account_ID: {self.account_id}')
        print(f'New balance: {self.amount - amount} -> {self.amount}')
        return self.amount

    def transfer(self, other, amount, user=None):
        """
        Transfers money from self to other.

        Args:
            other: BankAccount object of the receiver.
            amount: The amount that self will send other.
        Returns:
            self.amount: The updated amount.

        """
        if self == other:
            print('You can\'t transer to yourself')
            return
        if self.currency != other.currency:
            print('Can only transfer to account with same currency')
            return

        if self.amount < amount:
            print('Not Enough Balance on Account')
            return

        self.amount -= amount
        other.amount += amount

        print(f'Transfering {amount}')
        print(f'From Account_ID: {self.account_id}')
        print(f'To Account_ID: {other.account_id}')
        print(f'New balance: {self.amount + amount} -> {self.amount}')

        return self.amount

    def balance(self):
        """
        Returns balance of the account.

        Returns:
            self.amount: the amount of the BankAcccount object.

        """
        return self.amount

    def search_user(self, query):
        """
        search for users in bankaccount with a query.

        Args:
            query: a string that is used to search for users.
        Returns:
            unique_matches: list of users that matched the query.

        """
        if len(self.users) < 1:
            return []

        str_attributes = cu.get_class_str_attributes(self.users[0])
        final_matches = []
        for attribute in str_attributes:
            matches = cu.get_part_matches_by_attribute(self.users, attribute, query)
            final_matches.extend(matches)

        unique_matches = list(set(final_matches))
        return unique_matches

    def search_user_by_kwargs(self, **kwargs):
        """
        Search all users using keyword arguments.
        Example: first_name='anton', last_name='maxen'

        Args:
            kwargs: keywordarguments to use in search.
        Returns:
            list of users that matches keywordarguments.

        """
        if len(self.users) < 1:
            return []

        final_matches = []
        for key, value in kwargs.items():
            matches = cu.get_exact_matches_by_attribute(self.users, key, value)
            final_matches.extend(matches)

        unique_matches = list(set(final_matches))
        return unique_matches

    def to_dict(self):
        """
        Take attributes and child class attributes and returns a dictionary
        representation of self.

        Returns:
            dictionary representation of self.

        """
        return {
            'amount': self.amount,
            'currency': self.currency,
            'account_id': str(self.account_id),
            'users': [user.to_dict() for user in self.users]
        }

    def __str__(self):
        """
        String representation for the BankAccount object.

        Returns:
            string representation of the BankAccount object.

        """
        separator = '\n'
        user_string = separator.join([str(user) for user in self.users])
        return (
            f'| Amount: {self.amount}\n'
            f'| Currency: {self.currency}\n'
            f'| Account ID: {self.account_id}\n'
            f'|=================================================\n'
            f'| [Users: {len(self.users)}]\n'
            f'{user_string}\n'
            f'|+++++++++++++++++++++++++++++++++++++++++++++++++'
        )
