import utils as ut
from generator import generate_user, generate_account


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.users = []


    """Account Methods"""

    def create_account(self, amount, currency, users):
        account_id = self.generate_account_id()
        created_account = BankAccount(amount, currency, account_id, users)
        self.accounts.append(created_account)

        return account_id


    def get_account_by_id(self, account_id):
        matches = ut.get_exact_matches_by_attribute(self.accounts, 'account_id', account_id, insensitive=False)
        match = matches[0] if len(matches) > 0 else None
        return match

    def generate_account_id(self):
        return ut.generate_unique_id(self.accounts, 'account_id')

    def get_accounts_by_user_id(self, user_id):
        return [a for a in self.accounts if a.get_user_by_id(user_id)]

    
    """User Methods"""

    def create_user(self, first_name, last_name):
        user_id = self.generate_user_id()
        created_user = User(first_name, last_name, user_id)
        self.users.append(created_user)

        return user_id

    def get_user_by_id(self, user_id):
        matches = ut.get_exact_matches_by_attribute(self.users, 'user_id', user_id, insensitive=False)
        match = matches[0] if len(matches) > 0 else None
        return match 



    def generate_user_id(self):
        return ut.generate_unique_id(self.users, 'user_id')

    """Static Methods"""


class User:
    def __init__(self, first_name, last_name, user_id):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return (
            f'Firstname: {self.first_name}\n'
            f'Lastname: {self.last_name}\n'
            f'User_ID: {self.user_id}'
        )

class BankAccount:
    def __init__(self, amount, currency, account_id, users=None):
        self.amount = amount
        self.currency = currency
        self.account_id = account_id
        
        users = [users] if isinstance(users, User) else users
        if isinstance(users, list) and ut.all_is_instance_of(users, User):
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
        matches = ut.get_exact_matches_by_attribute(self.users, 'user_id', user_id, insensitive=False)
        match = matches[0] if len(matches) > 0 else None
        return match 

    def search_user(self, query):
        if len(self.users) < 1:
            return []

        str_attributes = ut.get_class_str_attributes(self.users[0])
        final_matches = []
        for attribute in str_attributes:
            matches = list(set([m for m in ut.get_part_matches_by_attribute(self.users, attribute, query)]))
            final_matches.extend([match for match in matches if match not in final_matches])

        return final_matches

    def __str__(self):
        separator = '\n' + '-' * 20 + '\n'
        user_string = separator.join([str(user) for user in self.users])
        return (
            f'Amount: {self.amount}\n'
            f'Currency: {self.currency}\n'
            f'Account ID: {self.account_id}\n'
            f'\nUsers: {len(self.users)}\n'
            f'{user_string}\n'
            f'============================'
        )


def main():
    bank = Bank('Nordea')
    AMOUNT_USERS = 100
    AMOUNT_ACCOUNTS = 50
    user_ids = [bank.create_user(**generate_user()) for i in range(AMOUNT_USERS)]
    users = [bank.get_user_by_id(user_id) for user_id in user_ids]
    
    accounts_ids = [bank.create_account(**generate_account(users)) for i in range(AMOUNT_ACCOUNTS)]
    accounts = [bank.get_account_by_id(account_id) for account_id in accounts_ids]




    for account in accounts:
        print(len([user for user in account.users]))


    matched_accounts = bank.get_accounts_by_user_id(user_ids[1])
    for account in matched_accounts:
        print(account)


if __name__ == '__main__':
    main()

