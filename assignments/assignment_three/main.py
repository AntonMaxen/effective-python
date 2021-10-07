import random
from bankapp.bank import Bank
from bankapp.generator import generate_user, generate_account
from bankapp.utils import class_utils as cu


def print_list(my_list):
    print()
    for e in my_list:
        print(e)


"""Example Usages"""
def search_by_wealth(bank):
    matched_accounts = bank.search_accounts_by_value(min_v=1337, max_v=1000000, desc=True)
    print_list(matched_accounts)
    print(f'total accounts: {len(bank.accounts)}')
    print(f'found: {len(matched_accounts)} accounts')


def bank_transfer(bank):
    matched_accounts = bank.search_accounts_by_kwargs(currency='kr')
    matched_accounts = cu.get_smaller_then_by_attribute(matched_accounts, 'amount', 100000)

    sender = random.choice(matched_accounts)
    receiver = random.choice(matched_accounts)
    while receiver == sender and len(matched_accounts) > 1:
        receiver = random.choice(matched_accounts)

    sender.transfer(receiver, 2000)


def generate_bank(bank, amount_users=1, amount_accounts=1):
    user_ids = [bank.create_user(**generate_user()) for i in range(amount_users)]
    users = [bank.get_user_by_id(user_id) for user_id in user_ids]
    account_ids = [bank.create_account(**generate_account(users)) for i in range(amount_accounts)]
    accounts = [bank.get_account_by_id(account_id) for account_id in account_ids]

    return users, accounts

def advanced_searching(bank):
    accounts = bank.search_accounts_by_kwargs(currency='kr')
    matches = []
    for account in accounts:
        matches.extend(account.search_user('max'))
        matches.extend(account.search_user('an'))

    matches = list(set(matches))

    for user in matches:
        user_accounts = bank.get_accounts_by_user_id(user.user_id)
        total = sum([account.amount for account in user_accounts if account.currency=='kr'])
        print(f'user: {user.first_name} {user.last_name}')
        print(f'Total amount: {total} kr')
        print(f'Across: {len(user_accounts)} Accounts.')
        print()


def add_myself(bank):
    matches = bank.search_users_by_kwargs(first_name='anton', last_name='maxen')
    if matches > 0:
        return matches[0]
    
    user_id = bank.create_user('Anton', 'Maxen')
    user = bank.get_user_by_id(user_id)
    account_id = bank.create_account(100000, 'kr', user)
    account = bank.get_account_by_id(account_id)

    return account

def find_my_accounts(bank):
    accounts = bank.search_accounts_by_kwargs(first_name='Anton', last_name='Maxen')
    print_list(accounts)
    print(f'Total accounts: {len(bank.accounts)}')
    print(f'Found: {len(accounts)}')


def remove_myself(bank):
    users = bank.search_users_by_kwargs(first_name='Anton', last_name='Maxen')

    for user in users:
        user_id = user.user_id
        accounts = bank.get_accounts_by_user_id(user_id)
        for account in accounts:
            bank.remove_account(account)

        bank.remove_user(user)


"""End Example Usages"""


def main():
    bank = Bank('Nordea', load_from_file=True)
    #generate_bank(bank, amount_users=100, amount_accounts=40)

    bank_transfer(bank)
    #search_by_wealth(bank)
    #my_account = add_myself(bank)
    #remove_myself(bank)
    #add_myself(bank)
    advanced_searching(bank)
    #find_my_accounts(bank)


    bank.save()


if __name__ == '__main__':
    main()
