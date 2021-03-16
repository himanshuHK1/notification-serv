from database import users, roles, user_role_map


class AddUser:
    """
     Class to add user to system
    """

    def __init__(self, input_data):
        self.user = input_data[1]
        self.role = input_data[2]

    def add(self):
        """
            Func to add user to system
        :return: Success/Failed message
        """
        if self.role not in roles:
            return f"User creation failed, error: Role {self.role} not in system"

        if self.user not in users:
            users.append(self.user)
            user_role_map[self.user] = self.role
            return f"User {self.user} creation success!!"
        else:
            return f"User creation failed, error: User already in system"



