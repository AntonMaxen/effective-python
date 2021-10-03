import random
from bankapp.bank import Bank 
from bankapp.generator import generate_user, generate_account
from bankapp.utils import class_utils as cu

def print_list(my_list):
    print()
    for e in my_list:
        print(e)

def search_by_wealth(bank):
    matched_accounts = bank.search_accounts_by_value(max_v=1000000, desc=True)
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


def main():
    bank = Bank('Nordea')
    AMOUNT_USERS = 100
    AMOUNT_ACCOUNTS = 50
    user_ids = [bank.create_user(**generate_user()) for i in range(AMOUNT_USERS)]
    user_ids.append(bank.create_user('Anton', 'Maxen'))
    users = [bank.get_user_by_id(user_id) for user_id in user_ids]
    
    account_ids = [bank.create_account(**generate_account(users)) for i in range(AMOUNT_ACCOUNTS)]
    account_ids.append(bank.create_account(100000, 'kr', users[-1]))
    accounts = [bank.get_account_by_id(account_id) for account_id in account_ids]

    #search_by_wealth(bank)
    bank_transfer(bank)




if __name__ == '__main__':
    main()

