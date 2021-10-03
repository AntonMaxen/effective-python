class User:
    def __init__(self, first_name, last_name, user_id):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name



def props(cls):
    return [i for i in cls.__dict__]


print(props(User))
user_1 = User('a', 'b', 'c')
user_2 = User('a', 'b', 'c')
user_3 = User('a', 'b', 'c')
user_4 = User('a', 'b', 'c')
users = [user_1, user_2, user_3, user_4]
attrs = [a for a in users[0].__dict__.keys() if isinstance(a, str)]
print(attrs)
