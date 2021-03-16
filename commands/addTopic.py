from database import users, user_role_map, topics
from constants import ADMIN_ROLE


class AddTopic:
    """
     Class to add a topic to system
    """

    def __init__(self, input_data):
        self.user = input_data[1]
        self.topic_name = input_data[2]

    def add(self):
        """
            Subscribe topic to user
        :return: str -> success/Failure Message
        """
        if self.user not in users:
            return f"User {self.user} does not exist in System"

        user_role = user_role_map.get(self.user)
        if user_role != ADMIN_ROLE:
            return "Only Admin Users can add a topic to system"

        if self.topic_name not in topics:
            topics.append(self.topic_name)
            return f"Topic {self.topic_name} successfully added to system"
        else:
            return f"Topic {self.topic_name} successfully present in system"





