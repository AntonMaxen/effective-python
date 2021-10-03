from .bank_account import BankAccount
from .user import User
from .utils import class_utils as cu

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
        matches = cu.get_exact_matches_by_attribute(self.accounts, 'account_id', account_id, insensitive=False)
        match = matches[0] if len(matches) > 0 else None
        return match

    def generate_account_id(self):
        return cu.generate_unique_id(self.accounts, 'account_id')

    def get_accounts_by_user_id(self, user_id):
        return [a for a in self.accounts if a.get_user_by_id(user_id)]

    def search_accounts(self, query):
        matches = []
        for account in self.accounts:
            if account.search_user(query) and account not in matches:
                matches.append(account)

        return matches

    def search_accounts_by_kwargs(self, **kwargs):
        account_matches = []

        for account in self.accounts:
            if account.search_user_by_kwargs(**kwargs):
                account_matches.append(account)


        account_specific_matches = [cu.get_exact_matches_by_attribute(self.accounts, key, value) for key, value in kwargs.items()]
        account_specific_matches = [m for m_list in account_specific_matches for m in m_list]
        account_matches.extend(account_specific_matches)

        return list(set(account_matches))
    
    def search_accounts_by_value(self, min_v=0, max_v=10000, inclusive=True, desc=False):
        matches = cu.get_bigger_then_by_attribute(self.accounts, 'amount', min_v, inclusive=inclusive)
        matches = cu.get_smaller_then_by_attribute(matches, 'amount', max_v, inclusive=inclusive)

        unique_matches = list(set(matches))
        sorted_matches = sorted(unique_matches, key=lambda a: a.amount, reverse=desc)

        return sorted_matches


    """User Methods"""

    def create_user(self, first_name, last_name):
        user_id = self.generate_user_id()
        created_user = User(first_name, last_name, user_id)
        self.users.append(created_user)

        return user_id

    def get_user_by_id(self, user_id):
        matches = cu.get_exact_matches_by_attribute(self.users, 'user_id', user_id, insensitive=False)
        match = matches[0] if len(matches) > 0 else None
        return match 

    def generate_user_id(self):
        return cu.generate_unique_id(self.users, 'user_id')

