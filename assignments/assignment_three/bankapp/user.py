class User:
    def __init__(self, first_name, last_name, user_id):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return (
            f'| Firstname: {self.first_name}\n'
            f'| Lastname: {self.last_name}\n'
            f'| User_ID: {self.user_id}\n'
            f'|-------------------------------------------------'
        )

