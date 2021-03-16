from database import users, user_topic_map, topics


class SubscribeTopic:
    """
     Class to subscribe a topic to user
    """

    def __init__(self, input_data):
        self.user = input_data[1]
        self.topic_name = input_data[2]

    @staticmethod
    def list_subscriptions(user):
        """List all subscriptions for user"""
        if user not in users:
            return f"User {user} does not exist in System"

        user_subscriptions = user_topic_map.get(user)
        if not user_subscriptions:
            return f"No topic subscribed by the user"

        return f"Topics subscribed by user {user}: {user_subscriptions}"

    def subscribe(self):
        """
            Subscribe topic to user
        :return: str -> success/Failure Message
        """
        if self.user not in users:
            return f"User {self.user} does not exist in System"

        if self.topic_name not in topics:
            return f"Topic {self.topic_name} does not exist in System"

        if user_topic_map.get(self.user):
            if self.topic_name in user_topic_map[self.user]:
                return "Topic already added to user"
            user_topic_map[self.user].append(self.topic_name)
        else:
            user_topic_map[self.user] = [self.topic_name]

        return f"Topic {self.topic_name} successfully subscribed to user {self.user}"








