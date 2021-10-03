from .user import User
from .utils import class_utils as cu

class BankAccount:
    def __init__(self, amount, currency, account_id, users=None):
        self.amount = amount
        self.currency = currency
        self.account_id = account_id
        
        users = [users] if isinstance(users, User) else users
        if isinstance(users, list) and cu.all_is_instance_of(users, User):
            self.users = users
        else:
            self.users = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)

    def get_user_by_id(self, user_id):
        matches = cu.get_exact_matches_by_attribute(self.users, 'user_id', user_id, insensitive=False)
        match = matches[0] if len(matches) > 0 else None
        return match 

    def withdraw(self, amount, user=None):
        if self.amount < amount:
            print('Not Enough Balance on account')
            return

        self.amount -= amount

        print(f'Withdrawing {amount} from Account_ID: {self.account_id}')
        print(f'New balance: {self.amount + amount} -> {self.amount}')

        return self.amount

    def deposit(self, amount, user=None):
        self.amount += amount
        print(f'Depositing {amount} into Account_ID: {self.account_id}')
        print(f'New balance: {self.amount - amount} -> {self.amount}')
        return self.amount

    def transfer(self, other, amount, user=None):
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
        return self.amount

    def search_user(self, query):
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
        if len(self.users) < 1:
            return []

        final_matches = []
        for key, value in kwargs.items():
            matches = cu.get_exact_matches_by_attribute(self.users, key, value)
            final_matches.extend(matches)

        unique_matches = list(set(final_matches))
        return unique_matches

    def __str__(self):
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

