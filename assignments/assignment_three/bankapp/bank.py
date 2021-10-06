import os
import json
import uuid

from .bank_account import BankAccount
from .user import User
from .utils import class_utils as cu


class Bank:
    """Bank class that holds users and bankaccounts"""

    def __init__(self, name, load_from_file=False, filename='data.json'):
        """
        Initialize bank object depending on what args and kwargs passed.

        Args:
            name: name of the bank
            load_from_file: True if you want to load bank from local json.
            filename: path to the json file to load and save data.

        """
        self.name = name
        self.filename = filename
        self.accounts = []
        self.users = []

        if load_from_file and os.path.isfile(self.filename):
            self._load()

    def _load(self):
        """
        Loads the class object with data that is located in self.filename.
        """
        with open(self.filename, 'r', encoding='utf8') as json_file:
            json_obj = json.load(json_file)

        self.name = json_obj.get('name', self.name)

        users = json_obj.get('users', [])
        accounts = json_obj.get('accounts', [])

        for user in users:
            user_id = user.get('user_id')
            first_name = user.get('first_name')
            last_name = user.get('last_name')
            self.create_user(first_name, last_name, user_id=user_id)

        for account in accounts:
            amount = account.get('amount')
            currency = account.get('currency')
            account_id = account.get('account_id')
            user_list = account.get('users', [])
            user_objects = [self.get_user_by_id(u.get('user_id')) for u in user_list]
            self.create_account(amount, currency, user_objects, account_id=account_id)

    def save(self):
        """
        save class attributes to a json file.
        """
        json_dict = self.to_dict()

        with open(self.filename, 'w', encoding='utf8') as json_file:
            json.dump(json_dict, json_file, indent=4)

    """Account Methods"""
    def create_account(self, amount, currency, users, account_id=None):
        """
        Creates a BankAccount object and stores it to self.accounts.

        Args:
            amount: amount of money to start the account with.
            currency: a str that tells what currency it is.
            users: user or list of users that you want to open the account with.
            account_id: if you want to use a specific account_id
        Returns:
            account_id: Returns account_id of the created BankAccount object.

        """
        if account_id and not self.get_account_by_id(account_id):
            account_id = uuid.UUID(account_id)
        else:
            account_id = self.generate_account_id()

        created_account = BankAccount(amount, currency, account_id, users)
        self.accounts.append(created_account)

        return account_id

    def get_account_by_id(self, account_id):
        """
        Returns BankAccount object if there is a BankAccount object with
        account_id: account_id

        Args:
            account_id: The account_id to check for.
        Returns:
            account_id or None if not found.

        """
        matches = cu.get_exact_matches_by_attribute(
            self.accounts,
            'account_id',
            account_id,
            insensitive=False
        )
        match = matches[0] if len(matches) > 0 else None
        return match

    def generate_account_id(self):
        """
        Generates a unique account_id.

        Returns:
            Unique uuid object.

        """
        return cu.generate_unique_id(self.accounts, 'account_id')

    def get_accounts_by_user_id(self, user_id):
        """
        Get all accounts that (user with user_id) owns.

        Args:
            user_id: The user_id to search for
        Returns:
            List of accounts that the user owns.

        """
        return [a for a in self.accounts if a.get_user_by_id(user_id)]

    def search_accounts(self, query):
        """
        search all accounts using a query. Also searches the users in each
        bankaccount.

        Args:
            query: a string to search for with insensitive search.
        Returns:
            list of accounts matching the query.

        """
        matches = []
        for account in self.accounts:
            if account.search_user(query) and account not in matches:
                matches.append(account)

        return matches

    def search_accounts_by_kwargs(self, **kwargs):
        """
        Search all accounts and subclasses using keyword arguments.
        Example: first_name='anton', last_name='maxen'

        Args:
            kwargs: keywordarguments to use in search.
        Returns:
            list of accounts that matches keywordarguments.

        """
        account_matches = []

        for account in self.accounts:
            if account.search_user_by_kwargs(**kwargs):
                account_matches.append(account)

        account_specific_matches = [cu.get_exact_matches_by_attribute(self.accounts, key, value)
                                    for key, value in kwargs.items()]
        account_specific_matches = [m for m_list in account_specific_matches for m in m_list]
        account_matches.extend(account_specific_matches)

        return list(set(account_matches))

    def search_accounts_by_value(self, min_v=0, max_v=10000, inclusive=True, desc=False):
        """
        Search accounts whose money amount that matches passed range of values.

        Args:
            min_v: minimum accepted money amount.
            max_v: maximum accepted money amount.
            inclusive: if the range should be inclusive or not.
            desc: if the matches should be sorted desc.
        Returns:
            sorted_matches: list of sorted matches.

        """
        matches = cu.get_bigger_then_by_attribute(
            self.accounts,
            'amount',
            min_v,
            inclusive=inclusive
        )
        matches = cu.get_smaller_then_by_attribute(
            matches,
            'amount',
            max_v,
            inclusive=inclusive
        )

        unique_matches = list(set(matches))
        sorted_matches = sorted(unique_matches, key=lambda a: a.amount, reverse=desc)

        return sorted_matches

    """User Methods"""
    def create_user(self, first_name, last_name, user_id=None):
        """
        Creates a User object and stores it in self.users

        Args:
            first_name: first_name of the user you want to create.
            last_name: last_name of the user you want to create.
            user_id: if you want to use a specific user_id.
        Returns:
            user_id: Returns the user_id of the created User object.

        """
        if user_id and not self.get_user_by_id(user_id):
            user_id = uuid.UUID(user_id)
        else:
            user_id = self.generate_user_id()

        created_user = User(first_name, last_name, user_id)
        self.users.append(created_user)

        return user_id

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

    def generate_user_id(self):
        """
        Generates a unique user_id

        Returns:
            unique uuid object

        """
        return cu.generate_unique_id(self.users, 'user_id')

    def to_dict(self):
        """
        Take attributes and child class attributes and returns a dictionary
        representation of self.

        Returns:
            dictionary representation of self.

        """
        return {
            'name': self.name,
            'accounts': [account.to_dict() for account in self.accounts],
            'users': [user.to_dict() for user in self.users]
        }
