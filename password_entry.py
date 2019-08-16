"""
Tyler Horsford
"""

def repeat_message(message, number_of_messages):
    for i in range(number_of_messages):
        print(message)


def main():
    message = input("Enter your message: ")
    number_of_messages = int(input("Enter number of times you would like the message repeated. "))

    repeat_message(message, number_of_messages)


main()
