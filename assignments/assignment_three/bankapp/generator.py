from faker import Faker
import random

fake = Faker()


def generate_user():
    """
    generates a fake user_dict

    Returns:
        dictionary with user_info

    """
    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name()
    }


def generate_account(all_users):
    """
    generates a fake account_dict.

    Args:
        all_users: list of users_objects.
    Returns:
        dictionary with account_info

    """
    min_amount = 1
    max_amount = 10000000
    bracket = random.randint(1, 100)

    if bracket <= 50:
        max_amount /= 100
    elif 50 < bracket <= 90:
        max_amount /= 10

    amount = random.randint(min_amount, max_amount)

    currency = random.choice(['kr', 'dollar', 'pound'])
    users = [random.choice(all_users) for _ in range(random.randint(1, 3))]

    return {
        'amount': amount,
        'currency': currency,
        'users': users
    }
