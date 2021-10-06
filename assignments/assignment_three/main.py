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
    print(matched_accounts)

    sender = random.choice(matched_accounts)
    receiver = random.choice(matched_accounts)
    while receiver == sender and len(matched_accounts) > 1:
        receiver = random.choice(matched_accounts)

    print(receiver.amount)
    sender.transfer(receiver, 2000)
    print(receiver.amount)


def generate_bank(bank, amount_users=1, amount_accounts=1):
    user_ids = [bank.create_user(**generate_user()) for i in range(amount_users)]
    users = [bank.get_user_by_id(user_id) for user_id in user_ids]
    account_ids = [bank.create_account(**generate_account(users)) for i in range(amount_accounts)]
    accounts = [bank.get_account_by_id(account_id) for account_id in account_ids]

    return users, accounts


def add_myself(bank):
    user_id = bank.create_user('Anton', 'Maxen')
    user = bank.get_user_by_id(user_id)
    account_id = bank.create_account(100000, 'kr', user)
    account = bank.get_account_by_id(account_id)

    return account


def remove_myself(bank):
    matches = bank.search_accounts_by_kwargs(first_name='Anton', last_name='Maxen')
    bank.remove_account()


"""End Example Usages"""


def main():
    bank = Bank('Nordea', load_from_file=True)
    #generate_bank(bank, amount_users=100, amount_accounts=40)

    bank_transfer(bank)
    #search_by_wealth(bank)
    #my_account = add_myself(bank)

    bank.save()


if __name__ == '__main__':
    main()
