from constants import *
from commands import *



class System:
    # COMMAND_FUNC_MAPPING = {
    #     ADD_USER_COMMAND: validate_commands()
    #
    # }

    def validate_and_execute_command(self, input_data):
        command = input_data[0]
        if command == ADD_USER_COMMAND:
            if len(input_data) != 3:
                print(INVALID_FIELD_ERROR)

            response = AddUser(input_data).add()
            print(response)
        elif command == ADD_TOPIC_COMMAND:
            if len(input_data) != 3:
                print(INVALID_FIELD_ERROR)

            response = AddTopic(input_data).add()
            print(response)
        elif command == SUBSCRIBE_TOPIC_COMMAND:
            if len(input_data) != 3:
                print(INVALID_FIELD_ERROR)

            response = SubscribeTopic(input_data).subscribe()
            print(response)
        elif command == VIEW_SUBSCRIBE_TOPICS_COMMAND:
            if len(input_data) != 2:
                print(INVALID_FIELD_ERROR)

            response = SubscribeTopic.list_subscriptions(input_data[1])
            print(response)
        elif command == POST_EVENT_COMMAND:
            if len(input_data) != 2:
                print(INVALID_FIELD_ERROR)

            response = PostEvent(input_data).post_event()
            print(response)
        else:
            print("Invalid command, please enter correct command")



    def take_input(self):
        try:
            while True:
                input_data = str(input())
                input_data = input_data.split(" ")
                self.validate_and_execute_command(input_data)

        except KeyboardInterrupt:
            print("GoodBye, Have a nice day!!")


if __name__ == "__main__":
    System().take_input()





