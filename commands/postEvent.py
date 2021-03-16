from database import topics, topic_message_queue
from constants import ADMIN_ROLE


class PostEvent:
    """
     Class to post an event to system
    """

    def __init__(self, input_data):
        self.message = input_data[1]

    def post_event(self):
        """
            Post event to system
        :return: str
        """
        if not isinstance(self.message, dict):
            return "Invalid message body received"
        try:
            id = self.message['id']
            topic_name = self.message['topicName']
            text_message = self.message['Text']
            if topic_name not in topics:
                return f"Topic {topic_name} does not exist in System"
            topic_message_queue.append([id, topic_name, text_message])
            return "Message will be delivered to the desired users in a while"

        except KeyError as key:
            return f"{key} is missing in request message"


