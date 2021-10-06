class User:
    def __init__(self, first_name, last_name, user_id):
        """
        Initialize User object with passed arguments.

        Args:
            first_name: first_name of the user.
            last_name: last_name of the user.
            user_id: unique user_id for the user.

        """
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        """
        Take attributes and child class attributes and returns a dictionary
        representation of self.

        Returns:
            dictionary representation of self.

        """
        return {
            'user_id': str(self.user_id),
            'first_name': self.first_name,
            'last_name': self.last_name
        }

    def __str__(self):
        """
        String representation for the User object.

        Returns:
            string representation of the User object.

        """
        return (
            f'| Firstname: {self.first_name}\n'
            f'| Lastname: {self.last_name}\n'
            f'| User_ID: {self.user_id}\n'
            f'|-------------------------------------------------'
        )
