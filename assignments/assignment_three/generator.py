from faker import Faker
import random

fake = Faker()

def generate_user():
    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name()
    }


def generate_account(all_users):
    amount = random.randint(1, 10000000)
    currency = random.choice(['kr', 'dollar', 'pound'])
    users = [random.choice(all_users) for _ in range(random.randint(1, 3))]

    return {
        'amount': amount,
        'currency': currency,
        'users': users
    } 
